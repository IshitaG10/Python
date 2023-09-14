from tkinter import *

value_in_km =  0

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=330,height=190)
window.config(padx=45,pady=30)

def calculate():
    miles = int(input.get())
    value_in_km = miles*1.6
    result_label.config(text=value_in_km)



input = Entry(width=10,font=("Arial",14))
input.grid(row=0,column=1)
input.insert(END,string="0")


mile_label = Label(text="Miles", font=("Arial",14))
mile_label.grid(row=0,column=2)
mile_label.config(padx = 9,pady=7)

text_label = Label(text = "is equal to",font=("Arial",14))
text_label.grid(row=1,column=0)


result_label = Label(text = value_in_km,font=("Arial",14))
result_label.grid(row=1,column=1)
result_label.config(pady=8)

km_label = Label(text="Km",font=("Arial",14))
km_label.grid(row=1,column=2)


calculate_button = Button(text="Calculate",font=("Arial",14),command=calculate)
calculate_button.grid(row=2,column=1)
calculate_button.config(padx=3,pady=3)


window.mainloop()

