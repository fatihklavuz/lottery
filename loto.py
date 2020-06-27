import random

a=0

while a>=0:

	b1=random.randint(1,49)
	b2=random.randint(1,49)
	b3=random.randint(1,49)
	b4=random.randint(1,49)
	b5=random.randint(1,49)
	b6=random.randint(1,49)
	print(str(b1)+" "+str(b2)+" "+str(b3)+" "+ str(b4) + " "+ str(b5) + " "+str(b6) + "\n")
	w=open("loto.txt","a")
	w.write(str(b1)+" "+str(b2)+" "+str(b3)+" "+ str(b4) + " "+ str(b5) + " "+str(b6) + "\n")
	w.close()	
