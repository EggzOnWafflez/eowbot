from src.lib.twitch import *


def uptime(**kwargs):
    uptime = get_stream_uptime()
    if get_stream_status():
        return "The current !uptime is " + str(uptime)
    else:
        return "The streamer is offline!"
