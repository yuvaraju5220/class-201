from tkinter import *
window=Tk()


window.title('Simple interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p = float(principal.get())
    r = float (rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest=round(i,2)
    result_label.destroy()

    message=Label(result_frame,text="Interest on Rs  "+str(p)+"at rate of interest "+str(r)+"for "+str(t)+" years is Rs."+str(interest), bg = "lightcyan", font=("Calibri", 12), width=52)
    message.place(x=20,y=40)
    message.pack()






app_label=Label(window, text="Simple interest CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principal_label=Label(window, text="enter principal", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
principal_label.place(x=20, y=90)

principal=Entry(window, text="", bd=2, width=22)
principal.place(x=150, y=92)

rate_label=Label(window, text="enter ROI", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
rate_label.place(x=20, y=120)

rate=Entry(window, text="", bd=2, width=22)
rate.place(x=150, y=122)

time=Label(window, text="time(in years)", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
time.place(x=20,y=150)

time=Entry(window, text="", bd=2, width=22)
time.place(x=150, y=152)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command=calculate_interest)
calculate_button.place(x=150,y=170)


result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()
 

window.mainloop()