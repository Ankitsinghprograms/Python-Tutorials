import argparse

import sys

'''
no sign => madatory argumnets then agrmuent while calling file
- and -- => optional arguments take by - or - and variable name

'''

#45,3,×=555
#56,9,+=77
#56,6,/=4

def add(args):
	
	b=args.y
	
	a=args.x
	
	o=args.o
	
	if (b==45 or a==45) and (a==3 or b==3) and o=="×":
		return 555
		
	elif (b==56 or a==56) and (b==9 or a==9) and o=="+":
		return 77
	
	elif (b==56 or a==56) and (b==6 or a==6) and o=="÷":
		return 4

	elif args.o=="+":
		
		return args.x+args.y
	
	elif args.o=="×":
		
		return args.x*args.y
		
	elif args.o=="÷":
		
		return args.x/args.y
		
	elif args.o=="-":
		
		return args.x-args.y
		
	else:
		return "Wrong operator Argumnet available:- '+' '-' '×' '÷' "
	
if __name__=="__main__":
	
	p=argparse.ArgumentParser()
	
	p.add_argument("o",type=str,default="+",help="Argument operator;str")
	
	p.add_argument("-x",type=int,default=0,help="argument x;int")
	
	p.add_argument("--y",type=int,default=0,help="Argument y;int")
	
args=p.parse_args()
sys.stdout.write(str(add(args)))