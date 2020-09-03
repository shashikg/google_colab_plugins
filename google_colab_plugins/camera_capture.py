import io
from PIL import Image
import numpy as np
from google.colab.output import eval_js
from base64 import b64decode, b64encode
from IPython.display import display, HTML

class cameraCapture:
    def __init__(self, quality=0.8):
        self.quality = quality
        self.startCamera = '''
            var div = document.createElement('div');
            var video = document.createElement('video');
            video.style.display = 'none';
            document.body.appendChild(div);
            div.appendChild(video);

            async function playVideo(){
                var stream = await navigator.mediaDevices.getUserMedia({video: true});
                video.srcObject = stream;
                await video.play();
                return;
            }

            playVideo();
            '''

        self.createCanvas = '''
            var canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;

            function getImage(quality){
                canvas.getContext('2d').drawImage(video, 0, 0);
                return canvas.toDataURL('image/jpeg', quality);
            }
            '''

        self.stopCamera = '''
            video.srcObject.getVideoTracks()[0].stop();
            div.remove();
            '''

        self.open()

    def open(self):
        eval_js(self.startCamera)
        eval_js(self.createCanvas)

    def release(self):
        eval_js(self.stopCamera)

    def read(self):
        data = eval_js('getImage({})'.format(self.quality))
        img = self.byte2img(data)
        return img

    def byte2img(self, data):
        binary = b64decode(data.split(',')[1])
        f = io.BytesIO(binary)
        img = np.asarray(Image.open(f).convert('RGB'))
        img = img[:, :, [2, 1, 0]]
        return img

    def img2byte(self, img):
        img = img[:, :, [2, 1, 0]]
        img = Image.fromarray(img)
        buffer = io.BytesIO()
        img.save(buffer, 'jpeg')
        buffer.seek(0)
        data = b64encode(buffer.read()).decode('utf-8')
        return data
