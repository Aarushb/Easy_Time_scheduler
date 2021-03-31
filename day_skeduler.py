import pyttsx3, schedule,time, mainmenu, sys,keyboard #these are all the complete libs we need for this  program
from win10toast import ToastNotifier#we need this for the notifications for tasks
#The function we will need down the road in order to output the tasks in sapi.
def job(n):
	engine = pyttsx3.init()
	engine.say("it is time for " + n)
	engine.runAndWait()
	print("it is time for " + n)
	toaster = ToastNotifier()
	toaster.show_toast("Its time for "+n,"Get to it!",
	duration=10)
	return schedule.CancelJob
#function for the main interface of our day schoduler
tasklist=[]

def day_scheduler():
	#Presenting a menu to the user, this will be ported to gui soon if everything goes as per plan.
	count=1#we need this later on for the menus in the delete menu
	#Validating user's input.
	while True:
		while True:
			try:
				print("Please choose an option from the following menu. \n 1. Add a task. \n 2. View current list of tasks. \n 3. delete a task. \n 4. Start my day.\n 5. Return to the main menu. \n 6. Exit.")
				option=int(input("Please choose an option."))
			except:
				print("Invalid input! Please enter a number.")
				continue
			if option in range(1,7):
				break
			else:
				print("Please pick a valid number from the given menu")
				continue

		#Actually coding these options in now.
		if option==2:
			if len(tasklist)==0:
				print("There are 0 tasks skeduled right now.")
				continue
			else:
				print("There are currently ",len(tasklist),"tasks skeduled which are as follows.",tasklist)
				continue
		elif option==1:
			taskname=input("Enter a name for your new task.")
			while True:
				tasktime=input("Enter the time at which you want to start this task. Your input should be in the form of hh:min. For example, 08:30 for 8 30 in the morning.")
				if int(tasktime[0:tasktime.index(":")]) in range(0,24) and int(tasktime[tasktime.index(":")+1:]) in range(0,61):
					break
				else:
					print("Invalid input of time spicified. Please try again.")
					continue
			tasklist.append(taskname+ ",at"+ tasktime)
			schedule.every().day.at(tasktime).do(job,n=taskname)
			print("All done! You will be notified when the task has to be done.")
			continue
		elif option==4:
			print("Starting your day, now!")
			task_notifier()
		elif option==6:
			print("Exiting.")
			time.sleep(1)
			sys.exit()
		elif option==3:
			print("Choose the task to be deleted from the following menu.")
			while True:
				for i in tasklist:
					print(count,i)
					count+=1
				try:
					taskdel=int(input("Choose a task."))
				except:
					print("Please enter a number.")
					continue
				if taskdel not in range(1,len(tasklist)+1):
					print("Invalid option.  Please try again.")
					continue
				tasktodel=tasklist[taskdel-1]
				tasklist.remove(tasktodel)
				tasktodel=tasktodel[0:tasktodel.index(",")]
				schedule.cancel_job(tasktodel)
				print("Deleted successfully!")
				break
		elif option==5:
			mainmenu.mainmenu()
def task_notifier():
	while True:
		schedule.run_pending()
		if keyboard.is_pressed("esc"):
			day_scheduler()
