#Pay Counter Test by altoid
print("PAY COUNTER BY ALTOID")

def Paycounter():
	d = input("Enter Pay Here: ")
	f = input("Enter Rate Here: ")
	Xh = int(d) * int(f)
	print("Your Total Is:",Xh)

Paycounter()

def Paycounter1():
	j = input("RESTARTING... type anything to continue: ")
	y = input("Enter Pay Here: ")
	u = input("Enter Rate Here: ")
	Fh = int(y) * int(u)
	print("Your Pay Is:",Fh)

def Again():
	h = input("Again? [y/n]:")
	if (h) == "y":
		Paycounter()
	if (h) == "n":
		    a = input("Are You Sure? [y/n]:")
		    if (a) == "y":
			    quit()
		    if (a) == "n":
			    Paycounter1()
Again()
print("You Have Been GNOMED")