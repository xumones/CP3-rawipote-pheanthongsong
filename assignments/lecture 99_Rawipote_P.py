from tkinter import *
import math

def leftClickButton(event):
    text = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    if text >= 30:
        labelResult.configure(text='อ้วนมาก')
    elif text <= 29.9 and text >= 25:
        labelResult.configure(text='อ้วน')
    elif text <= 24.9 and text >= 23.0:
        labelResult.configure(text='น้ำหนักเกิน')
    elif text <= 22.9 and text >= 18.6:
        labelResult.configure(text='น้ำหนักปกติ เหมาะสม')
    elif text <= 18.5:
        labelResult.configure(text='ผอมเกินไป')
    result.configure(text=round(text))
MainWindow = Tk()
labelHeight = Label(MainWindow,font=("FC Daisy",50), text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow,font=("FC Daisy",50))
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow,font=("FC Daisy",50), text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow,font=("FC Daisy",50))
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,font=("FC Daisy",50),text = "คำนวน",width=15,heigh=2)
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,font=("FC Daisy",50),text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
result = Label(MainWindow,font=("FC Daisy",50),text="ค่า BMI")
result.grid(row=3,column=1)

MainWindow.mainloop()
