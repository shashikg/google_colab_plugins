import numpy as np
import subprocess

def download_test_video():
  subprocess.check_output(["wget", "-O", "bunny_video.mp4", "https://github.com/shashikg/google_colab_plugins/raw/master/examples/data/bunny_video.mp4"])
  print("Download Complete!")
