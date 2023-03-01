import tkinter as tk

# create a calculator class


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.result = tk.StringVar()
        self.result.set("0")
        self.expression = ""

        # create the display
        self.display = tk.Label(
            master, textvariable=self.result, anchor="e", font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=5)

        # create the buttons
        button_values = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "C", "/"
            "(", ")", "=", "%"
        ]
        self.buttons = []

        for i, val in enumerate(button_values):
            button = tk.Button(
                master, text=val, width=5, height=2,
                command=lambda val=val: self.button_click(val)
            )
            self.buttons.append(button)
            button.grid(row=1+i//4, column=i % 4)

    def button_click(self, val):
        if val == "C":
            self.expression = ""
            self.result.set("0")
        elif val == "=":
            try:
                self.result.set(eval(self.expression))
            except:
                self.result.set("ERROR")
            self.expression = ""
        else:
            self.expression += str(val)
            self.result.set(self.expression)


root = tk.Tk()
calc = Calculator(root)
root.mainloop()
