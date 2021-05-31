from tkinter import Tk, Button, Label
from tkinter.constants import CENTER
from speedtest import Speedtest

def update():
    speed_test = Speedtest()
    download_speed = round(speed_test.download() / (10**6), 2)
    upload_speed = round(speed_test.upload() / (10**6), 2)
    down_label.config(text= "Download Speed: - " + str(download_speed) + "Mbps") 
    up_label.config(text= "Upload Speed: - " + str(upload_speed) + "Mbps") 


root = Tk()
root.title("Internet Speed Checker")
root.geometry('400x300')
button = Button(root, text="Get Speed",command=update)
button.place(relx=0.5, rely=0.5, anchor = CENTER)
button.pack()
down_label = Label(root, text="")
down_label.pack()
up_label = Label(root, text="")
up_label.pack()

root.mainloop()