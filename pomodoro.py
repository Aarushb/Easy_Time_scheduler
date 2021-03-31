#The pomodoro technique
#The lib(s) we need
import time, mainmenu, keyboard
from win10toast import ToastNotifier
toaster = ToastNotifier()
def pomodoro():
	while True:
		pomodoros=0
		#code for the main window for pomodoro, including all the buttons go here.
		#code for if start is pressed:
		print("Started!")
		while pomodoros<4:
			print("Your task, starts now!")
			toaster.show_toast("Your task, starts now!", "Get to it!")
			time.sleep(5)
		#	time.sleep(1500)
			pomodoros+=1
			print("Pomodoro",pomodoros,", check!")
			if pomodoros<4:
				print("Feel free to have a 5 minute break. You will be notified when the break is up.")
				#	time.sleep(300)
				time.sleep(3)
				print("Time's up! Get ready for the next task")

				time.sleep(5)
		print("Your first set of pomodoros is complete! Well done! Get a 15 minute break, you will be notified when its up. After that, feel free to press the start button to begin the next set.")
		#time.sleep(900)
		time.sleep(3)
		print("Breaktime up! Time to start the cycle once more!")
		time.sleep(5)
		option=input("Would you like to restart the pomodoro cycle? Press y, and hit enter to confirm if you do. Otherwise, hit any other key, followed by an enter.")
		if option=="y":
			continue
		else:
			print("Thank you for using pomodoro!")
			break
	if keyboard.is_pressed("esc"):
		print("exiting!")
		mainmenu()