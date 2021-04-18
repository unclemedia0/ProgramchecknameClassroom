'''
- ມາຮູ້ຈັກ Python GUI
- tkinter package ສຳຫຼັບພັດທະນາ GUI
- list method (ຄຳສັ່ງຍ່ອຍຂອງ list)
- dictionary ຄືຍັງ?
- def (ຟັງຊັນຄືຍັງ?)
- ບັນທືກຂໍ້ມູນລົງ csv
- ອອກເເບບໂປຣເເກຣມຄຳນວນງ່າຍໆ
- ສ້າງຟອມກອກເພືອບັນທືກຂໍ້ມູນ
'''
from tkinter import *
GUI = Tk()
import csv
#CSV File

ຟື້ນຫຼັງ = PhotoImage(file='unclemedia.png').subsample(2)
p = Label(GUI, image=ຟື້ນຫຼັງ)
p.pack(pady=20)

def WritetoCSV(data):
 	with open('checkname.csv','a',newline='',encoding='utf-8') as file:
 		fw = csv.writer(file)
 		fw.writerow(data)
 	print('ບັນທືກສຳເລັດເເລ້ວ')

GUI.title('ໂປຣເເກຣມທຳທືກຂໍ້ມູນ')
GUI.geometry('600x900+500+200') # xກວ້າງ x yສູງ
FONT1 = ('Phetsarath OT',20)
FONT2 = ('Phetsarath OT',20)
FONT3 = ('Phetsarath OT',20)

L1 = Label(GUI,text='ຊື່:',font=FONT1)
L1.pack()
v_keep1 = StringVar()
E1 = Entry(GUI, textvariable=v_keep1, font=FONT1,width=30)
E1.pack()


L2 = Label(GUI,text='ນາມສະກຸນ:',font=FONT2)
L2.pack()
v_keep2 = StringVar()
E2 = Entry(GUI, textvariable=v_keep2, font=FONT2,width=30)
E2.pack()


L3 = Label(GUI,text='ຊັ້ນຮຽນ:',font=FONT3)
L3.pack()
v_keep3 = StringVar()
E3 = Entry(GUI, textvariable=v_keep3, font=FONT3,width=30)
E3.pack()

def Savebutton(event=None):
	keep1 = v_keep1.get()
	keep2 = v_keep2.get()
	keep3 = v_keep3.get()
	print(keep1)
	print(keep2)
	print(keep3)
	dt = [keep1,keep2,keep3] # dt = data
	WritetoCSV(dt)
	print('...ທົດສອບ...')
	####### clearn ຂໍ້ມູນໃນຊ່ອງ #######
	v_keep1.set('')
	v_keep2.set('')
	v_keep3.set('')
	E1.focus() # corser in send 
E3.bind('<Return>',Savebutton) # ເຊືອມຕໍ່ປຸ່ມ enterທີ່ keyboad

B1 = Button(GUI,text='ຢືນຢັນການລົງຊື່',command=Savebutton)
B1.pack(ipadx=10,ipady=5)


GUI.mainloop()