            # ('H', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \n Melting point = \n Electronic Configuration ='),
import tkinter as tk
# import cv2
# from PIL import Image, ImageTk
# import sys
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
            ('H', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= 120 pm \nState = Gas\nCategory = Non Metal\nDensity= 0.00008988 g/cm³\nBoiling Point = 20.28 K\nMelting point = 13.81 K\nElectronic Configuration = 1s2\nYear Discovered= 1868'),
            ('Li', 'Lithium', 'Atomic No= 3\nAtomic Mass= 7.0 u\nAtomic Radius= 182 pm\nState Solid= \nCategory = Alkali Metal\nDensity= 0.534 g/cm³\nBoiling Point = 1615 K\nMelting point = 453.65 K \nElectronic Configuration = [He]2s1 \nYear Discovered= 1766'),
            ('Na', 'Sodium', 'Atomic No= 11\nAtomic Mass= 22.99u u\nAtomic Radius= 227 pm\nState = Solid\nCategory = Alkali Metal\nDensity= 0.97 g/cm³\nBoiling Point = 1156 K\nMelting point = 370.95 K\nElectronic Configuration = [Ne]3s1\nYear Discovered= 1807'),
            ('K', 'Potassium', 'Atomic No= 19\nAtomic Mass= 39.1 u\nAtomic Radius= 275 pm\nState = Solid\nCategory = Alkali Metal\nDensity= 0.89 g/cm³\nBoiling Point = 1032 K\nMelting point = 336.53 K\nElectronic Configuration = [Ar]4s1\nYear Discovered= 1807'),
            ('Rb', 'Rubudium', 'Atomic No= 37\nAtomic Mass= 85.47 u\nAtomic Radius= 303 pm\nState = Solid\nCategory = Alkali Metal\nDensity= 1.53 g/cm³\nBoiling Point = 961 K\nMelting point = 312.46 K\nElectronic Configuration = [Kr]5s1\nYear Discovered= 1861'),
            ('Cs', 'Cesium', 'Atomic No= 55\nAtomic Mass= 132.90 u\nAtomic Radius= 343 pm\nState = Solid\nCategory = Alkali Metal\nDensity= 1.93 g/cm³\nBoiling Point = 944 K\nMelting point = 301.59 K\nElectronic Configuration = [Xe]6s1\nYear Discovered= 1860'),
            ('Fr', 'Francium', 'Atomic No= 87\nAtomic Mass= 223.109 u\nAtomic Radius= 348 pm\nState = Solid\nCategory = Alkali Metal\nDensity= NA\nBoiling Point = NA\nMelting point = 300K\nElectronic Configuration = [Rn]7s1\nYear Discovered= 1939')
            
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
               ('Be', 'Beryllium', 'Atomic No= 4\nAtomic Mass= 9.0123 u\nAtomic Radius= 153 pm\nState = Solid\nCategory = Alkaline Earth Metal\nDensity= 1.85 g/cm³\nBoiling Point = 2744 K\nMelting point = 1560 K\nElectronic Configuration = [He]2s2\nYear Discovered= 1797'),
               ('Mg', 'Magnesium', 'Atomic No= 12\nAtomic Mass= 24.305 u\nAtomic Radius= 173pm\nState = Solid\nCategory = Alkaline Earth Metal\nDensity= 1.74 g/cm³\nBoiling Point = 1363 K\nMelting point = 923 K\nElectronic Configuration = [Ne]3s2\nYear Discovered= 1755'),
               ('Ca', 'Calcium', 'Atomic No= 20\nAtomic Mass= 40.08 u\nAtomic Radius= 231 pm\nState = Solid\nCategory = Alkaline Earth Metal\nDensity= 1.55 g/cm³\nBoiling Point = 1757 K\nMelting point = 1115 K\nElectronic Configuration = [Ar]4s2\nYear Discovered= 1808'),
               ('Sr', 'Strontium', 'Atomic No= 38\nAtomic Mass= 87.6 u\nAtomic Radius= 249 pm\nState = Solid\nCategory = Alkaline Earth Metal\nDensity= 2.64 g/cm³\nBoiling Point = 1655 K\nMelting point = 1050 K\nElectronic Configuration = [Kr]5s2\nYear Discovered= 1790'),
               ('Ba', 'Barium', 'Atomic No= 56\nAtomic Mass= 137.33 u\nAtomic Radius= 268 pm\nState = Solid\nCategory = Alkaline Earth Metal\nDensity= 3.62 g/cm³\nBoiling Point = 2170 K\nMelting point = 1000 K \nElectronic Configuration = [Xe]6s2 \nYear Discovered= 1808'),
               ('Ra', 'Radium', 'Atomic No= 88\nAtomic Mass= 226.025 u\nAtomic Radius= 283 pm\nState = Solid\nCategory = Alkaline Earth Metal\nDensity= 5.5 g/cm³\nBoiling Point = 1413 K\nMelting point = 973 K\nElectronic Configuration = [Rn]7s2\nYear Discovered= 1898')
                         
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
            ('Sc', 'Scandium', 'Atomic No= 21\nAtomic Mass= 44.955 u\nAtomic Radius= 211 pm\nState = Solid\nCategory = Transition Metal\nDensity= 2.99 g/cm³\nBoiling Point = 3109 K \nMelting point = 1814 K\nElectronic Configuration = [Ar]4s23d1\nYear Discovered= 1879'),
            ('Y', 'Yttrium', 'Atomic No= 39\nAtomic Mass= 88.905 u\nAtomic Radius= 219 pm\nState = Solid\nCategory = Transition Metal\nDensity= 4.47 g/cm³\nBoiling Point = 3618 K\nMelting point = 1795 K\nElectronic Configuration = [Kr]5s24d1\nYear Discovered= 1794'),
            ('La >|', 'Lanthanum', 'Atomic No= 57\nAtomic Mass= 138.905 u\nAtomic Radius= 240 pm\nState = Solid\nCategory = Lanthanide\nDensity= 6.15 g/cm³\nBoiling Point = 3737 K\nMelting point = 1191 K\nElectronic Configuration = [Xe]6s25d1\nYear Discovered= 1839'),
            ('Ac >|', 'Actinium', 'Atomic No= 89\nAtomic Mass= 227.027 u\nAtomic Radius= 260 pm\nState = Solid\nCategory = Actinide\nDensity= 10.07 g/cm³\nBoiling Point = 3471 K\nMelting point = 1324 K\nElectronic Configuration = [Rn]7s26d1\nYear Discovered= 1899')

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
                
            ('Ti', 'Titanium', 'Atomic No= 22\nAtomic Mass= 47.87 u\nAtomic Radius= 187 pm\nState = Solid\nCategory = Transition Metal\nDensity= 4.5 g/cm³\nBoiling Point = 3560 K\nMelting point = 1941 K\nElectronic Configuration = [Ar]4s23d2 \nYear Discovered= 1791'),
            ('Zr', 'Zirconium', 'Atomic No= 40\nAtomic Mass= 91.22 u\nAtomic Radius= 186 pm\nState = Solid\nCategory = Transition Metal\nDensity= 6.52 g/cm³\nBoiling Point = 4682 K\nMelting point = 2128 K\nElectronic Configuration = [Kr]5s24d2\nYear Discovered= 1789'),
            ('Hf', 'Hafnium', 'Atomic No= 72\nAtomic Mass= 178.49 u\nAtomic Radius= 212 pm\nState = Solid\nCategory = Transition Metal\nDensity= 13.3 g/cm³\nBoiling Point = 4876 K\nMelting point = 2506 K\nElectronic Configuration = [Xe]6s24f145d2\nYear Discovered= 1923'),
            ('Rf', 'Rutherfordium', 'Atomic No= 104\nAtomic Mass= 267.122 u\nAtomic Radius= 267 pm\nState = Solid\nCategory = Transition Metal\nDensity= 23.2 g/cm³\nBoiling Point = 5773.15 K\nMelting point = 2373.15 K\nElectronic Configuration = [Rn]7s25f146d2\nYear Discovered= 1964')

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
            ('V', 'Vanadium', 'Atomic No= 23\nAtomic Mass= 50.94 u\nAtomic Radius= 179 pm\nState = Solid\nCategory = Transition Metal\nDensity= 6.0 g/cm³\nBoiling Point = 3680 K\nMelting point = 2183 K\nElectronic Configuration = [Ar]4s23d3 \nYear Discovered= 1801'),
            ('Nb', 'Niobium', 'Atomic No= 41\nAtomic Mass= 92.906 u\nAtomic Radius= 207 pm\nState = Solid\nCategory = Transition Metal\nDensity= 8.57 g/cm³\nBoiling Point = 5017 K\nMelting point = 2750 K\nElectronic Configuration = [Kr]5s14d4\nYear Discovered= 1801'),
            ('Ta', 'Tantalum', 'Atomic No= 73\nAtomic Mass= 180.947 u\nAtomic Radius= 217 pm\nState = Solid\nCategory = Transition Metal\nDensity= 16.4 g/cm³\nBoiling Point = 5731 K\nMelting point = 3290 K\nElectronic Configuration = [Xe]6s24f145d3\nYear Discovered= 1802'),
            ('Db', 'Dubnium', 'Atomic No= 105\nAtomic Mass= 262 u\nAtomic Radius= 268 pm\nState = Solid\nCategory = Transition Metal\nDensity= 29.3 g/cm3\nBoiling Point = NA\nMelting point = Na\nElectronic Configuration = [Rn]7s25f146d3\nYear Discovered= 1967')
            
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
            ('Cr', 'Chromium', 'Atomic No= 24\nAtomic Mass= 51.996 u\nAtomic Radius= 189 pm\nState = Solid\nCategory = Transition Metal\nDensity= 7.15 g/cm³\nBoiling Point = 2944 K\nMelting point = 2180 K\nElectronic Configuration = [Ar]3d54s1 \nYear Discovered= 1797'),
            ('Mo', 'Molybdenum', 'Atomic No= 42\nAtomic Mass= 96 u\nAtomic Radius= 209 pm\nState = Solid\nCategory = Transition Metal\nDensity= 10.2 g/cm³\nBoiling Point = 4912 K\nMelting point = 2896 K\nElectronic Configuration = [Kr]5s14d5\nYear Discovered= 1778'),
            ('W', 'Tungsten', 'Atomic No= 74\nAtomic Mass= 183.8 u\nAtomic Radius= 210 pm\nState = Solid\nCategory = Transition Metal\nDensity= 19.3 g/cm³\nBoiling Point = 5828 K\nMelting point = 3695 K\nElectronic Configuration = [Xe]6s24f145d4\nYear Discovered= 1783'),
            ('Sg', 'Seaborgium', 'Atomic No= 106\nAtomic Mass= 269.128 u\nAtomic Radius= 143pm\nState = Solid\nCategory = Transition Metal\nDensity= 35g/cm³\nBoiling Point = NA\nMelting point = NA\nElectronic Configuration = [Rn]7s25f146d4\nYear Discovered= 1974')
            
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
            ('Mn', 'Manganese', 'Atomic No= 25\nAtomic Mass= 54.93 u\nAtomic Radius= 197 pm\nState = Solid\nCategory = Transition Metal\nDensity= 7.3 g/cm³\nBoiling Point = 2334 K\nMelting point = 1519 K\nElectronic Configuration = [Ar]4s23d5 \nYear Discovered= 1774'),
            ('Tc', 'Technetium', 'Atomic No= 43\nAtomic Mass= 96.90 u\nAtomic Radius= 209 pm\nState = Solid\nCategory = Transtion Metal\nDensity= 11 g/cm³\nBoiling Point = 4538 K\nMelting point = 2430 K\nElectronic Configuration = [Kr]5s24d5\nYear Discovered= 1937'),
            ('Re', 'Rhenium', 'Atomic No= 75\nAtomic Mass= 186.21 u\nAtomic Radius= 217 pm\nState = Solid\nCategory = Transition Metal\nDensity= 20.8 g/cm³\nBoiling Point = 5869 K\nMelting point = 3459 K\nElectronic Configuration = [Xe]6s24f145d5\nYear Discovered= 1925'),
            ('Bh', 'Bohrium', 'Atomic No= 107\nAtomic Mass= 270.13 u\nAtomic Radius= 141 pm\nState = Solid\nCategory = Transiton Metal\nDensity= 37 g/cm³\nBoiling Point = NA\nMelting point = NA\nElectronic Configuration = [Rn]7s25f146d5\nYear Discovered= 1976')
            
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
            ('Fe', 'Iron', 'Atomic No= 26\nAtomic Mass= 55.84 u\nAtomic Radius= 194 pm\nState = Solid\nCategory = Transition Metal\nDensity= 7.874 g/cm³\nBoiling Point = 3134 K\nMelting point = 1811 K\nElectronic Configuration = [Ar]4s23d6\nYear Discovered= Ancient'),
            ('Ru', 'Ruthenium', 'Atomic No= 44\nAtomic Mass= 101.1 u\nAtomic Radius= 207 pm\nState = Solid\nCategory = Transition Metal\nDensity= 12.1 g/cm³\nBoiling Point = 4423 K\nMelting point = 2607 K\nElectronic Configuration = [Kr]5s14d7\nYear Discovered= 1827'),
            ('Os', 'Osmium', 'Atomic No= 76\nAtomic Mass= 190.2 u\nAtomic Radius= 216 pm\nState = Solid\nCategory = Transition Metal\nDensity= 22.57 g/cm³\nBoiling Point = 5285 K\nMelting point = 3306 K\nElectronic Configuration = [Xe]6s24f145d6\nYear Discovered= 1803'),
            ('Hs', 'Hassium', 'Atomic No= 108\nAtomic Mass= 269.13 u\nAtomic Radius= 134 pm\nState = Solid\nCategory = Transition Metal\nDensity= 41 g/cm³\nBoiling Point = NA\nMelting point = NA\nElectronic Configuration = [Rn]7s25f146d6\nYear Discovered= 1984')

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
            ('Co', 'Cobalt', 'Atomic No= 27\nAtomic Mass= 58.93 u\nAtomic Radius= 192 pm\nState = Solid\nCategory = Transition Metal\nDensity= 8.86 g/cm³\nBoiling Point = 3200 K\nMelting point = 1768 K\nElectronic Configuration = [Ar]4s23d7\nYear Discovered= 1735'),
            ('Rh', 'Rhodium', 'Atomic No= 45\nAtomic Mass= 102.90 u\nAtomic Radius= 195 pm\nState = Solid\nCategory = Transition Metal\nDensity= 12.4 g/cm³\nBoiling Point = 3968 K\nMelting point = 2237 K\nElectronic Configuration = [Kr]5s14d8\nYear Discovered= 1803'),
            ('Ir', 'Iridium', 'Atomic No= 77\nAtomic Mass= 192.22 u\nAtomic Radius= 202 pm\nState = Solid\nCategory = Transition Metal\nDensity= 22.42 g/cm³\nBoiling Point = 4701 K\nMelting point = 2719 K\nElectronic Configuration = [Xe]6s24f145d7\nYear Discovered= 1803'),
            ('Mt', 'Meitnerium', 'Atomic No= 109\nAtomic Mass= 227.15 u\nAtomic Radius= 129\nState = Solid\nCategory = Transition Metal\nDensity= 37.4 g/cm³\nBoiling Point = NA\nMelting point = NA\nElectronic Configuration = [Rn]7s25f146d7\nYear Discovered= 1982')
            
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
            ('Ni', 'Nickel', 'Atomic No= 28\nAtomic Mass= 58.69 u\nAtomic Radius= 163 pm\nState = Solid\nCategory = Transition Metal\nDensity= 8.912 g/cm³\nBoiling Point = 3186 K\nMelting point = 1728 K\nElectronic Configuration = [Ar]4s23d8 \nYear Discovered= 1751'),
            ('Pd', 'Palladium', 'Atomic No= 46\nAtomic Mass= 106.4 u\nAtomic Radius= 202 pm\nState = Solid\nCategory = Transition Metal\nDensity= 12.0 g/cm³\nBoiling Point = 3236 K\nMelting point = 1828.05 K\nElectronic Configuration = [Kr]4d10\nYear Discovered= 1803'),
            ('Pt', 'Platinum', 'Atomic No= 78\nAtomic Mass= 195.08 u\nAtomic Radius= 209 pm\nState = Solid\nCategory = Transition Metal\nDensity= 21.46 g/cm³\nBoiling Point = 4098 K\nMelting point = 2041.55 K\nElectronic Configuration = [Xe]6s14f145d9\nYear Discovered= 1735')
            
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
            ('Cu', 'Copper', 'Atomic No= 29\nAtomic Mass= 63.55 u\nAtomic Radius= 140 pm\nState = Solid\nCategory = Transition Metal\nDensity= 8.933 g/cm³\nBoiling Point = 2835 K\nMelting point = 1357.77 K\nElectronic Configuration = [Ar]4s13d10\nYear Discovered= Ancient'),
            ('Ag', 'Silver', 'Atomic No= 47\nAtomic Mass= 107.86 u\nAtomic Radius= 172 pm\nState = Solid\nCategory = Transition Metal\nDensity= 10.501 g/cm³\nBoiling Point = 2435 K\nMelting point = 1234.93 K\nElectronic Configuration = [Kr]5s14d10\nYear Discovered= Ancient'),
            ('Au', 'Gold', 'Atomic No= 79\nAtomic Mass= 196.96 u\nAtomic Radius= 166 pm\nState = Solid\nCategory = Transition Metal\nDensity= 19.28 g/cm³\nBoiling Point = 3129 K\nMelting point = 1337.33K\nElectronic Configuration = [Xe]6s14f145d10\nYear Discovered= Ancient')
            
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
            ('Zn', 'Zinc', 'Atomic No= 30\nAtomic Mass= 65.4 u\nAtomic Radius= 139 pm\nState = Solid\nCategory = Transition Metal\nDensity= 7.134 g/cm³\nBoiling Point = 1180 K\nMelting point = 692.69 K\nElectronic Configuration =[Ar]4s23d10 \nYear Discovered= 1746'),
            ('Cd', 'Cadmium', 'Atomic No= 48\nAtomic Mass= 112.41 u\nAtomic Radius= 158 pm\nState = Solid\nCategory = Transition Metal\nDensity= 8.69 g/cm³\nBoiling Point = 1040 K\nMelting point = 594.22 K\nElectronic Configuration = [Kr]5s24d10 \nYear Discovered= 1817'),
            ('Hg', 'Mercury', 'Atomic No= 80\nAtomic Mass= 200.59 u\nAtomic Radius= 209 pm\nState = Liquid\nCategory = Transition Metal\nDensity= 13.5336 g/cm³\nBoiling Point = 629.88 K\nMelting point = 234.32 K\nElectronic Configuration = [Xe]6s24f145d10 \nYear Discovered= Ancient')

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
            ('>| Ce', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \n Melting point = \n Electronic Configuration ='),
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
            ('>| Th', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= \nState = Gas\nCategory = Alkali Metals\nDensity=\nBoiling Point = \nMelting point = \nElectronic Configuration ='),
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
        self.infoLine.grid(row=0, column=0, columnspan=10, rowspan=4)



    # Replaces Label at the top with the name of whichever element button was pressed
    def name(self, text): 
        self.topLabel.config(text=text)

    # Displays information when button is pressed
    def info(self, text): 
        self.infoLine.config(text=text)
        # img_show1()
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
