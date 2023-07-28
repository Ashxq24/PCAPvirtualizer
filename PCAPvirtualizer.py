import sys
import os
import socket
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

root =Tk()
app = Window(root)
root.title("PCAP VISUALIZER")
root.geometry("800x500")
bgimg= ImageTk.PhotoImage(Image.open('/home/kali/Desktop/CNProject/PCAPvirtualizer/test/pcapvisual/bg.jpg'))
limg= Label(root, i=bgimg)
limg.pack()
lbl=Label(root,text="Browse the pcap file to draw its visualization",fg='black',bg='red',font=("Times", 16 ))
lbl.place(x=30,y=30)
my_dir=' '

def my_browse():
	global my_dir
	my_dir = filedialog.askdirectory()
	l1.config(text=my_dir)

b1=Button(root,text='Browse',fg='blue',font=12,command=lambda:my_browse())
b1.place(x=70,y=100)
l1=Label(root,text=my_dir,bg='red',font=12)
l1.place(x=170,y=105)

def run_layer4():
    
    os.system("python main.py -i %s -o UDPTCP.png --layer4" % my_dir)
    
btn1=Button(root,text="VISUALIZE UDP/TCP COMMUNICATION",fg='red',command=lambda:run_layer4())
btn1.place(x=70,y=200)


def run_layer3():
	os.system("python main.py -i %s -o IP.png --layer3" % my_dir)
	
btn2=Button(root,text="VISUALIZE IP COMMUNICATION",fg='red',command=lambda:run_layer3())
btn2.place(x=70,y=300)

def run_layer2():
	os.system("python main.py -i %s -o DEVICE.png --layer2" % my_dir)

btn3=Button(root,text="VISUALIZE DEVICE LEVEL",fg='red',command=lambda:run_layer2())
btn3.place(x=70,y=400)

def run_layer2g():
	os.system("python main.py -i %s -g graphDEVICE.dot --layer2" % my_dir)
def run_layer2a():
	run_layer2()
	os.system("dot -Tpng graphDEVICE.dot -o graphDEVICE.png")

btn4=Button(root,text="MAKE GRAPH FOR DEVICE LEVEL",fg='red',command=lambda:[run_layer2g(),run_layer2a()])
btn4.place(x=400,y=400)

def run_layer3g():
	os.system("python main.py -i %s -g graphIP.dot --layer3" % my_dir)
def run_layer3a():
	run_layer3g()
	os.system("dot -Tpng graphIP.dot -o graphIP.png")

btn4=Button(root,text="MAKE GRAPH FOR IP COMMUNICATION",fg='red',command=lambda:[run_layer3g(),run_layer3a()])
btn4.place(x=400,y=300)

def run_layer4g():
	os.system("python main.py -i %s -g graphUDPTCP.dot --layer4" % my_dir)
def run_layer4a():
	run_layer4g()
	os.system("dot -Tpng graphUDPTCP.dot -o graphUDPTCP.png")

btn4=Button(root,text="MAKE GRAPH FOR UDP/TCP COMMUNICATION",fg='red',command=lambda:[run_layer4g(),run_layer4a()])
btn4.place(x=400,y=200)




root.mainloop()



