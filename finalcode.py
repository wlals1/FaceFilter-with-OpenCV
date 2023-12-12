import cv2
import imageio

def detect_and_draw(img, cascade, nested_cascade, scale, glasses):
    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fx = 1 / scale
    small_img = cv2.resize(gray, None, fx=fx, fy=fx, interpolation=cv2.INTER_LINEAR_EXACT)
    cv2.equalizeHist(small_img, small_img)
    
    faces = cascade.detectMultiScale(small_img, 1.1, 2, 0 | cv2.CASCADE_SCALE_IMAGE, minSize=(30, 30))
    
    for i, (x, y, w, h) in enumerate(faces):
        if not nested_cascade.empty():
            small_img_roi = small_img[y:y + h, x:x + w]
            nested_objects = nested_cascade.detectMultiScale(small_img_roi, 1.1, 2, 0 | cv2.CASCADE_SCALE_IMAGE, minSize=(20, 20))

            points = []
            for (nx, ny, nw, nh) in nested_objects:
                center = (round((x + nx + nw * 0.5) / scale), round((y + ny + nh * 0.5) / scale))
                points.append(center)
                
            if len(points) == 2:
                center1, center2 = points
                center = ((center1[0] + center2[0]) // 2, (center1[1] + center2[1]) // 2)
                width = 4 * abs(center2[0] - center1[0])
                height = 1 * width  # 가로:세로 비율 3:1로 고정

                img_scale = width / glasses.shape[1]
                glasses_resized = cv2.resize(glasses, (int(width), int(height)))

                output = overlay_image(output, glasses_resized, center)
    
    return output

def overlay_image(background, foreground, location):
    output = background.copy()

    y_offset, x_offset = location[1] - foreground.shape[0] // 2, location[0] - foreground.shape[1] // 2

    for y in range(max(y_offset, 0), min(y_offset + foreground.shape[0], background.shape[0])):
        for x in range(max(x_offset, 0), min(x_offset + foreground.shape[1], background.shape[1])):
            if foreground[y - y_offset, x - x_offset, 3] != 0:
                output[y, x] = foreground[y - y_offset, x - x_offset, :3]

    return output

def bgr_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cascade_name = 'haarcascade_frontalface_alt.xml'
nested_cascade_name = 'haarcascade_eye_tree_eyeglasses.xml'

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_name)
nested_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + nested_cascade_name)

glasses_image = './sunglasses.png'
glasses = cv2.imread(glasses_image, cv2.IMREAD_UNCHANGED)

if glasses is None:
    print("Could not read image -", glasses_image)
    exit()


capture = cv2.VideoCapture(0)
    
frames = []

for _ in range(30):
    ret, frame = capture.read()

    if frame is None:
        break

    result_frame = detect_and_draw(frame, cascade, nested_cascade, 1, glasses)

    result_frame_rgb = bgr_to_rgb(result_frame)
    
    frames.append(result_frame)

imageio.mimsave('output.gif', [bgr_to_rgb(frame) for frame in frames], duration=0.1)

capture.release()
cv2.destroyAllWindows()