from win10toast import ToastNotifier
import os
import time

hostname = "google.com" #hostname with which you want to check connectivity
server = "youtube.com" #Please enter your gateway here (youtube.com is here for test only).

toaster = ToastNotifier() #toast notification object

while True:
    response = os.system("ping -n 1 " + hostname)  #ping the host once
    server_check = os.system("ping -n 1 " + server)  #ping the server once
    if response == 0:  #run if ping successful
        toaster.show_toast("Internet ON","Enjoy your time!!", duration=30)  #display notification on windows
        break
    elif server_check == 1:  #run if server is not reachable
        print("Local internet server not reachable")
    time.sleep(30)  #wait for 30 seconds
    

