# Advance Robotic Fabrication - 2024

This repo has examples of the python programs worked in class.

## Setup

> [!Note]
> This needs to be done only once.

### Create a Virtual Environment (Optional)

It is suggeted to create a virtual environment. To create a virtual environment in VS Code, follow [these](https://code.visualstudio.com/docs/python/environments#_using-the-create-environment-command) instructions.

Alternatively, you can run this terminal command:

```bash
python -m venv .venv
```

### Install OpenCV

**CameraControl** and **CameraServer** examples require `OpenCV` library. You can install `OpenCV` using this terminal command:

```bash
pip install opencv-python
```

## Example Programs

### Threading

| Files                |                                                             |
| -------------------- | ----------------------------------------------------------- |
| _SimpleThreading.py_ | Running two processes in parallel on different threads.     |
| _ThreadingEvent.py_  | Using `threading.Event` to communicate between the threads. |

### TCP Communication

| Files                     |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| _SimpleTCPServer.py_      | A simple TCP server that listens for a client to connect and echod back the messages.     |
| _SimpleTCPClient.py_      | A simple TCP client that connects to a server, sends messages, and receives the responds. |
| _MultiThreadTCPServer.py_ | A TCP server that accepts multiple clients and uses threads receive messages from them    |

### Camera Control

| Files             |                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _StreamCamera.py_ | Capture and display camera feed using `OpenCV`.                                                                                                           |
| _Snapshot.py_     | Stream camera and saves the image to a `.png` file on demand using `OpenCV`                                                                               |
| _CameraServer.py_ | Streams the camera using `OpenCV` and runs a TCP server in the background. Saves the image to a `.png` file when the server receives a _capture_ message. |
