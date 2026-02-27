# ✋ Real-Time Hand Tracking using MediaPipe & OpenCV

## Overview
This project implements real-time hand tracking using a webcam feed. It leverages Google MediaPipe's Hand solution to detect and track 21 hand landmarks, and OpenCV for video capture and visualization.

The system identifies hand keypoints, converts normalized coordinates to pixel positions, and draws landmarks and connections directly on the video stream.

## Features
- Real-time webcam hand detection
- 21 hand landmark tracking
- Landmark coordinate extraction (pixel space)
- Visualization of hand skeleton and connections
- Highlighting specific landmarks (e.g., wrist point)

## How It Works
1. Capture video frames using OpenCV.
2. Convert frames from BGR to RGB format.
3. Process frames using MediaPipe Hands.
4. Extract landmark positions.
5. Convert normalized coordinates to pixel coordinates.
6. Draw landmarks and connections on the frame.

## Technologies Used
- Python
- OpenCV
- MediaPipe

## Applications
- Gesture recognition systems
- Human-computer interaction
- Virtual mouse/keyboard control
- Sign language recognition (foundation step)
- AR/VR interaction systems

## How to Run
1. Install dependencies:
