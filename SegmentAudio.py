from pydub import AudioSegment

name = "Recording (29)"
path = "D:\OneDrive - Wavenet International (Pvt.) Ltd\Repos\Tigo_Call_Center_Voice_Intent_Matching\Data\Dual_Channel\Service_Failure\{}.wav".format(name)
point = 50000

# 1st part
newAudio = AudioSegment.from_wav(path)
newAudio  = newAudio[:point]

name1  = name + '-1'
newAudio.export("{}.wav".format(name1), format="wav") #Exports to a wav file in the current path.from pydub import AudioSegment


# 2nd part
newAudio = AudioSegment.from_wav(path)
newAudio  = newAudio[point:]

name2  = name + '-2'
newAudio.export('{}.wav'.format(name2), format="wav") #Exports to a wav file in the current path.from pydub import AudioSegment