#!"C:\Users\Rusty Shackleford\AppData\Local\Programs\Python\Python36-32\python.exe"
import cgi

form = cgi.FieldStorage() 
name = form.getvalue("Event Name")
time  = form.getvalue("Start Time")
group = form.getvalue("Group Name")
descrip = form.getvalue("Description...")
location = form.getvalue("Event Location")

events = open('\events.txt', 'w')

events.write(name)
events.write('\n')
events.write(time)
events.write('\n')
events.write(group)
events.write('\n')
events.write(descrip)
events.write('\n')
events.write(location)
events.write('\n')

users.close()
