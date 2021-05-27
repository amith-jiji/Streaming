from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from feed.camera import VideoCamera


# Create your views here.

def indexView(request):
    return render(request, 'home2.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'


def video_feed1(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')
