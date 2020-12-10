from aiohttp import web
import socketio
import vlc
import time

instance = vlc.Instance()

playaudio = instance.media_player_new()


sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

async def index(request):
	return web.Response(text="Hello Wold", content_type="text/html")

@sio.on('play')
def play(sid, message):
	print("Socket ID: ", sid)
	# await sio.emit('reply', data, namespace='/chat')
	print (message)
	media = instance.media_new('test.WAV')
	playaudio.set_media(media)
	playaudio.play()

@sio.on('stop')
def stop(sid, message):
	print("Socket ID: ", sid)
	# await sio.emit('reply', data, namespace='/chat')
	print (message)
	playaudio.stop()


@sio.on('pause')
def pause(sid, message):
	print("Socket ID: ", sid)
	# await sio.emit('reply', data, namespace='/chat')
	print (message)
	playaudio.pause()


app.router.add_get('/', index)

if __name__ == '__main__':
	web.run_app(app)