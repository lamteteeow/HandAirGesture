import cv2
import pydirectinput as pdi
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a hand landmarker instance with the live stream mode:
def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    print('hand landmarker result: {}'.format(result))

base_options=BaseOptions(model_asset_path='C:/Users/Admin/Code Projects/Hand landmark cursor control/Model/hands_landmark.task')
options = HandLandmarkerOptions(base_options=base_options, running_mode=VisionRunningMode.LIVE_STREAM, result_callback=print_result, num_hands=2)

## .task file could not be loaded in Windows 11 so far ##
with HandLandmarker.create_from_options(options) as landmarker: # Initializing landmarker
    # Use OpenCV’s VideoCapture to start capturing from the webcam.
    cap = cv2.VideoCapture(0)
    # Create a loop to read the latest frame from the camera using VideoCapture#read()
    while cap.isOpened():
        success, cap_frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        # Convert the frame received from OpenCV to a MediaPipe’s Image object.
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cap_frame)
    
        # Send live image data to perform hand landmarks detection.
        # The results are accessible via the `result_callback` provided in the `HandLandmarkerOptions` object.
        # The hand landmarker must be created with the live stream mode.
        # landmarker_result = landmarker.detect_async(mp_image, frame_timestamp_ms)

