import io
from PIL import Image
import numpy as np
from google.colab.output import eval_js
from base64 import b64decode, b64encode
from IPython.display import display, HTML

from google_colab_plugins.camera_capture import cameraCapture

import google_colab_plugins.utils

def playVideo(filename, format='mp4', width=640, height=480):
    encoded = b64encode(io.open(filename, 'r+b').read())
    embedded = HTML('''
        <video width="{1}" height="{2}" controls>
            <source src="data:video/{3};base64,{0}" type="video/{3}" />
        </video>'''.format(encoded.decode('utf-8'), width, height, format))

    display(embedded)
