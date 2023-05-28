from pytube import  YouTube

url = 'the url of video'
my_video = YouTube(url)

print(my_video.title)
print(my_video.description)
print(my_video.thumbnail_url)

my_video = my_video.streams.get_highest_resolution()


'''
===========================================
 to select the resolution
===========================================
my_video = my_video.streams.first()
for stream in my_video.streams:
    print(stream)
'''

my_video.download()