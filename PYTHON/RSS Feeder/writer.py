import datetime
pubDate = datetime.datetime.now()
t = datetime.datetime.now()
x = t.strftime('%Y-%m-%d %H:%M:%S.%f')
f=open("jobstatus.txt", "a+")
for i in range(1):
     f.write("\n" +x)
