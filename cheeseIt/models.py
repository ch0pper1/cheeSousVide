from django.db import models

# Create your models here.
class Cheese(models.Model):
	name = models.CharField(max_length=64, verbose_name='Name', default='Cheeeeeeeese')
	startTemp = models.IntegerField(default=86)
	holdTime = models.IntegerField()
	targetTemp = models.IntegerField()
	onTemp = models.BooleanField(default=False)
	mTemp = models.IntegerField(default=1)
	wTemp = models.IntegerField(default=1)

    #def heat_milk_and_hold(self):
        # Step one
