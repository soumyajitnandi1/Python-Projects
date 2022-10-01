import tkinter as tk
from tkinter import ttk

w = tk . Tk ()
w . title ( 'BIO DATA' )




# Labels & Entry-boxes .......
l0 = tk . Label ( w , text = "Name : " )
l0 . grid ( row = 0 , column = 0 , sticky = tk . W )

N = tk.StringVar()
e0 = tk . Entry ( w , width = 30 , textvariable = N )
e0 . grid ( row = 0 , column = 1 , sticky = tk . W )

l = tk . Label ( w , text = "" )
l . grid ( row = 1 , column = 0 , sticky = tk . W )




l1 = tk . Label ( w , text = "Father's Name : ")
l1 . grid ( row = 2 , column = 0 , sticky = tk . W )

FN = tk.StringVar()
e1 = tk . Entry ( w , width = 30 , textvariable = FN )
e1 . grid ( row = 2 , column = 1 , sticky = tk . W )

l = tk . Label ( w , text = "" )
l . grid ( row = 3 , column = 0 , sticky = tk . W )




l2 = tk . Label ( w , text = "Mother's Name : " )
l2 . grid ( row = 4 , column = 0 , sticky = tk . W )

MoN = tk.StringVar()
e2 = tk . Entry ( w , width = 30 , textvariable = MoN )
e2 . grid ( row = 4 , column = 1 , sticky = tk . W )

l = tk . Label ( w , text = "" )
l . grid ( row = 5 , column = 0 , sticky = tk . W )




l3 = tk . Label ( w , text = "Permanent Address : " )
l3 . grid ( row = 6 , column = 0 , sticky = tk . W )

PA = tk.StringVar()
e3 = tk . Entry ( w , width = 30 , textvariable = PA )
e3 . grid ( row = 6 , column = 1 , sticky = tk . W )

l = tk . Label ( w , text = "" )
l . grid ( row = 7 , column = 0 , sticky = tk . W )




S = tk.IntVar()
cbad = tk.Checkbutton( w , text=' Same as Permanent address .', variable = S)
cbad.grid ( row =7 , column = 1 , sticky = tk . W)

l4 = tk . Label ( w , text = "Current Address : " )
l4 . grid ( row = 8 , column = 0 , sticky = tk . W )

CA = tk.StringVar()
e4 = tk . Entry ( w , width = 30 , textvariable = CA )
e4 . grid ( row = 8 , column = 1 , sticky = tk . W )

l = tk . Label ( w , text = "" )
l . grid ( row = 9 , column = 0 , sticky = tk . W )




l5 = tk . Label ( w , text = "Email Id : " )
l5 . grid ( row = 10 , column = 0 , sticky = tk . W )

EI = tk.StringVar()
e5 = tk . Entry ( w , width = 30 , textvariable = EI )
e5 . grid ( row = 10 , column = 1 , sticky = tk . W )

l = tk . Label ( w , text = "" )
l . grid ( row = 11 , column = 0 , sticky = tk . W )




l6 = tk . Label ( w , text = "ISD & Mobile No : " )
l6 . grid ( row = 12 , column = 0 , sticky = tk . W )

ISD=tk.StringVar()
e6 = tk . Entry ( w , width = 8 , textvariable = ISD )
e6 . grid ( row = 12 , column = 1 , sticky = tk . W)

MN = tk.StringVar()
e6_1 = tk. Entry ( w , width = 20 , textvariable = MN )
e6_1 . grid ( row = 12 , column = 1 , sticky = tk . E )

l = tk . Label ( w , text = "" )
l . grid ( row = 13 , column = 0 , sticky = tk . W )




l7 =tk.Label(w , text = "Date of birth (dd-mm-yyyy) : " )
l7 . grid ( row = 14 , column = 0 , sticky = tk . W )

dd = tk.IntVar()
e7 = tk . Entry ( w , width = 10 , textvariable = dd )
e7 . grid ( row = 14 , column = 1 , sticky = tk . W )

mm = tk.IntVar()
e7_1 = tk . Entry ( w , width = 8 , textvariable = mm )
e7_1 . grid (row = 14 , column = 1 )

yyyy = tk.IntVar()
e7_2 = tk . Entry ( w , width = 10, textvariable = yyyy )
e7_2 . grid ( row = 14 , column = 1 , sticky = tk . E )

l = tk . Label ( w , text = "" )
l . grid ( row = 15 , column = 0 , sticky = tk . W )




l8 = tk . Label ( w , text = "Height (in cms) : " )
l8 . grid ( row = 0 , column = 2 , sticky = tk . W )

H = tk.StringVar()
e8 = tk . Entry ( w , width = 11 , textvariable = H )
e8 . grid ( row = 0 , column = 3 , sticky = tk . W )

l = tk . Label ( w , text = "" )
l . grid ( row = 1 , column = 2 , sticky = tk . W )




l9 = tk . Label ( w , text = "Weight (in Kgs) : " )
l9 . grid ( row = 2 , column = 2 , sticky = tk . W )

wt = tk.StringVar()
e9 = tk . Entry ( w , width = 11 , textvariable = wt )
e9 . grid ( row = 2 , column = 3 , sticky = tk . W )

l = tk . Label ( w , text = "" )
l . grid ( row = 3 , column = 2 , sticky = tk . W )




# Labels & Combo-boxes.......
l10= tk . Label ( w , text = "PWD : " )
l10 . grid ( row = 4 , column = 2 , sticky = tk . W )

pwd = tk . StringVar()
cb = ttk . Combobox( w , width = 5 , state = 'readonly' , textvariable = pwd )
cb [ 'values' ] = ( 'YES' , 'NO' )
cb.grid ( row = 4 , column = 3 , sticky = tk . W )

l = tk . Label ( w , text = "" )
l . grid ( row = 5 , column = 2 , sticky = tk . W )	




l11 = tk . Label ( w , text = "PWD Percentage : " )
l11 . grid ( row = 6 , column = 2 , sticky = tk . W )
	
pwdpntg = tk . StringVar()
cb1 = ttk . Combobox( w , width = 5 , textvariable = pwdpntg )
cb1 [ 'values' ] = ( 0 ,5 , 25 , 50 , 75 , 95 )
cb1.grid ( row = 6 , column = 3 , sticky = tk . W )
cb1 . current (0)	

l = tk . Label ( w , text = "" )
l . grid ( row = 7 , column = 2 , sticky = tk . W )	



# Label & Radio-buttons .......
l12 = tk . Label ( w , text = "Caste : " )
l12  . grid ( row = 8 , column = 2 , sticky = tk . W )

C = tk . StringVar ()
rb = tk . Radiobutton ( w , text ='UR' , value ='UR' , variable = C )
rb.grid ( row = 9 , column = 2 , sticky = tk . W )

rb1 = tk . Radiobutton ( w , text ='OBC' , value ='OBC' , variable = C )
rb1.grid ( row = 9 , column = 2 , sticky = tk . E )

rb2 = tk . Radiobutton ( w , text ='SC' , value ='SC' , variable = C )
rb2.grid ( row = 9 , column = 3 , sticky = tk . W )

rb3 = tk . Radiobutton ( w , text ='ST' , value ='ST' , variable = C )
rb3.grid ( row = 9 , column = 3 , sticky = tk . E )




l13 = tk . Label ( w , text = " Employed :-" )
l13 . grid ( row = 10 , column = 2 , sticky = tk . W )	

J=tk.StringVar()
rb4 = ttk.Radiobutton(w,text='Yes',value='Yes', variable = J)
rb4.grid(row=11,column=2 ,sticky=tk.E)

rb5 = ttk.Radiobutton(w,text='NO',value='NO', variable = J)
rb5.grid(row=11,column=3 , sticky=tk.W)




# Check-buttons......
A = tk.IntVar()
cb = tk.Checkbutton( w , text=' Agree, all true', variable = A)
cb.select()
cb.grid ( row =12 , column = 2)




F = tk.IntVar()
cb1 = ttk.Checkbutton( w , text='You are OK, fit', variable = F)
cb1.grid ( row =13, column = 2)




# Buttons & their commands........
def act1() :
	Nm=N.get()
	FNm=FN.get()
	MNm = MoN.get()
	PAd = PA.get()
	if S.get() == 1 :
		CAd="Same as Permanent Address."
	else :
		CAd =CA.get()
	EId = EI.get()
	ISDc = ISD.get()
	MNo = MN.get()
	d = dd.get()
	m = mm.get()
	y = yyyy.get()
	Ht = H.get()
	wgt = wt.get()
	pwdp = pwd.get()
	prcnt=pwdpntg.get()
	if pwdp == 'YES' and prcnt != '0' :
		pwdpcntg = prcnt
	elif pwdp == 'NO' or pwdp == '' :
		pwdpcntg = 'N/A'
	else :
		pwdpcntg = 1
	Cs = C.get()
	Jb = J.get()
	if A.get() == 1 :
		Ag = 'Agreed'
	else :
		Ag = 'Not Agreed'
	if F.get() == 1 :
		Ft = 'Fit & OK'
	else :
		Ft = 'Unfit & not OK'
		
	if Nm != '' :
		l0 . configure (foreground='green')
	if FNm != '' :
		l1 . configure (foreground='green')
	if MNm != '' :
		l2 . configure (foreground='green')
	if PAd != '' :
		l3 . configure (foreground='green')
	if S.get() == 0 and CAd != '' :
		l4 . configure (foreground='green')
	if EId != '' :
		l5 . configure (foreground='green')
	if MNo != '' :
		l6 . configure (foreground='green')
	if d != 0 and m !=  0 and y != 0 :
		l7 . configure (foreground='green')
	if Ht != '' :
		l8 . configure (foreground='green')
	if wgt != '' :
		l9 . configure (foreground='green')
	if pwdp != '' :
		l10 . configure (foreground='green')
	if pwdp == 'YES' :
		l11  . configure (foreground='green')
	if Cs == 'UR' or Cs == 'OBC-A/B' or Cs == 'SC' or Cs == 'ST' :
		l12  . configure (foreground='green')
	if Jb == 'Yes' or Jb == 'No' :
		l13  . configure (foreground='green')
	if S.get() == 1 :	
		cbad.configure(foreground = 'blue')
	if A.get() == 1 or A.get() == 0 :
		cb.configure(foreground = 'Green')
	if F.get() == 1 and F.get() == 0 :#this will not work becauss the check button is 'ttk' check btn
		cb1.configure(foreground='green')
	if C.get() == 'UR' :
		rb.configure(foreground='blue')
	if C.get() == 'OBC' :
		rb1.configure(foreground='blue')
	if C.get() == 'SC' :
		rb2.configure(foreground='blue')
	if C.get() == 'ST' :
		rb3.configure(foreground='blue')
	
	with open ('Bio Datas.txt' , 'a' ) as b :
		b.write(f'''Name : {Nm}
Father : {FNm}
Mother : {MNm}
Permanent Address : {PAd}
Current Address : {CAd}
Email : {EId}
Phone : +{ISDc}{MNo}
D.O.B : {d}.{m}.{y}
Height : {Ht} cms.
Weight : {wgt} Kgs.
PWD : {pwdp}
PWD % : {pwdpcntg}%
Caste : {Cs}
Employee : {Jb}
True data agreement : {Ag}
Health & Sense : {Ft}
\n\n\n''')

def act2() :
	e0 . delete(0 , tk.END )
	e1 . delete(0 , tk.END )
	e2 . delete(0 , tk.END )
	e3 . delete(0 , tk.END )
	e4 . delete(0 , tk.END )
	e5 . delete(0 , tk.END )
	e6 . delete(0 , tk.END )
	e7 .  delete(0 , tk.END )
	e8 . delete(0 , tk.END )
	e9 . delete(0 , tk.END )
	e6_1 . delete(0 , tk.END )
	e7_1 . delete(0 , tk.END )
	e7_2 . delete(0 , tk.END )
	
	b2.configure (background='red')

b1 = ttk . Button( w , text = 'Submit' , command = act1)
b1.grid ( row = 14 , column = 2)

b2 = tk . Button( w , text = 'Clear' , command = act2)
b2.grid ( row = 14 , column = 3)

w.mainloop()