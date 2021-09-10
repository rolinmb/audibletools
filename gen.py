import time
import subprocess
import soundfile as sf
from Pedalboard import (
    Pedalboard, Chorus, Phaser
)

def convert_wav(inmp3,outwav):
    subprocess.call(['ffmpeg','-i',inmp3,outwav])

if __name__ == '__main__':
    