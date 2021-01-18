#from newsapi import NewsApiClient as source
import json
import requests as r 

from gtts import gTTS 

import os 

import webbrowser



news_raw=r.get("http://newsapi.org/v2/everything?q=bitcoin&from=2020-12-06&sortBy=publishedAt&apiKey=054c1a4e5b144dc69776a31f691e5bb2")

start=47


new_raw_cut=news_raw.text[47:]

details=[]

each=""
prev=""

for i in new_raw_cut:
	if prev=="}" and i==",":
		details.append(each)
		each=""
	else:
		each+=i
	prev=i
	
	
news=[]
t=0
for i in range(len(details)):
	if t==1:
		news.append("{"+details[i])
		t=0
	else:
		t+=1
		

no_of_news=1

full_news=""


for each in news:
	
	each_news=json.loads(each)
	
#	print(each_news["urlToImage"],end="\n")

	print("News\n")
	
	print(f"News no. {no_of_news}\n")

	print("In short\n",each_news["title"],end="\n\n")
	
	print("In detail\n",each_news["description"],end="\n\n")
	
#	print("Full story\n",each_news["content"],end="\n\n")
	
	print("\n\n\n")

	
	full_news=full_news+f",.,!!!!!!!!!!!!!!!!!!!!!  News no. {no_of_news} ,,.,!!!!!!!!!!!!!!!!!!!!! {each_news['title']} ,.,,!!!!!!!!!!!!!!!!!!!!! In detail ,.,!!!!!!!!!!!!!!!!!!!!! {each_news['description']} ,.,!!!!!!!!!!!!!!!!!!!!!,.,!!!!!!!!!!!!!!!!!!!!!" 
	
	no_of_news+=1
	
	


print("Changing News to Voice. This will take time something around 7-8min\n")

news_voice=gTTS(full_news) 
news_voice.save("news.mp3")

print("Playing Audio of News\n")

current_dir=os.getcwd()


file_path='content://com.estrongs.files'+current_dir+"/news.mp3"

webbrowser.open(file_path)#pllaying Audio