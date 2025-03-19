from pytube import YouTube

def download_youtube_video(url, output_path="."):
    """
    Scarica un video di YouTube fino a 4K.

    Args:
        url (str): L'URL del video di YouTube.
        output_path (str): Il percorso in cui salvare il video scaricato.
    """
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.filter(res="2160p").first() # cerca il video in 4k
        if highest_res_stream is None: # se non trova il video in 4k cerca la risoluzione piu' alta
            highest_res_stream = streams.order_by('resolution').desc().first()
        highest_res_stream.download(output_path=output_path)
        print(f"Video scaricato con successo in: {output_path}")
    except Exception as e:
        print(f"Si è verificato un errore durante il download del video: {e}")

if __name__ == "__main__":
    video_url = input("Inserisci l'URL del video di YouTube: ")
    output_directory = input("Inserisci il percorso in cui salvare il video (o premi Invio per la cartella corrente): ")
    if not output_directory:
        output_directory = "."
    download_youtube_video(video_url, output_directory)
