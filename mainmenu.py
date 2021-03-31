import pomodoro
import day_skeduler
def mainmenu():
	while True:
		try:
			option=int(input("Please select an option. \n 1. Generic day scheduler. 	\n 2. Pomodoro."))
			break
		except:
			print("Invalid input, please choose an option from the choices provided above.")
			continue
	if option==1:
		day_skeduler.day_scheduler()
	elif option==2:
			pomodoro.pomodoro()
