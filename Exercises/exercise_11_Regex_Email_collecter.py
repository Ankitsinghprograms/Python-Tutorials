import requests

import re



#website=requests.get("https://mail.google.com/mail/mu/mp/933/#mn") #No emails available at this website

#string=website.text

string='''
ankitsingh300307@gmail.com
sangitasingh@gmail.com
kumarsingh9334@gmail.com
'''



email_patt=re.compile("\S+@gmail.com")

emails=email_patt.findall(string)



try:
	with open("emails.txt","x") as file:
		
		for each in emails:
			
			file.write(f"{each}\n")
		
		
except:
		
	print("File already exists")
		
	with open("emails.txt","a") as file:
		
		for each in emails:
			
			file.write(f"{each}\n")
			
			
finally:
		
		print("Data Saved, Done!")
		
