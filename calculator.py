from Tkinter import *
class Calculator(Frame):
    def __init__(self):
        self.expression = []
        Frame.__init__(self)
        self.master.title("Calculator")
        
        #main frame fills entire container, expands if necessary
        self.master.rowconfigure(0, weight =1)
        self.master.columnconfigure(0, weight =1)
        self.grid(sticky=W+E+N+S)

                                    
        self.entry=Entry(self)
        self.entry.grid(row=0, columnspan=4, sticky=W+E+N+S)
        self.entry.insert(INSERT, "enter text here")
        
        self.button1=Button(self, text="7")
        self.button1.grid(row=1, column=0, sticky=W+E+N+S)
        self.button1.bind('<Button-1>', lambda event: self.command(7, event))

        self.button2=Button(self, text="8")
        self.button2.grid(row=1, column=1, sticky=W+E+N+S)
        self.button2.bind('<Button-1>', lambda event: self.command(8, event))

        self.button3=Button(self, text="9")
        self.button3.grid(row=1, column=2, sticky=W+E+N+S)
        self.button4=Button(self, text="/")
        self.button4.grid(row=1, column=3, sticky=W+E+N+S)
        self.button5=Button(self, text="4")
        
        self.button5.grid(row=2, column=0, sticky=W+E+N+S)
        self.button6=Button(self, text="5")
        self.button6.grid(row=2, column=1, sticky=W+E+N+S)
        self.button7=Button(self, text="6")
        self.button7.grid(row=2, column=2, sticky=W+E+N+S)
        self.button8=Button(self, text="*")
        self.button8.grid(row=2, column=3, sticky=W+E+N+S)
        
        self.button9=Button(self, text="1")
        self.button9.grid(row=3, column=0, sticky=W+E+N+S)
        self.button10=Button(self, text="2")
        self.button10.grid(row=3, column=1, sticky=W+E+N+S)
        self.button11=Button(self, text="3")
        self.button11.grid(row=3, column=2, sticky=W+E+N+S)
        self.button12=Button(self, text="-")
        self.button12.grid(row=3, column=3, sticky=W+E+N+S)
        
        self.button13=Button(self, text="0")
        self.button13.grid(row=4, column=0, sticky=W+E+N+S)
        self.button14=Button(self, text=".")
        self.button14.grid(row=4, column=1, sticky=W+E+N+S)
        self.button15=Button(self, text="=")
        self.button15.grid(row=4, column=2, sticky=W+E+N+S)
        self.button16=Button(self, text="+")
        self.button16.grid(row=4, column=3, sticky=W+E+N+S)

    def command(self, button_selected, event):
        """
        it adds the button selected to expression
        it also replace the digit in entry with one selected
        prints which button has been pressed for debugging purpose
        :param button_selected: string to the button selected
        :return: None
        """

        # clear the entry first
        self.entry.delete(0, len(self.entry.get()))
        # then add the selected button
        self.entry.insert(INSERT, button_selected)
        self.expression.append(button_selected)
        print "button_selected:", button_selected




def main():
    Calculator().mainloop()
if __name__ == "__main__":
    main()
"""this is my solution to problem 10.3 page 389 on the book av sent to y      
        
ou. i have also sent a scndcalculator.py program on which i was trying to add
functionality to button 1.please go through it and jst tel me why the program is
giving me the error when i click 7 on the calculator.in the program, i was trying to solve problem 10.6 on the same page"""
