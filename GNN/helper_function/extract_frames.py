import cv2
import os
import shutil

def extract_frames(video_path, output_folder, start_frame):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print(f"Error: Could not open video {video_path}")
        return start_frame

    # Initialize frame count
    frame_count = start_frame

    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()
        if not ret:
            break

        # Save the frame as an image
        frame_filename = os.path.join(output_folder, f"IMG_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    # Release the video capture object
    video_capture.release()
    print(f"Extracted frames from {video_path}, total frames so far: {frame_count}")

    return frame_count

def extract_frames_from_videos(video_paths, output_folder):
    setup(output_folder)
    frame_count = 0
    for video_path in video_paths:
        frame_count = extract_frames(video_path, output_folder, frame_count)

def setup(path, delete_all=True):
    path_exists = os.path.exists(path)
    if not path_exists:
        print(f"Creating directory: {path}")
        os.mkdir(path)
    elif delete_all and path_exists:
        print(f"Directory exists. Deleting and recreating: {path}")
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        print(f"Directory exists and delete_all is False: {path}")

# Example usage
video_paths = [
    "bad_deadlift_1.mp4",
    "bad_deadlift_2.mp4",
    "bad_deadlift_3.mp4",
    "bad_deadlift_4.mp4",
    "bad_deadlift_5.mp4",
    "bad_deadlift_6.mp4"
]
output_folder = "bad_deadlift"

extract_frames_from_videos(video_paths, output_folder)
