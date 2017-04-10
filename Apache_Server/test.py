#!"C:\Users\Rusty Shackleford\AppData\Local\Programs\Python\Python36-32\python.exe"
import cgi

form = cgi.FieldStorage() 
firstname = form.getvalue('firstname')
lastname  = form.getvalue('lastname')
print("Content-Type: text/html\r\n\r\n")
print("<head>")
print("</head>")
print("<body>")
print("test")
print(firstname, lastname)
print("</body>")
