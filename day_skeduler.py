#Here is where the code for the generic day schoduler goes, as mentioned in the spec docs. Feel free to remove this comment once you begin coding and add your own along the way.
#install two libraries 
# first one pyttsx3 in cmd type"pip install pyttsx3"
# second one schedule in cmd type" pip install schedule"

# Currently code run for 8 am to 5 pm duration of 1 hour
# Currently code run for 8 am to 5 pm duration of 2 hours
# Currently code run for 9 am to 6 pm duration of 1 hour
# Currently code run for 9 am to 6 pm duration of 2 hours


# import libraries pyttsx3, schedule, and time
import pyttsx3
import schedule
import time




#--------------------------------------------------------------------------------------------------
print("WELCOME TO DAY SCHEDULER")

time_selection=int(input("Select the start time and end time, if 8 am to 5 pm choose '1' and 9 am  to 6 pm choose '2': "))
time_duration=int(input("Enter duration of time, if duration is one hour choose '1' and if duration is two hours choose '2': "))

#----------------------------------------------------------------------------------------------------------

if time_selection ==1: 
    if time_duration==1:
        task1=input("Enter the first task from 8am to 9am: ")
        task2=input("Enter the second task from 9am to 10am: ")
        task3=input("Enter the third task from 10am to 11am: ")
        task4=input("Enter the fourth task from 11am to 12pm: ")
        task5=input("Enter the fifth task from 12pm to 1pm: ")
        print("1pm to 2pm is lunch time")
        task6=input("Enter the sixth task from 2pm to 3pm: ")
        task7=input("Enter the seventh task from 3pm to 4pm: ")
        task8=input("Enter the eightth task from 4pm to 5pm: ")

        def job(n):
            engine = pyttsx3.init()
            engine = pyttsx3.init()
            engine.say("it is time for " + n)
            engine.say("it is time for " + n)
            engine.say("it is time for " + n)
            engine.runAndWait()
            print("it is time for " + n)
            return schedule.CancelJob
            
        
        schedule.every().day.at("8:00").do(job,n=task1)
        schedule.every().day.at("9:00").do(job,n=task2)
        schedule.every().day.at("10:00").do(job,n=task3)
        schedule.every().day.at("11:00").do(job,n=task4)
        schedule.every().day.at("12:00").do(job,n=task5)
        schedule.every().day.at("13:00").do(job,n="Lunch")
        schedule.every().day.at("14:00").do(job,n=task6)
        schedule.every().day.at("15:00").do(job,n=task7)
        schedule.every().day.at("16:00").do(job,n=task8)
        schedule.every().day.at("17:00").do(job,n="Break/Rest/Play")

        while 1:
            n = schedule.idle_seconds()
            if n is None:
                # no more jobs
                break
            elif n > 0:
                # sleep exactly the right amount of time
                time.sleep(n)
            schedule.run_pending()



    elif time_duration==2:
        task1=input("Enter the first task from 8am to 10am: ")
        task2=input("Enter the second task from 10am to 12pm: ")
        task3=input("Enter the third task from 12pm to 3pm: ")
        print("1pm to 2pm will be lunch break")
        task4=input("Enter the fourth task from 3pm to 5pm: ")


        def job(n):
            engine = pyttsx3.init()
            engine = pyttsx3.init()
            engine.say("it is time for " + n)
            engine.say("it is time for " + n)
            engine.say("it is time for " + n)
            engine.runAndWait()
            print("it is time for " + n)
            return schedule.CancelJob
            
        
        schedule.every().day.at("8:00").do(job,n=task1)
        schedule.every().day.at("10:00").do(job,n=task2)
        schedule.every().day.at("12:00").do(job,n=task3)
        schedule.every().day.at("13:00").do(job,n="Lunch")
        schedule.every().day.at("14:00").do(job,n=task3)
        schedule.every().day.at("15:00").do(job,n=task4)
        schedule.every().day.at("17:00").do(job,n="Break/Rest/Play")
        

        while 1:
            n = schedule.idle_seconds()
            if n is None:
                # no more jobs
                break
            elif n > 0:
                # sleep exactly the right amount of time
                time.sleep(n)
            schedule.run_pending()


elif time_selection ==2: 
    if time_duration==1:
        
        task1=input("Enter the first task from 9am to 10am: ")
        task2=input("Enter the second task from 10am to 11am: ")
        task3=input("Enter the third task from 11am to 12pm: ")
        task4=input("Enter the fourth task from 12pm to 1pm: ")
        print("1pm to 2pm is lunch time")
        task5=input("Enter the fifth task from 2pm to 3pm: ")
        task6=input("Enter the sixth task from 3pm to 4pm: ")
        task7=input("Enter the seventh task from 4pm to 5pm: ")
        task8=input("Enter the eightth task from 5pm to 6pm: ")

        def job(n):
            engine = pyttsx3.init()
            engine = pyttsx3.init()
            engine.say("it is time for " + n)
            engine.say("it is time for " + n)
            engine.say("it is time for " + n)
            engine.runAndWait()
            print("it is time for " + n)
            return schedule.CancelJob
            
        
        
        schedule.every().day.at("9:00").do(job,n=task1)
        schedule.every().day.at("10:00").do(job,n=task2)
        schedule.every().day.at("11:00").do(job,n=task3)
        schedule.every().day.at("12:00").do(job,n=task4)
        schedule.every().day.at("13:00").do(job,n="Lunch")
        schedule.every().day.at("14:00").do(job,n=task5)
        schedule.every().day.at("15:00").do(job,n=task6)
        schedule.every().day.at("16:00").do(job,n=task7)
        schedule.every().day.at("17:00").do(job,n=task8)
        schedule.every().day.at("18:00").do(job,n="Break/Rest/Play")

        while 1:
            n = schedule.idle_seconds()
            if n is None:
                # no more jobs
                break
            elif n > 0:
                # sleep exactly the right amount of time
                time.sleep(n)
            schedule.run_pending()


    elif time_duration==2:
        task1=input("Enter the first task from 9am to 11am: ")
        task2=input("Enter the second task from 11am to 1pm: ")
        print("1pm to 2pm will be lunch break")
        task3=input("Enter the third task from 2pm to 4pm: ")
        task4=input("Enter the fourth task from 4pm to 6pm: ")

        def job(n):
            engine = pyttsx3.init()
            engine = pyttsx3.init()
            engine.say("it is time for " + n)
            engine.say("it is time for " + n)
            engine.say("it is time for " + n)
            engine.runAndWait()
            print("it is time for " + n)
            return schedule.CancelJob
            
        
        schedule.every().day.at("9:00").do(job,n=task1)
        schedule.every().day.at("11:00").do(job,n=task2)
        schedule.every().day.at("13:00").do(job,n="Lunch")
        schedule.every().day.at("14:00").do(job,n=task3)
        schedule.every().day.at("16:00").do(job,n=task4)
        schedule.every().day.at("18:00").do(job,n="Break/Rest/Play")
        

        while 1:
            n = schedule.idle_seconds()
            if n is None:
                # no more jobs
                break
            elif n > 0:
                # sleep exactly the right amount of time
                time.sleep(n)
            schedule.run_pending()


else:
    print("Invalid input")


