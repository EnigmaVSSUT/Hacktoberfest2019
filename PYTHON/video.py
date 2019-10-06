from pytube import YouTube


link = "https://www.youtube.com/watch?v=OCBeBlpVZBY"
yt = YouTube(link)

for i in yt.streams.filter(progressive=True, file_extension='mp4').all():
    #  print(vars(i))
    # for j in vars(i):
    j = i.__dict__
    if(j.get('fmt_profile').get('resolution') == '720p'):
        stream = i
        break

try:
    stream.download('E:/')
except:
    print('Couldn\'t download video. Please try again')
