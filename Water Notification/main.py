import time
from plyer import notification

while True:
 	notification.notify(
 		title = "**Please Drink Water Now!!",
 		message ="Drinking Water Helps Maintain the Balance of Body Fluids. So please drink at least 4 liters of water everyday!",
 		app_icon = "D:\Python\Projects\Water Notification\water.ico",
 		timeout= 10
	)
	# setting reminder for every hour
	time.sleep(60*60)