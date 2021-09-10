import time
import subprocess
import soundfile as sf
from Pedalboard import *

def convert_wav(inmp3,outwav):
    subprocess.call(['ffmpeg','-i',inmp3,outwav])

if __name__ == '__main__':
    start = time.time()
    wav,sr = sf.read('final_boass.wav')
    fx = Pedalboard([LadderFilter(mode=LadderFilter.Mode.HPF12,cutoff_hz=900)])
    print('Program Execution Time: '+str(reound(time.time()-start,2))+' seconds.')