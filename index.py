import vlc
import time
import tkinter as tkr
player = tkr.Tk()

instance = vlc.Instance()

playaudio = instance.media_player_new()



# print("this process has the pid", os.getpid())
# pid = os.getpid()


player.title("Audio Player")
player.geometry("205x340")

# Get Song
file = "test.WAV"

def Play():
	media = instance.media_new(file)
	playaudio.set_media(media)
	playaudio.play()
def ExitPlayer():
	playaudio.stop()
def Pause():
	playaudio.pause()
# Register Button
button1 = tkr.Button(player, width=5, height=3, text="Play", command=Play)
button1.pack(fill = "x")
button2 = tkr.Button(player, width=5, height = 3, text="Stop", command=ExitPlayer)
button2.pack(fill= "x")
button3 = tkr.Button(player, width=5, height = 3, text="Pause", command=Pause)
button3.pack(fill= "x")

# Song Name
label1 = tkr.LabelFrame(player, text="Name of File")
label1.pack(fill="both", expand="yes")
contents1 = tkr.Label(label1, text = file)
contents1.pack()

# Active
player.mainloop()