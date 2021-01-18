import time

#def gen():
#	
#	with open("file.txt") as file:
#		
#		file=file.read()

#	file="""CBSE Exam 2021: When Will Board Release Class X, XII Datesheet? Is There Any Change in Marking Scheme? Official Answers
#CBSE Board Exam 2021: Bharadwaj also talked about the datesheet or schedule for Class X, XII. He said that the board and stakeholders are still working and there is no clarity on the same as of now.
#By India.com Education Desk | Updated:Tue, December 15, 2020 7:56am




#Subscribe to Notifications
#  

#CBSE Board Exams 2021: Sanyam Bhardwaj, the Controller of Examinations, Central Board of Secondary Education (CBSE) held a meeting with select Principals of CBSE affiliated schools and deliberated upon the upcoming CBSE Board Exams 2021. Bharadwaj, who had confirmed that the Class X, XII board examinations will be held, asserted that practicals would be conducted only after the resumtion of normal classes or the schools reopen. Also Read - CBSE Exam 2021: When Will Board Release Class X, XII Datesheet? Is There Any Change in Marking Scheme? Official Answers

#According to the reports of Times Now, Bharadwaj also talked about the datesheet or schedule for Class X, XII. He said that the board and stakeholders are still working and there is no clarity on the same as of now. He, however, mentioned that students can expect their exam schedule in due course of time. The board official didn't rule out the possibility of more gap days between the exams. CBSE is expected to grant 'sufficient time for preparation' to Class, XII students. Also Read - Delhi HC Slams CBSE for 'Anti-student attitude', Treating Students as Enemies by Dragging them to SC


#Will Syllabus be Reduced? Also Read - CBSE Board Exams 2021: Nishank to Interact With Teachers on Dec 17 | Big Announcement Likely For Class X, XII Students

#Furthermore, he said that the board is not planning to reduce the syllabus further. Earlier, the board has reduced the 30 per cent of the syllabus. On examination pattern, he stated that typology for the question papers would remain the same as the CBSE sample papers, which students can acess through the official website- cbseacademic.nic.in


#What about the marking scheme?

#There will be no change in marking scheme. The board would follow the previous 80+ 20 format wherein 80 is for theory paper and 20 for the practicals or internal evaluation.


#Pokhriyal to make big announcement on Dec 17

#Education Minister Ramesh Pokhriyal 'Nishank' will interact with teachers about the upcoming CBSE board exams 2021. The Minister would go live at 4 pm. Teachers can raise their concerns by using the hashtag #EducationMinisterGoesLive. "Dear Teachers, I will be going #live on Dec 17 at 4 PM to talk to you all about the upcoming board exams. Please share your queries/concerns with me using #EducationMinisterGoesLive. I will be happy to address them all," Nishank tweeted.

#Published:Tue, December 15, 2020 7:56am | Updated:Tue, December 15, 2020 7:56am

#Tags
#CBSECBSE Board Exam 2021

#Exams and Results News
#Schools, Colleges in Assam to Reopen From This Date, Academic Restrictions to be Lifted | Check Details
#Schools, Colleges to Reopen in Assam From New Year; Govt to Issue SOPs Soon
#DU FMS Admission 2021: Application Process Begins for MBA Admissions at fms.edu, Details Here
#ICAI CA January/February 2021 Complete Schedule Released at icai.org, Check Details Here
#IGNOU December TEE 2020 Application Dates Extended At ignou.ac.in, Register by 31st December
#Latest News
#Tatas, Interups, AI Employees Among Multiple Bidders For Air India
#7,000 People Booked For Violence at Karnataka's iPhone Manufacturing Plant
#Jammu and Srinagar to Get Light Metro Rail Networks Soon
#When Will Coronavirus End? When Will COVID Vaccine be Available in India? Union Minister Makes Big Statement
#'Democracy Prevailed': Biden Clears 270-mark on Electoral Votes to Confirm His Win as US President
#Explore more
#Home
#News
#India
#Entertainment
#Photos
#Sports
#Viral
#Lifestyle
#Business
#Tech
#Education
#Festivals
#Food
#World
#Travel
#Videos
#About UsDisclaimerPrivacy PolicyContact Us

#Copyright © 2020 India WebPortal Private Limited. All Rights Reserved.

#"""
#	
#	file=file.lower()
#	
#		
#	time.sleep(7)
#	
#	while True:
#		
#		find_word=(yield).lower()
#		
#		if find_word in file:
#			
#			place=file.find(find_word)
#			
#			location_start=place-20
#			
#			location_end=place+20
#			
#		#	print(location_start)
#			
#			if location_start<0:
#				
#				location_start=0
#				
#			#	print(location_start)
#				
#		
#			print(f"'{find_word}' was in the file at '{file[location_start:location_end]}'")
#			
#		else:
#			
#			print(f"{find_word} was not in file\n")
#			
#		
#			
#			
#a=gen()
#input("Press enter")
#next(a)
#input("Press enter")

#a.send("marking")
#input("Press enter")
#a.send("life")
#input("Press enter")
#a.send("lifestyle")



def name_in_file():
	
	file=["harry","ankit"]#Here I am using list instead of file
	
	time.sleep(2)
	
	
	while True:
		
		text=(yield)
		
		if text in file:
			
			yield f"{text} was in file"
		
		else:
			
			yield f"{text} was not in list"
			
check=name_in_file()
	


print("Enter Your name\n")
				
name=input()
	
next(check)
print(check.send(name))


print("Enter Your name\n")
				
name=input()
	
print(check.send(name))
				

print("Enter Your name\n")
				
name=input()
	
print(check.send(name))
				
	
				
	
	