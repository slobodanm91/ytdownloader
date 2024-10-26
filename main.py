from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import yt_dlp

folderName = ''
def choose_folder():
    global folderName
    try:
        folderName = filedialog.askdirectory()
        labelPath.config(text=f'Video will be saved to: {folderName}')
    except ValueError:
        labelPath.config(text='Invalid folder selected')

def download_yt_video(videoUrl):
    urlString = videoUrl.get().strip()
    if len(folderName) > 0:
        try:
            ydl_opts = {'outtmpl': f"{folderName}/%(title)s.%(ext)s"}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([urlString])
            labelInvalidUrl.config(text='Video downloaded successfully.')
        except Exception as e:
            labelInvalidUrl.config(text=f'Error: {str(e)}')
    else:
        labelPath.config(text='No folder selected for video saving!')
root = Tk()
root.title("YouTube Downloader")

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

labelTitle = ttk.Label(mainframe, text='YOUTUBE VIDEO DOWNLOADER')
labelTitle.configure(font='Calibri 17 bold', foreground='green')
labelTitle.grid()

labelUrl = ttk.Label(mainframe, text='Enter the video URL below!')
labelUrl.grid()
videoUrl = StringVar()
entryUrl = ttk.Entry(mainframe, width=70, textvariable=videoUrl)
entryUrl.grid()

buttonPath = ttk.Button(mainframe, width=15, text='Choose', command=choose_folder)
buttonPath.grid()

labelPath = ttk.Label(mainframe, text='Choose a save location for the video')
labelPath.grid()

buttonDownloadVideo = ttk.Button(mainframe, text='Download video', command=lambda: download_yt_video(videoUrl))
buttonDownloadVideo.grid()

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

labelInvalidUrl = ttk.Label(mainframe, text=' ')
labelInvalidUrl.grid()

root.mainloop()