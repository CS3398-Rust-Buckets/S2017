#!"C:\Users\Rusty Shackleford\AppData\Local\Programs\Python\Python36-32\python.exe"
import cgi

form = cgi.FieldStorage() 
firstname = form.getvalue('firstname')
lastname  = form.getvalue('lastname')
email = form.getvalue('your.email@here.com')
password = form.getvalue('password')
repass = form.getvalue('re-enter password')

users = open('\users.txt', 'w')

users.write(firstname)
users.write('\n')
users.write(lastname)
users.write('\n')
users.write(email)
users.write('\n')
users.write(password)
users.write('\n')
users.write(repass)
users.write('\n')

users.close()
