from pytube import YouTube
url = input('Digite a url do Youtube: ')

video = YouTube(url)
#baixa vídeos
video.streams.get_lowest_resolution().download(
    output_path = r"C:\Users\Kurumí\Desktop\SLA LSLSLSLSLSSLLSLSLSLSLS",
    filename = video.title
)
#baixa áudios
video.streams.filter(only_audio=True).first().download(
    output_path = r"C:\Users\Kurumí\Desktop\SLA LSLSLSLSLSSLLSLSLSLSLS" ,
    filename = video.title + ".mp3"
)





