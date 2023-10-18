import tkinter as tk
import requests

def get_lyrics():

    artist = artist_entry.get()
    song = song_entry.get()
    api_url = f"https://api.vagalume.com.br/search.php?art={artist}&mus={song}"
    response = requests.get(api_url)

    if response.status_code == 200:
      data = response.json()
      lyrics = data['mus'] [0]['text']
      display_lyrics(lyrics)
    
    else:
        result_label.config(text='A letra não existe')


def display_lyrics(lyrics):
    result_text.delete(1.0, 'end')
    result_text.insert(tk.END, lyrics)


app = tk.Tk()
app.title('Busque sua música favorita')

artist_label = tk.Label(app, text = 'Digite o artista')
artist_label.pack()

artist_entry = tk.Entry()
artist_entry.pack()

song_label = tk.Label(app, text='Digite a música')
song_label.pack()

song_entry = tk.Entry()
song_entry.pack()

btn = tk.Button(app, text= 'Buscar', command=get_lyrics)
btn.pack()

result_text = tk.Text(app, height=40, width=60)
result_text.pack()

result_label = tk.Label()
result_text.pack()

app.mainloop()
