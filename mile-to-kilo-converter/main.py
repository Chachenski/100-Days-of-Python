from tkinter import *

#Converter function
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

#Window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

#Input
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

#Button
calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()