import time #for importing time
from datetime import datetime as dt

hosts_temp=r"C:\website_blocker\hosts" #temp file name
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"#original file location 
redirect="127.0.0.1" #redirect address for blocking the website
website_list=["www.facebook.com","facebook.com","netflix.com","www.netflix.com"] #list of the website to block

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16): #time span during which we're blocking wesbite
        print("Working hours...")
        with open(hosts_path,'r+') as file: #with is method for opening and automatic closing of file
            content=file.read()
            for website in website_list:
                if website in content:
                    pass #incase the file is already present in the hosts file
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file: #r+ is used for read and write operation
            content=file.readlines() #it points the curser to the last line
            file.seek(0)#it point the curser at the begining
            for line in content:
                if not any(website in line for website in website_list): #If any of the above is True you get the expression evaluated to True. In this case none of them is True, so you get False.
                    file.write(line)
            file.truncate()#to delete the files for fun hours
        print("Fun hours...")
    time.sleep(5) #its cheching time in every five second for the while condition
