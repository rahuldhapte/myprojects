from plyer import notification
import subprocess
import time

def get_battery_percentage():
	result = subprocess.run(["powershell", "WMIC PATH Win32_Battery Get EstimatedChargeRemaining"], capture_output=True, text=True)
	output = str(result)
	num = ""
	for x in output:
		if x.isdigit():
			num = num + x
	return(int(num[3:]))		
	
get_battery_percentage()


while True:
	time.sleep(10*60) #wait for 10 minutes
	if get_battery_percentage() >= 80:
			notification.notify(
			title = 'Battery Info',
			message = 'Battery charged: Please disconnect charger',
			timeout = 5)
	elif get_battery_percentage() <= 20:
			notification.notify(
			title = 'Battery Info',
			message = 'Battery low: Please connect charger',
			timeout = 5)
	else:
		print("Current battery % is", get_battery_percentage())
		
		
		
	




	
	








