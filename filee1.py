html=open("Files/coronometer.html","r")
#print(html.read())
#html=open("Files/coronometer.html","rt")
#print(html.read())
#html=open("Files/coronometer.html","rb")
#print(html.read())
n=0
while True:
	html_readline=html.readline()
	print(html_readline)
	n=n+1
	
	if html_readline=="":
		#n=n+1
		print(n)
		break
g=0
while True:
	html_read=html.read()
	print(html_read)
	g=g+1
	if html_read=="": #blank space means NOTHING
		print(g)
		break
	
n=0
while True:
	html_readline=html.readline()
	print(html_readline)
	n=n+1
	
	if html_readline=="":#blank space means NOTHING
		#n=n+1
		print(n)
		break
#	n=n+1
#	print(n)