from pydub import AudioSegment
import os


for r, d, f in os.walk(path):
    for folder in d:
        folders.append(os.path.join(folder))


for i in folders:
    statinfo = os.stat(path + i + "/LineL Track.wav")
    if statinfo.st_size > 1000000:
        audio_l = AudioSegment.from_file(path + i + "/LineL Track.wav", format="wav")
        audio_r = AudioSegment.from_file(path + i + "/LineR Track.wav", format="wav")
        stereo_sound = AudioSegment.from_mono_audiosegments(audio_l, audio_r)
        file_handle = stereo_sound.export("/media/usb/mp3/" + i + ".mp3", format="mp3")
        
