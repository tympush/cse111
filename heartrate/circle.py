import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math

def main():

    root = tk.Tk()

    frm_main = Frame(root)
    frm_main.master.title("Heart Rate")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)

    root.mainloop()



def populate_main_window(frm_main):


    lbl_age = Label(frm_main, text="radius:")

    ent_age = IntEntry(frm_main, width=4, lower_bound=1, upper_bound=90)

    lbl_age_units = Label(frm_main, text="cm{2}\u00B2")

    lbl_rates = Label(frm_main, text="area:")

    lbl_slow = Label(frm_main, width=3)
    lbl_fast = Label(frm_main, width=3)
    lbl_rate_units = Label(frm_main, text="cm")

    btn_clear = Button(frm_main, text="Clear")

    lbl_age.grid(      row=0, column=0, padx=3, pady=3)
    ent_age.grid(      row=0, column=1, padx=3, pady=3)
    lbl_age_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_rates.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_slow.grid(      row=1, column=1, padx=3, pady=3)
    lbl_fast.grid(      row=1, column=2, padx=3, pady=3)
    lbl_rate_units.grid(row=1, column=3, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")



    def calculate(event):

        try:
            # Get the user's age.
            age = ent_age.get()

            max_rate = math.pi * age ** 2

            lbl_fast.config(text=f"{max_rate:.0f}")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_slow.config(text="")
            lbl_fast.config(text="")
    


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_age.clear()
        lbl_slow.config(text="")
        lbl_fast.config(text="")
        ent_age.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_age.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_age.focus()


if __name__ == "__main__":
    main()