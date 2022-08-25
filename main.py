import sys
from pytube import YouTube
from os import startfile

def main():
    yt = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    # print(yt.title)
    stream = yt.streams.filter(file_extension='mp4').all()[0]
    stream.download()
    startfile(f"{yt.title}.mp4")
    return

if __name__ == '__main__':
    sys.exit(main())

