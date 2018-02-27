from channels import Group
from channels.sessions import channel_session
from .models import Cheese


def ws_connect(message):
	Group('mTemp').add(message.reply_channel)
    #Group('wTemp').add(message.reply_channel)

	message.reply_channel.send({
		'accept': True
	})

def ws_message(message):
	mTemp = message
	"""
	self.send({
		"type": "websocket.send",
		"text": event["text"],
	})
	"""

def ws_disconnect(message):
    Group('mTemp').discard(message.reply_channel)
    #Group('wTemp').discard(message.reply_channel)
