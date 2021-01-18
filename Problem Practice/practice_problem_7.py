import time

l=["hello world python","is python interpereted or complied","python if elif else","python input","python join split function","module in python","python loops","python for loop","while loop and its uses in python","break and continue in python","python datatypes","dictionary in python","tuple in python","list in python","sets in python","Functions in python","oops in python","python class and objects oops python","operator overiding in python"]

search=input("Search\n\n").lower().split()

before=time.time()

search_tags={}


a=0

for every in l:
		
	every=every.split()
		
	for each in search:
		
		a+=every.count(each)
	
	if a>0:
		
		if a in search_tags:
				
			search_tags[a].append(" ".join(every))
		
			
		else:
			search_tags[a]=[" ".join(every)]
	
	a=0
	

search_results=sorted(search_tags,reverse=True)


search_result=[]


for each in search_results:
	
	search=search_tags.get(each)
	
	for s in search:
		
		search_result.append(s)
		
after=time.time()

time_taken=str(after-before)[:6]

print(f"{len(search_result)} results found in ({time_taken} seconds)")

print(*search_result,sep="\n")