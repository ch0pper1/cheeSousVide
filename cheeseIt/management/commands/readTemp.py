from channels import Group
from django.core.management import BaseCommand
from temperature import Temperature
from websocket import create_connection
import time

class Command(BaseCommand):
	def handle(self, *args, **options):
		mTemp = Temperature(0)
		wTemp = Temperature(2)
		ws = create_connection("ws://127.0.0.1:8000/ws/")
		while True:
			#self.stdout.write(temp.getTemp())
			# print(temp.getTemp())
			m = mTemp.getTemp()
			Group("mTemp").send({'text': str(m)})
			ws.send(str(m))
			# Group("wTemp").send({'temp': wTemp.getTemp()})
			time.sleep(5)
