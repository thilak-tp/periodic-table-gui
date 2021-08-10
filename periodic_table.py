# Propties to be added.
# 1. Atomic number
# 2. Atomic mass
# 3. Atomic radius
# 4. Density 
# 5. Boiling point
# 6. Melting point
# 7. Shell configuration
# 8. Electronic configuration

import tkinter as tk

class App(tk.Frame):
    # A constructor to initialize the class object.
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.winfo_toplevel().title("Periodic Table of the Elements")
        self.topLabel = tk.Label(self, text="Click the element you would like information about.", font=20)
        self.topLabel.grid(row=0, column=0, columnspan=18)

        column1 = [
            ('H', 'Hydrogen', 'Atomic No= 1\nAtomic Weight =1.01\nState = Gas\nCategory = Alkali Metals'),
            ('Li', 'Lithium', 'Atomic No = 3\nAtomic Weight = 6.94\nState = Solid\nCategory = Alkali Metals'),
            ('Na', 'Sodium', 'Atomic # = 11\nAtomic Weight = 22.99\nState = Solid\nCategory = Alkali Metals'),
            ('K', 'Potassium', 'Atomic # = 19\nAtomic Weight = 39.10\nState = Solid\nCategory = Alkali Metals'),
            ('Rb', 'Rubidium', 'Atomic # = 37\nAtomic Weight = 85.47\nState = Solid\nCategory = Alkali Metals'),
            ('Cs', 'Cesium', 'Atomic # = 55\nAtomic Weight = 132.91\nState = Solid\nCategory = Alkali Metals'),
            ('Fr', 'Francium', 'Atomic # = 87\nAtomic Weight = 223.00\nState = Solid\nCategory = Alkali Metals')]
        