            # ('H', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \n Melting point = \n Electronic Configuration ='),
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import sys
# from tkinter import font
# from tkinter.constants import GROOVE, RAISED, RIDGE, SUNKEN
# from tkinter.font import BOLD, families
# from PIL import *
# Creates and Initiates class 'App'
def img_show1():
    try:
        img1 = Image.open("/home/thilaktp/Documents/Programming/Python/gui-perdiodic-table/img/h.jpeg")
        

    except IOError:
        print("Unable to load image")
        sys.exit(1)
    img1.show()
def img_show():
    window = tk.Tk()

    # load an image with Pillow's [Image]
    loaded_image = Image.open('/home/thilaktp/Documents/Programming/Python/gui-perdiodic-table/img/hydrogen.png')

    # convert loaded_image with Pillow's [ImageTK]
    converted_image = ImageTk.PhotoImage(loaded_image)

    # set canvas dimensions from loaded image size
    (canvas_width, canvas_height) = loaded_image.size

    # create a Tkinter canvas / window
    canvas =Canvas(window, width=canvas_width, 
    height=canvas_height)
    window.title('Window Title')

    # place our converted image in the window
    canvas.create_image(10,10, image=converted_image, 
    anchor=NW)

    # I don't understand this bit either
    canvas.pack()
    canvas.mainloop()

class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.winfo_toplevel().title("[ Periodic Table of the Elements ]" )
        self.topLabel = tk.Label(self, text="Click on an element for more info.", font = 500)
        self.topLabel.grid(row=0, column=0, columnspan=18)

        
        # Names of tk.Buttons in column 1
        column1 = [
            # ('H', 'Hydrogen', 'Atomic # = 1\nAtomic Weight =1.01\nState = Gas\nCategory = Alkali Metals'),
            ('H', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= 32pm \nState = Gas\nCategory = Non-Metal\nDensity= 0.0899 g/cm3\nBoiling Point = -252.9 °C\nMelting point = -259.1 °C\nElectronic Configuration =1s1'),
            ('Li', 'Lithium', 'Atomic No= 11\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point =\nElectronic Configuration ='),
            ('Na', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point =\nElectronic Configuration ='),
            ('K', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point =\nElectronic Configuration ='),
            ('Rb', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point =\nElectronic Configuration ='),
            ('Cs', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point =\nElectronic Configuration ='),
            ('Fr', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point =\nElectronic Configuration =')
            
        #     ('Li', 'Lithium', 'Atomic # = 3\nAtomic Weight = 6.94\nState = Solid\nCategory = Alkali Metals'),
        #     ('Na', 'Sodium', 'Atomic # = 11\nAtomic Weight = 22.99\nState = Solid\nCategory = Alkali Metals'),
        #     ('K', 'Potassium', 'Atomic # = 19\nAtomic Weight = 39.10\nState = Solid\nCategory = Alkali Metals'),
        #     ('Rb', 'Rubidium', 'Atomic # = 37\nAtomic Weight = 85.47\nState = Solid\nCategory = Alkali Metals'),
        #     ('Cs', 'Cesium', 'Atomic # = 55\nAtomic Weight = 132.91\nState = Solid\nCategory = Alkali Metals'),
        #     ('Fr', 'Francium', 'Atomic # = 87\nAtomic Weight = 223.00\nState = Solid\nCategory = Alkali Metals')
            ]
        # # create all tk.Buttons with a loop
        r = 1
        c = 0
        count = 0
        
        # tk.Label(text='1').grid(row = 1,column = 0)

        for b in column1: 
            # if count == 0:
                # count = count + 1
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="firebrick1",
                    #   image='/home/thilaktp/Documents/Programming/Python/gui-perdiodic-table/img/image.jpeg',
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column2 = [
               ('Be', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
               ('Mg', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
               ('Ca', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
               ('Sr', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
               ('Ba', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
               ('Ra', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
                         
            # ('Be', 'Beryllium', 'Atomic # = 4\nAtomic Weight = 9.01\nState = Solid\nCategory = Alkaline Earth Metals'),
            # ('Mg', 'Magnesium', 'Atomic # = 12\nAtomic Weight = 24.31\nState = Solid\nCategory = Alkaline Earth Metal'),
            # ('Ca', 'Calcium', 'Atomic # = 20\nAtomic Weight = 40.08\nState = Solid\nCategory = Alkaline Earth Metals'),
            # ('Sr', 'Strontium', 'Atomic # = 38\nAtomic Weight = 87.62\nState = Solid\nCategory = Alkaline Earth Metal'),
            # ('Ba', 'Barium', 'Atomic # = 56\nAtomic Weight = 137.33\nState = Solid\nCategory = Alkaline Earth Metals'),
            # ('Ra', 'Radium', 'Atomic # = 88\nAtomic Weight = 226.03\nState = Solid\nCategory = Alkaline Earth Metals')
            ]
        r = 2
        c = 1
        for b in column2: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="darkorange1",
                      command=lambda text=b:  self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column3 = [
            ('Sc', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Y', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('La', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Ac', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')

            # ('Sc', 'Scandium', 'Atomic # = 21\nAtomic Weight = 44.96\nState = Solid\nCategory = Trans Metals'),
            # ('Y', 'Yttrium', 'Atomic # = 39\nAtomic Weight = 88.91\nState = Solid\nCategory = Trans Metals'),
            # ('La   >|', 'Lanthanum', 'Atomic # = 57\nAtomic Weight = 138.91\nState = Solid\nCategory = Trans Metals'),
            # ('Ac   >|', 'Actinium', 'Atomic # = 89\nAtomic Weight = 227.03\nState = Solid\nCategory = Trans Metals')
             
            ]
        r = 4
        c = 2
        for b in column3: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="goldenrod1",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column4 = [
                
            ('Ti', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Zr', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Hf', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Rf', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')

            # ('Ti', 'Titanium', 'Atomic # = 22\nAtomic Weight = 47.90\nState = Solid\nCategory = Trans Metals'),
            # ('Zr', 'Zirconium', 'Atomic # = 40\nAtomic Weight = 91.22\nState = Solid\nCategory = Trans Metals'),
            # ('Hf', 'Hanium', 'Atomic # = 72\nAtomic Weight = 178.49\nState = Solid\nCategory = Trans Metals'),
            # ('Rf', 'Rutherfordium', 'Atomic # = 104\nAtomic Weight = 261.00\nState = Synthetic\nCategory = Tran Metal')
            ]
        r = 4
        c = 3
        for b in column4: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="goldenrod1",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 10: 
                r = 1
                c += 1

        column5 = [
            ('V', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Nb', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Ta', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Ha', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('V', 'Vanadium', 'Atomic # = 23\nAtomic Weight = 50.94\nState = Solid\nCategory = Trans Metals'),
            # ('Nb', 'Niobium', 'Atomic # = 41\nAtomic Weight = 92.91\nState = Solid\nCategory = Trans Metals'),
            # ('Ta', 'Tantalum', 'Atomic # = 73\nAtomic Weight = 180.95\nState = Solid\nCategory = Trans Metals'),
            # ('Ha', 'Hahnium', 'Atomic # = 105\nAtomic Weight = 262.00\nState = Synthetic\nCategory = Trans Metals')
            
            
             ]
        r = 4
        c = 4
        for b in column5: 
            tk.Button(self,
                      text=b[0],
                      width=5, height=4,
                      bg="goldenrod1",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 10: 
                r = 1
                c += 1

        column6 = [
            ('Cr', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Mo', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('W', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Sg', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('Cr', 'Chromium', 'Atomic # = 24\nAtomic Weight = 51.99\nState = Solid\nCategory = Trans Metals'),
            # ('Mo', 'Molybdenum', 'Atomic # = 42\nAtomic Weight = 95.94\nState = Solid\nCategory = Trans Metals'),
            # ('W', 'Tungsten', 'Atomic # = 74\nAtomic Weight = 183.85\nState = Solid\nCategory = Trans Metals'),
            # ('Sg', 'Seaborgium', 'Atomic # = 106\nAtomic Weight = 266.00\nState = Synthetic\nCategory = Trans Metals')
            ]
        r = 4
        c = 5
        for b in column6: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="goldenrod1",
                      command=lambda text=b:  self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column7 = [
            ('Mn', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Tc', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Re', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Bh', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('Mn', 'Manganese', 'Atomic # = 25\nAtomic Weight = 178.49\nState = Solid\nCategory = Trans Metals'),
            # ('Tc', 'Technetium', 'Atomic # = 43\nAtomic Weight = 178.49\nState = Synthetic\nCategory = Trans Metals'),
            # ('Re', 'Rhenium', 'Atomic # = 75\nAtomic Weight = 178.49\nState = Solid\nCategory = Trans Metals'),
            # ('Bh', 'Bohrium', 'Atomic # = 107\nAtomic Weight = 262.00\nState = Synthetic\nCategory = Trans Metals')
            ]
        r = 4
        c = 6
        for b in column7: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="goldenrod1",
                      command=lambda text=b:  self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column8 = [
            ('Fe', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Ru', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Os', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Hs', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')

            # ('Fe', 'Iron', 'Atomic # = 26\nAtomic Weight = 55.85\nState = Solid\nCategory = Trans Metals'),
            # ('Ru', 'Ruthenium', 'Atomic # = 44\nAtomic Weight = 101.07\nState = Solid\nCategory = Trans Metals'),
            # ('Os', 'Osmium', 'Atomic # = 76\nAtomic Weight = 190.20\nState = Solid\nCategory = Trans Metals'),
            # ('Hs', 'Hassium', 'Atomic # = 108\nAtomic Weight = 265.00\nState = Synthetic\nCategory = Trans Metals')
            ]
        r = 4
        c = 7
        for b in column8: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="goldenrod1",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column9 = [
            ('Co', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Rh', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Ir', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Mt', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('Co', 'Cobalt', 'Atomic # = 27\nAtomic Weight = 58.93\nState = Solid\nCategory = Trans Metals'),
            # ('Rh', 'Rhodium', 'Atomic # = 45\nAtomic Weight = 102.91\nState = Solid\nCategory = Trans Metals'),
            # ('Ir', 'Iridium', 'Atomic # = 77\nAtomic Weight = 192.22\nState = Solid\nCategory = Trans Metals'),
            # ('Mt', 'Meitnerium', 'Atomic # = 109\nAtomic Weight = 266.00\nState = Synthetic\nCategory = Trans Metals')
            ]
        r = 4
        c = 8
        for b in column9: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="goldenrod1",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column10 = [
            ('Ni', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Pd', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Pt', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('Ni', 'Nickle', 'Atomic # = 28\nAtomic Weight = 58.70\nState = Solid\nCategory = Trans Metals'),
            # ('Pd', 'Palladium', 'Atomic # = 46\nAtomic Weight = 106.40\nState = Solid\nCategory = Trans Metals'),
            # ('Pt', 'Platinum', 'Atomic # = 78\nAtomic Weight = 195.09\nState = Solid\nCategory = Trans Metals')
            ]
        r = 4
        c = 9
        for b in column10: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="goldenrod1",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column11 = [
            ('Cu', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Ag', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Au', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('Cu', 'Copper', 'Atomic # = 29\nAtomic Weight = 63.55\nState = Solid\nCategory = Trans Metals'),
            # ('Ag', 'Silver', 'Atomic # = 47\nAtomic Weight = 107.97\nState = Solid\nCategory = Trans Metals'),
            # ('Au', 'Gold', 'Atomic # = 79\nAtomic Weight = 196.97\nState = Solid\nCategory = Trans Metals')
            ]
        r = 4
        c = 10
        for b in column11: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="goldenrod1",
                      command=lambda text=b:  self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column12 = [
            ('Zn', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Cd', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Hg', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')

            # ('Zn', 'Zinc', 'Atomic # = 30\nAtomic Weight = 65.37\nState = Solid\nCategory = Trans Metals'),
            # ('Cd', 'Cadmium', 'Atomic # = 48\nAtomic Weight = 112.41\nState = Solid\nCategory = Trans Metals'),
            # ('Hg', 'Mercury', 'Atomic # = 80\nAtomic Weight = 200.59\nState = Liquid\nCategory = Trans Metals')
            ]
        r = 4
        c = 11
        for b in column12: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="goldenrod1",
                      command=lambda text=b:  self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column13_1 = [
            ('B', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('B', 'Boron', 'Atomic # = 5\nAtomic Weight = 10.81\nState = Solid\nCategory = Nonmetals')
            ]
        r = 2
        c = 12
        for b in column13_1: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="deeppink",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column13_2 = [
            ('Al', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Ga', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('In', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Ti', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('Al', 'Aluminum', 'Atomic # = 13\nAtomic Weight = 26.98\nState = Solid\nCategory = Other Metals'),
            # ('Ga', 'Gallium', 'Atomic # = 31\nAtomic Weight = 69.72\nState = Solid\nCategory = Other Metals'),
            # ('In', 'Indium', 'Atomic # = 49\nAtomic Weight = 69.72\nState = Solid\nCategory = Other Metals'),
            # ('Ti', 'Thallium', 'Atomic # = 81\nAtomic Weight = 204.37\nState = Solid\nCategory = Other Metals')
            ]
        r = 3
        c = 12
        for b in column13_2: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="mediumpurple1",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column14_1 = [
            ('C', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Si', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('C', 'Carbon', 'Atomic # = 6\nAtomic Weight = 12.01\nState = Solid\nCategory = Nonmetals'),
            # ('Si', 'Silicon', 'Atomic # = 14\nAtomic Weight = 28.09\nState = Solid\nCategory = Nonmetals')
            ]
        r = 2
        c = 13
        for b in column14_1: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="deeppink",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column14_2 = [
            ('Ge', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Sn', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Pb', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('Ge', 'Germanium', 'Atomic # = 32\nAtomic Weight = 72.59\nState = Solid\nCategory = Other Metals'),
            # ('Sn', 'Tin', 'Atomic # = 50\nAtomic Weight = 118.69\nState = Solid\nCategory = Other Metals'),
            # ('Pb', 'Lead', 'Atomic # = 82\nAtomic Weight = 207.20\nState = Solid\nCategory = Other Metals')
            ]
        r = 4
        c = 13
        for b in column14_2: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="mediumpurple1",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column15_1 = [
            ('N', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('P', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('As', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('N', 'Nitrogen', 'Atomic # = 7\nAtomic Weight = 14.01\nState = Gas\nCategory = Nonmetals'),
            # ('P', 'Phosphorus', 'Atomic # = 15\nAtomic Weight = 30.97\nState = Solid\nCategory = Nonmetals'),
            # ('As', 'Arsenic', 'Atomic # = 33\nAtomic Weight = 74.92\nState = Solid\nCategory = Nonmetals')
            ]
        r = 2
        c = 14
        for b in column15_1: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="deeppink",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column15_2 = [
            ('Sb', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Bi', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('Sb', 'Antimony', 'Atomic # = 51\nAtomic Weight = 121.75\nState = Solid\nCategory = Other Metals'),
            # ('Bi', 'Bismuth', 'Atomic # = 83\nAtomic Weight = 208.98\nState = Solid\nCategory = Other Metals')
            ]
        r = 5
        c = 14
        for b in column15_2: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="mediumpurple1",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column16_1 = [
            ('O', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('S', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Se', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Te', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('O', 'Oxygen', 'Atomic # = 8\nAtomic Weight = 15.99\nState = Gas\nCategory = Nonmetals'),
            # ('S', 'Sulfur', 'Atomic # = 16\nAtomic Weight = 32.06\nState = Solid\nCategory = Nonmetals'),
            # ('Se', 'Selenium', 'Atomic # = 34\nAtomic Weight = 78.96\nState = Solid\nCategory = Nonmetals'),
            # ('Te', 'Tellurium', 'Atomic # = 52\nAtomic Weight = 127.60\nState = Solid\nCategory = Nonmetals')
            ]
        r = 2
        c = 15
        for b in column16_1: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="deeppink",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column16_2 = [
            ('Po', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('Po', 'Polonium', 'Atomic # = 84\nAtomic Weight = 209.00\nState = Solid\nCategory = Other Metals')
            ]
        r = 6
        c = 15
        for b in column16_2: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="mediumpurple1",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column17 = [
            ('F', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Cl', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Br', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('I', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('At', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('F', 'Fluorine', 'Atomic # = 9\nAtomic Weight = 18.99\nState = Gas\nCategory = Nonmetals'),
            # ('Cl', 'Chlorine', 'Atomic # = 17\nAtomic Weight = 35.45\nState = Gas\nCategory = Nonmetals'),
            # ('Br', 'Bromine', 'Atomic # = 35\nAtomic Weight = 79.90\nState = Liquid\nCategory = Nonmetals'),
            # ('I', 'Iodine', 'Atomic # = 53\nAtomic Weight = 126.90\nState = Solid\nCategory = Nonmetals'),
            # ('At', 'Astatine', 'Atomic # = 85\nAtomic Weight = 210.00\nState = Solid\nCategory = Nonmetals')
            ]
        r = 2
        c = 16
        for b in column17: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="deeppink",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        column18 = [
            ('He', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Ne', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Ar', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Kr', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Xe', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Rn', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('He', 'Helium', 'Atomic # = 2\nAtomic Weight = 4.00\nState = Gas\nCategory = Nobel Gases'),
            # ('Ne', 'Neon', 'Atomic # = 10\nAtomic Weight = 20.18\nState = Gas\nCategory = Nobel Gases'),
            # ('Ar', 'Argon', 'Atomic # = 18\nAtomic Weight = 39.95\nState = Gas\nCategory = Nobel Gases'),
            # ('Kr', 'Krypton', 'Atomic # = 36\nAtomic Weight = 83.80\nState = Gas\nCategory = Nobel Gases'),
            # ('Xe', 'Xenon', 'Atomic # = 54\nAtomic Weight = 131.30\nState = Gas\nCategory = Nobel Gases'),
            # ('Rn', 'Radon', 'Atomic # = 86\nAtomic Weight = 222.00\nState = Gas\nCategory = Nobel Gases')
            ]
        r = 1
        c = 17
        for b in column18: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="deepskyblue",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        self.fillerLine = tk.Label(self, text="")
        self.fillerLine.grid(row=10, column=0)

        lanthanide = [
            ('Ce', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \n Melting point = \n Electronic Configuration ='),
            ('Pr', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Nd', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Pm', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Sm', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Eu', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Gd', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Tb', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Dy', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Ho', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Er', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Tm', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Yb', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Lu', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('>| Ce', 'Cerium', 'Atomic # = 58\nAtomic Weight = 140.12\nState = Solid\nCategory = Trans Metals'),
            # ('Pr', 'Praseodymium', 'Atomic # = 59\nAtomic Weight = 140.91\nState = Solid\nCategory = Trans Metals'),
            # ('Nd', 'Neodymium', 'Atomic # = 60\nAtomic Weight = 144.24\nState = Solid\nCategory = Trans Metals'),
            # ('Pm', 'Promethium', 'Atomic # = 61\nAtomic Weight = 145.00\nState = Synthetic\nCategory = Trans Metals'),
            # ('Sm', 'Samarium', 'Atomic # = 62\nAtomic Weight = 150.40\nState = Solid\nCategory = Trans Metals'),
            # ('Eu', 'Europium', 'Atomic # = 63\nAtomic Weight = 151.96\nState = Solid\nCategory = Trans Metals'),
            # ('Gd', 'Gadolinium', 'Atomic # = 64\nAtomic Weight = 157.25\nState = Solid\nCategory = Trans Metals'),
            # ('Tb', 'Terbium', 'Atomic # = 65\nAtomic Weight = 158.93\nState = Solid\nCategory = Trans Metals'),
            # ('Dy', 'Dyprosium', 'Atomic # = 66\nAtomic Weight = 162.50\nState = Solid\nCategory = Trans Metals'),
            # ('Ho', 'Holmium', 'Atomic # = 67\nAtomic Weight = 164.93\nState = Solid\nCategory = Trans Metals'),
            # ('Er', 'Erbium', 'Atomic # = 68\nAtomic Weight = 167.26\nState = Solid\nCategory = Trans Metals'),
            # ('Tm', 'Thulium', 'Atomic # = 69\nAtomic Weight = 168.93\nState = Solid\nCategory = Trans Metals'),
            # ('Yb', 'Ytterbium', 'Atomic # = 70\nAtomic Weight = 173.04\nState = Solid\nCategory = Trans Metals'),
            # ('Lu', 'Lutetium', 'Atomic # = 71\nAtomic Weight = 174.97\nState = Solid\nCategory = Trans Metals')
            ]
        r = 11
        c = 3
        for b in lanthanide: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="green2",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            c += 1
            if c > 18: 
                c = 1
                r += 1

        actinide = [
            ('Th', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Pa', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('U', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Np', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Pu', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Am', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Cm', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Bk', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Cf', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Es', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Fm', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Md', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('No', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
            ('Lr', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration =')
            
            # ('>| Th', 'Thorium', 'Atomic # = 90\nAtomic Weight = 232.04\nState = Solid\nCategory = Trans Metals'),
            # ('Pa', 'Protactinium', 'Atomic # = 91\nAtomic Weight = 231.04\nState = Solid\nCategory = Trans Metals'),
            # ('U', 'Uranium', 'Atomic # = 92\nAtomic Weight = 238.03\nState = Solid\nCategory = Trans Metals'),
            # ('Np', 'Neptunium', 'Atomic # = 93\nAtomic Weight = 237.05\nState = Synthetic\nCategory = Trans Metals'),
            # ('Pu', 'Plutonium', 'Atomic # = 94\nAtomic Weight = 244.00\nState = Synthetic\nCategory = Trans Metals'),
            # ('Am', 'Americium', 'Atomic # = 95\nAtomic Weight = 243.00\nState = Synthetic\nCategory = Trans Metals'),
            # ('Cm', 'Curium', 'Atomic # = 96\nAtomic Weight = 247\nState = Synthetic\nCategory = Trans Metals'),
            # ('Bk', 'Berkelium', 'Atomic # = 97\nAtomic Weight = 247\nState = Synthetic\nCategory = Trans Metals'),
            # ('Cf', 'Californium', 'Atomic # = 98\nAtomic Weight = 247\nState = Synthetic\nCategory = Trans Metals'),
            # ('Es', 'Einsteinium', 'Atomic # = 99\nAtomic Weight = 252.00\nState = Synthetic\nCategory = Trans Metals'),
            # ('Fm', 'Fermium', 'Atomic # = 100\nAtomic Weight = 257.00\nState = Synthetic\nCategory = Trans Metals'),
            # ('Md', 'Mendelevium', 'Atomic # = 101\nAtomic Weight = 260.00\nState = Synthetic\nCategory = Trans Metals'),
            # ('No', 'Nobelium', 'Atomic # = 102\nAtomic Weight = 259\nState = Synthetic\nCategory = Trans Metals'),
            # ('Lr', 'Lawrencium', 'Atomic # = 103\nAtomic Weight = 262\nState = Synthetic\nCategory = Trans Metals')
            ]
        r = 12
        c = 3
        for b in actinide:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="green3",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            c += 1
            if c > 18: 
                c = 1
                r += 1

        reset = [
            ('Reset', 'Click on the Element to know more about it.', '')]
        r = 12
        c = 0
        for b in reset: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="darkslategrey",
                      fg="white",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7: 
                r = 1
                c += 1

        self.infoLine = tk.Label(self, text="", justify='left')
        self.infoLine.grid(row=1, column=1, columnspan=10, rowspan=4)



    # Replaces Label at the top with the name of whichever element button was pressed
    def name(self, text): 
        self.topLabel.config(text=text)

    # Displays information when button is pressed
    def info(self, text): 
        self.infoLine.config(text=text)
        img_show1()
        # img_paths = ["/home/thilaktp/Documents/Programming/Python/gui-perdiodic-table/img/h.jpg", "/home/thilaktp/Documents/Programming/Python/gui-perdiodic-table/img/image.jpg"]
        # img = cv2.imread(img_paths[0])
        # cv2.imshow('output', img)
        # cv2.waitKey(0)
        
      


# Creates an instance of 'app' class
def main():
    root = tk.Tk()
    a = App(root)
    a.grid(row=0, column=0, sticky='nsew') 
    a.mainloop()


if __name__ == "__main__": 
    main()
