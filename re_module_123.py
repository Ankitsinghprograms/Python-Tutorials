
import re

#help(re)

"""

Meta characters:-
. =any character except '\n'
^ starts with
$ ends with
* Zero to any no. of occurence
+ One to any no. of occurence
{int} specified no. of occurence
() group
| either


\A -string Starts with
\b - charcters starts or ends with
\B character not starts or ends with
\d - chracter [0-9]
\D- charcter not [0-9]
\s-whitspace character
\S-Not whitespace charcter
\w-[a-z][ 0-9]_(underscore)
\W- Not [a-z][0-9]_(underscore)
\Z-Ends with



Functions:-
finditer-Return matches in iterator
findall- Return all mathes in list
search-First match
split-Split specific pattern and make list of others
sub(pattern,replace,string)-Replaces specific pattern to specified charcter in string
"""

#simple search without metatags

print("\n\n simple search without metatags \n\n")

b=re.compile("or")

a="Hello world"

c=b.finditer(a)

for each in c:
	print(each)


# . (any) meta tag

print("\n\n. Starts with\n\n")

b=re.compile(".or..")

a="Hello world"

c=b.finditer(a)

for each in c:
	print(each)
	
	
	
# ^ (starts with)

print("\n\n^ Starts with\n\n")

b=re.compile("^Hello")

a="Hello world"

c=b.finditer(a)

for each in c:
	
	print(each)
	
	
# $ (ends with)

print("\n\n$ Ends with\n\n")

b=re.compile("ld$")

a="Hello world"

c=b.finditer(a)

for each in c:
	
	print(each)
	
	
# * Zero to any no. of occurence

print("\n\n* Zero to any no. of occurence\n\n")

b=re.compile("He*")

a="Hello  hehe H Heeeeeeeeee Hii "

c=b.finditer(a)

for each in c:
	
	print(each)
	
	
# + One to any no. of occurence

print("\n\n+ One to any no. of occurence\n\n")

b=re.compile("He+")

a="Hello  Heeeeeeeeee Hii "

c=b.finditer(a)

for each in c:
	
	print(each)
	

# {} specified no. of occurence


print("\n\n{} Specified no. of occurence\n\n")

b=re.compile("(He){2}")

a="Hello  Heeeeeeeeee Hii HeHe"

c=b.finditer(a)

for each in c:
	
	print(each)
	
	
	
# () Group

print("\n\n() Group\n\n")

b=re.compile("(He)*")

a="Hello H  Heeeeeeeeee Hii "

c=b.finditer(a)

for each in c:
	
	print(each)
	
# | Either (same as or)

print("\n\n | Either\n\n")

b=re.compile("H|e")

a="Hello H  Heeeeeeeeee Hii "

c=b.finditer(a)

for each in c:
	
	print(each)
	
	
	
# \A String starts with

print("\n\n \A string starts with\n\n")

b=re.compile("\AHe")

a="Hello H  Heeeeeeeeee Hii "

c=b.finditer(a)

for each in c:
	
	print(each)


	
# \b String starts or ends with

print("\n\n \\b Characters starts or ends with\n\n")

b=re.compile(r"\bHe")

a="Hello H  Heeeeeeeeee Hii "

c=b.finditer(a)

for each in c:
	
	print(each)
	
	
#\w [a-z][0-9]_


print("\n\n \w [a-z][0-9]_\n\n")

a=re.compile("\w")
txt="Hsllo 843g#+&3-_-_-#-363736"
b=a.finditer(txt)

for each in b:
	print(each)	
	
	
#\W Not [a-z][0-9]_


print("\n\n \W Not [a-z][0-9]_\n\n")

a=re.compile("\W")
txt="Hsllo 843g#+&3-_-_-#-363736"
b=a.finditer(txt)

for each in b:
	print(each)	
	
	
#\d [0-9]


print("\n\n \d [0-9]\n\n")

a=re.compile("\d")
txt="Hsllo 843g#+&3-_-_-#-363736"
b=a.finditer(txt)

for each in b:
	print(each)	
	
	
#\D Not [0-9]


print("\n\n \D [0-9]\n\n")

a=re.compile("\D")
txt="Hsllo 843g#+&3-_-_-#-363736"
b=a.finditer(txt)

for each in b:
	print(each)	
	
	
	
#\s whitespace character


print("\n\n \s whitespace character\n\n")

a=re.compile("\s")
txt="Hsllo 843g#+&3-_-_-#-363736"
b=a.finditer(txt)

for each in b:
	print(each)	
	
	
#\S Not whitespace charcter


print("\n\n \S Not white space character\n\n")

a=re.compile("\S")
txt="Hsllo 843g#+&3-_-_-#-363736"
b=a.finditer(txt)

for each in b:
	print(each)	
	
	
	
#\Z ends with


print("\n\n \Z endswith\n\n")

a=re.compile("\d{2}\Z")
txt="Hsllo 843g#+&3-_-_-#-363736"
b=a.finditer(txt)

for each in b:
	print(each)	
	
	
	
#Functions

#Finditer
print("\n\n finditer-Return matches in iterator\n\n")

a=re.compile("\d{2}")
txt="Hsllo 843g#+&3-_-_-#-363736"
b=a.finditer(txt)

for each in b:
	print(each)	
	
	
#Findall- Return all mathces in list

print("\n\n findall-Return matches in list\n\n")

patt=re.compile("\S")
txt="Hii"
print(patt.findall(txt))


#search-Return First match

print("\n\n fsearch-Return First match\n\n")

patt=re.compile("\A")
txt="Hii"
print(patt.search(txt))



#search-Return First match

print("\n\n search-Return First match\n\n")

patt=re.compile("\A")
txt="Hii"
print(patt.search(txt))


#Split specific pattern and make list of others

print("\n\n Split specific pattern and make list of others\n\n")

patt=re.compile("i")
txt="Hii"
print(patt.split(txt))



#sub(pattern,replace,string)-Replaces specific pattern to specified charcter in string


print("\n\n sub(pattern,replace,string)-Replaces specific pattern to specified charcter in string\n\n")

txt="Sourabh Interesting Facts"

print(re.sub("\s","-",txt))








#Task (To find phone no.)

print("\n\n Task\n\n")
	
	
a=re.compile(r"\+91 \d{5} \d{5}")

text=r" +91 97083 66564  hsgzgdhdg  +91 93343 74992 hdgshsyeyeceuzbc  +91 93342 74992"

b=a.finditer(text)

for e in b:

	print(e)
	
	
	
	
	
	
	
	
	
	
	