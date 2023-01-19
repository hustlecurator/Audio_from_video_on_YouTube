from pytube import YouTube


def download_audio():
    video_url = input('Введите URL видео: ')
    yt = YouTube(video_url)
    name = f'{yt.streams[0].title}.mp3'
    yt.streams.filter(only_audio=True).first().download(filename=name)


download_audio()