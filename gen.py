import soundfile as sf
import subprocess
import time
from pedalboard import *

def to_wav(mp3,wavOut):
	print('Converting '+mp3+' to '+wavOut)
	subprocess.call(['ffmpeg','-i',mp3,wavOut],shell=True)

def getBoard(rate):
	pb = Pedalboard([
		Chorus(rate_hz=12.5,depth=0.15,mix=0.4),
		Phaser(rate_hz=0.75,depth=0.1,mix=0.175)
	],sample_rate=rate)
	return pb
	
def writeFx(fx,wav,osr,dest):
	result = fx(wav)
	print('Output Sample Rate: '+str(osr)+' Hz')
	print('\t-> Writing effected audio to \''+dest+'\'')
	with sf.SoundFile(dest,'w',samplerate=osr,channels=len(result.shape)) as f:
		f.write(result)
	
if __name__ == '__main__':
	start = time.time()
	inName = 'sample.wav'
	outName = 'out.wav'
	#to_wav('boass.mp3',inName)
	wav,inRate  = sf.read(inName) 
	print('Input Sample Rate:'+str(inRate)+' Hz')
	outRate = 44100 #44100 Hz is Standard
	board =getBoard(outRate)
	outName = 'out.wav'
	writeFx(board,wav,outRate,outName)
	print('Total Execution Time: '+str(round(time.time()-start,2))+' seconds.')