a=["yAlastair"," CampbellA"," (VERY LONG)"," ESSAY ON POLITICAL"," COMMUNICA","TIONS","i hate facebook",7,3,26,445,1,2,4,1, "FRENCH"] 
#STYLEPosted by Alastair Campbell | Oct 19, 2011 | Economy, Foreign Policy, Media, Politics | 9  |     The post has just arrived and in it a very nice surprise, the discovery that Jacques Seguela, one-time adviser to President Mitterrand, now close confidant of President and Madame Sarkozy (indeed he intoduced them), and something of a legend in French political communications, has dedicated his latest book to little old moi.With apologies for the missing accents here
for i in a:
	if i=="i hate facebook":
		continue 
	if type(i)==str:
		print("Facbook user",i)