from pytube import YouTube
link=input("enter link")
print("downloading..")
YouTube(link).streams.first().download()
print("downloaded")