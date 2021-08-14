 
import tkinter as tk

# App Class
class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.winfo_toplevel().title("[ Periodic Table of the Elements ]" )
        self.topLabel = tk.Label(self, text="Click on an element for more info.", font = 500)
        self.topLabel.grid(row=0, column=0, columnspan=18)

        
        # Names of Buttons in column 1
        column1 = [

            ('H', 'Hydrogen', 'Atomic No= 1\nAtomic Mass= 1.008 u\nAtomic Radius= 120 pm \nState = Gas\nCategory = Non Metal\nDensity= 0.00008988 g/cm³\nBoiling Point = 20.28 K\nMelting point = 13.81 K\nElectronic Configuration = 1s2\nYear Discovered= 1868'),
            ('Li', 'Lithium', 'Atomic No= 3\nAtomic Mass= 7.0 u\nAtomic Radius= 182 pm\nState Solid= \nCategory = Alkali Metal\nDensity= 0.534 g/cm³\nBoiling Point = 1615 K\nMelting point = 453.65 K \nElectronic Configuration = [He]2s1 \nYear Discovered= 1766'),
            ('Na', 'Sodium', 'Atomic No= 11\nAtomic Mass= 22.99u u\nAtomic Radius= 227 pm\nState = Solid\nCategory = Alkali Metal\nDensity= 0.97 g/cm³\nBoiling Point = 1156 K\nMelting point = 370.95 K\nElectronic Configuration = [Ne]3s1\nYear Discovered= 1807'),
            ('K', 'Potassium', 'Atomic No= 19\nAtomic Mass= 39.1 u\nAtomic Radius= 275 pm\nState = Solid\nCategory = Alkali Metal\nDensity= 0.89 g/cm³\nBoiling Point = 1032 K\nMelting point = 336.53 K\nElectronic Configuration = [Ar]4s1\nYear Discovered= 1807'),
            ('Rb', 'Rubudium', 'Atomic No= 37\nAtomic Mass= 85.47 u\nAtomic Radius= 303 pm\nState = Solid\nCategory = Alkali Metal\nDensity= 1.53 g/cm³\nBoiling Point = 961 K\nMelting point = 312.46 K\nElectronic Configuration = [Kr]5s1\nYear Discovered= 1861'),
            ('Cs', 'Cesium', 'Atomic No= 55\nAtomic Mass= 132.90 u\nAtomic Radius= 343 pm\nState = Solid\nCategory = Alkali Metal\nDensity= 1.93 g/cm³\nBoiling Point = 944 K\nMelting point = 301.59 K\nElectronic Configuration = [Xe]6s1\nYear Discovered= 1860'),
            ('Fr', 'Francium', 'Atomic No= 87\nAtomic Mass= 223.109 u\nAtomic Radius= 348 pm\nState = Solid\nCategory = Alkali Metal\nDensity= NA\nBoiling Point = NA\nMelting point = 300K\nElectronic Configuration = [Rn]7s1\nYear Discovered= 1939')
            
        
            ]
        
        r = 1
        c = 0
        count = 0
        

        for b in column1: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=4,
                      bg="firebrick1",
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
            ('B', 'Boron', 'Atomic No= 5\nAtomic Mass= 10.81 u\nAtomic Radius= 192 pm\nState = Solid\nCategory = Metalloid\nDensity= 2.37 g/cm³\nBoiling Point = 4273 K\nMelting point = 2348 K\nElectronic Configuration =[He]2s22p1 \nYear Discovered= 1808')
            
            
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
            ('Al', 'Aluminium', 'Atomic No= 13\nAtomic Mass= 26.98 u\nAtomic Radius= 184 pm\nState = Solid\nCategory = Post-Transition Metal\nDensity= 2.70 g/cm³\nBoiling Point = 2792 K\nMelting point = 933.43 K\nElectronic Configuration = [Ne]3s23p1 \nYear Discovered= Ancient'),
            ('Ga', 'Gallium', 'Atomic No= 31\nAtomic Mass= 69.72 u\nAtomic Radius= 187 pm\nState = Solid\nCategory = Post-Transition Metal\nDensity= 5.91 g/cm³\nBoiling Point = 2477 K\nMelting point = 302.91 K\nElectronic Configuration = [Ar]4s23d104p1\nYear Discovered= 1875'),
            ('In', 'Indium', 'Atomic No= 49\nAtomic Mass= 114.82 u\nAtomic Radius= 193 pm\nState = Solid\nCategory = Post-Transition Metal\nDensity= 7.31 g/cm³\nBoiling Point = 2345 K\nMelting point = 429.75 K\nElectronic Configuration = [Kr]5s24d105p1\nYear Discovered= 1863'),
            ('Tl', 'Thallium', 'Atomic No= 81\nAtomic Mass= 204.38 u u\nAtomic Radius= 196 pm\nState = Solid\nCategory = Post Transition Metal\nDensity= 11.8 g/cm³\nBoiling Point = 1746 K\nMelting point = 577K\nElectronic Configuration = [Xe]6s24f145d106p1\nYear Discovered= 1861')
            
            
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
            ('C', 'Carbon', 'Atomic No= 6\nAtomic Mass= 12.011 u\nAtomic Radius= 170 pm\nState = Solid\nCategory = Non Metal\nDensity= 2.2670 g/cm³\nBoiling Point = 4098 K \nMelting point = 3823 K\nElectronic Configuration = [He]2s22p2\nYear Discovered= Ancient'),
            ('Si', 'Silicon', 'Atomic No= 14\nAtomic Mass= 28.085 u\nAtomic Radius= 210 pm\nState = Solid\nCategory = Metalloid\nDensity= 2.3296 g/cm³\nBoiling Point = 3538 K\nMelting point = 1687 K\nElectronic Configuration = [Ne]3s23p2\nYear Discovered= 1854')
            
            
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
            ('Ge', 'Germanium', 'Atomic No= 32\nAtomic Mass= 72.63 u\nAtomic Radius= 211 pm\nState = Solid\nCategory = Metalloid\nDensity= 5.323 g/cm³\nBoiling Point = 3106 K\nMelting point = 1211.4 K\nElectronic Configuration = [Ar]4s23d104p2 \nYear Discovered= 1886'),
            ('Sn', 'Tin', 'Atomic No= 50\nAtomic Mass= 118.71 u\nAtomic Radius= 217 pm\nState = Solid\nCategory = Post-Transition Metal\nDensity= 7.287 g/cm³\nBoiling Point = 2875 K\nMelting point = 505.08 K\nElectronic Configuration = [Kr]5s24d105p2\nYear Discovered= Ancient'),
            ('Pb', 'Lead', 'Atomic No= 82\nAtomic Mass= 207.2 u\nAtomic Radius= 202 pm \nState = Solid\nCategory = Post-Transition Metal\nDensity= 11.342 g/cm³\nBoiling Point = 2022 K\nMelting point = 600.61 K\nElectronic Configuration = [Xe]6s24f145d106p2\nYear Discovered= Ancient')
            
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
            ('N', 'Nitrogen', 'Atomic No= 7\nAtomic Mass= 14.007 u\nAtomic Radius= 155 pm\nState = Gas\nCategory = Non Metal\nDensity= 0.0012506 g/cm³\nBoiling Point = 77.3 K\nMelting point = 63.15 K\nElectronic Configuration = [He]2s22p3\nYear Discovered= 1772'),
            ('P', 'Phosphorus', 'Atomic No= 15\nAtomic Mass= 30.97 u\nAtomic Radius= 180pm\nState = Solid\nCategory = Non Metal\nDensity= 1.82 g/cm³\nBoiling Point = 553.65 K\nMelting point = 317.3 K\nElectronic Configuration = [Ne]3s23p3\nYear Discovered= 1669'),
            ('As', 'Arsenic', 'Atomic No= 33\nAtomic Mass= 74.92 u\nAtomic Radius= 185 pm\nState = Solid\nCategory = Metalloid\nDensity= 5.776 g/cm³\nBoiling Point = 887 K\nMelting point = 1090 K\nElectronic Configuration = [Ar]4s23d104p3\nYear Discovered= Ancient')
            
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
            ('Sb', 'Antimony', 'Atomic No= 51\nAtomic Mass= 121.76 u\nAtomic Radius= 206 pm\nState = Solid\nCategory = Metalloid\nDensity= 6.685 g/cm³\nBoiling Point = 1860 K\nMelting point = 903.7 K\nElectronic Configuration = [Kr]5s24d105p3\nYear Discovered= Ancient'),
            ('Bi', 'Bismuth', 'Atomic No= 83\nAtomic Mass= 208.98 u\nAtomic Radius= 207 pm\nState = Solid\nCategory = Post-Transition Metal\nDensity= 9.807 g/cm³\nBoiling Point = 1837 K\nMelting point = 544.5 K\nElectronic Configuration = [Xe]6s24f145d106p3\nYear Discovered= 1753')
            
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
            ('O', 'Oxygen', 'Atomic No= 8\nAtomic Mass= 15.999 u\nAtomic Radius= 152 pm\nState = Gas\nCategory = Non Metal\nDensity= 0.001429 g/cm³\nBoiling Point = 90.2 K\nMelting point = 54.36 K\nElectronic Configuration = [He]2s22p4\nYear Discovered= 1774'),
            ('S', 'Sulphur', 'Atomic No= 16\nAtomic Mass= 32.07 u\nAtomic Radius= 180 pm\nState = Solid\nCategory = Non Metal\nDensity= 2.067 g/cm³\nBoiling Point = 717.75 K\nMelting point = 388.36 K\nElectronic Configuration = [Ne]3s23p4\nYear Discovered= Ancient'),
            ('Se', 'Selenium', 'Atomic No= 34\nAtomic Mass= 78.97 u\nAtomic Radius= 190 pm\nState = Solid\nCategory = Non Metal\nDensity= 4.809 g/cm³\nBoiling Point = 958 K\nMelting point = 493.65 K\nElectronic Configuration = [Ar]4s23d104p4\nYear Discovered= 1817'),
            ('Te', 'Tellurium', 'Atomic No= 52\nAtomic Mass= 127.6 u\nAtomic Radius= 206 pm\nState = Solid\nCategory = Metalloid\nDensity= 6.232 g/cm³\nBoiling Point = 1261 K\nMelting point = 722.66 K\nElectronic Configuration = [Kr]5s24d105p4 \nYear Discovered= 1782')
            
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
            ('Po', 'Polonium', 'Atomic No= 84\nAtomic Mass= 208.98 u\nAtomic Radius= 197 pm\nState = Solid\nCategory = Metalloid\nDensity= 9.32 g/cm³\nBoiling Point = 1235 K\nMelting point = 527 K\nElectronic Configuration = [Xe]6s24f145d106p4\nYear Discovered= 1898')
            
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
            ('F', 'Fluorine', 'Atomic No= 9\nAtomic Mass= 18.998 u\nAtomic Radius= 135 pm\nState = Gas\nCategory = Halogen\nDensity= 0.001696 g/cm³\nBoiling Point = 85.03 K\nMelting point = 53.5 K\nElectronic Configuration = [He]2s22p5\nYear Discovered= 1670'),
            ('Cl', 'Chlorine', 'Atomic No= 17\nAtomic Mass= 35.45 u\nAtomic Radius= 175 pm\nState = Gas\nCategory = Halogen\nDensity= 0.003214 g/cm³\nBoiling Point = 239.11 K\nMelting point = 171.65 K\nElectronic Configuration = [Ne]3s23p5\nYear Discovered= 1774'),
            ('Br', 'Bromine', 'Atomic No= 35\nAtomic Mass= 79.90 u\nAtomic Radius= 183 pm\nState = Liquid\nCategory = Halogen\nDensity= 3.11 g/cm³\nBoiling Point = 331.95 K\nMelting point = 265.95 K\nElectronic Configuration = [Ar]4s23d104p5\nYear Discovered= 1826'),
            ('I', 'Iodine', 'Atomic No= 53\nAtomic Mass= 126.904 u\nAtomic Radius= 198 pm\nState = Solid\nCategory = Halogen\nDensity= 4.93 g/cm³\nBoiling Point = 457.55 K\nMelting point = 386..85 K\nElectronic Configuration = [Kr]5s24d105p5\nYear Discovered= 1811'),
            ('At', 'Astatine', 'Atomic No= 85\nAtomic Mass= 209.98 u\nAtomic Radius= 202 pm\nState = Solid\nCategory = Halogen\nDensity= 7 g/cm³\nBoiling Point = NA\nMelting point = 575 K\nElectronic Configuration = [Xe]6s24f145d106p5\nYear Discovered= 1940')
            
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
            ('He', 'Helium', 'Atomic No= 2\nAtomic Mass= 4.0026 u\nAtomic Radius= 140 pm\nState = Gas\nCategory = Noble Gas\nDensity= 0.0001785 g/cm³\nBoiling Point = 4.22 K\nMelting point = 0.95 K\nElectronic Configuration = 1s2\nYear Discovered= 1868'),
            ('Ne', 'Neon', 'Atomic No= 10\nAtomic Mass= 20.18 u\nAtomic Radius= 154 pm\nState = Gas\nCategory = Noble Gas\nDensity= 0.0008999 g/cm³\nBoiling Point = 27.07 K\nMelting point = 24.56 K\nElectronic Configuration = [He]2s22p6\nYear Discovered= 1898'),
            ('Ar', 'Argon', 'Atomic No= 18\nAtomic Mass= 39.9 u\nAtomic Radius= 188 pm\nState = Gas\nCategory = Noble Gas\nDensity= 0.0017837 g/cm³\nBoiling Point = 87.3 K\nMelting point = 15.75 K\nElectronic Configuration = [Ne]3s23p6\nYear Discovered= 1894'),
            ('Kr', 'Krypton', 'Atomic No= 36\nAtomic Mass= 83.80 u\nAtomic Radius= 202 pm\nState = Gas\nCategory = Noble Gas\nDensity= 0.003733 g/cm³\nBoiling Point = 119.93 K\nMelting point = 115.79 K\nElectronic Configuration = [Ar]4s23d104p6\nYear Discovered= 1896'),
            ('Xe', 'Xenon', 'Atomic No= 54\nAtomic Mass= 131.29 u\nAtomic Radius= 216 pm\nState = Gas\nCategory = Noble Gas\nDensity= 0.005887 g/cm³\nBoiling Point = 165.03 K\nMelting point = 161.63 K\nElectronic Configuration = [Kr]5s24d105p6\nYear Discovered= 1898'),
            ('Rn', 'Radon', 'Atomic No= 86\nAtomic Mass= 222.0175 u\nAtomic Radius= 220 pm\nState = Gas\nCategory = Noble Gas\nDensity= 0.00973 g/cm³\nBoiling Point = 211.45 K\nMelting point = 202 K\nElectronic Configuration = [Xe]6s24f145d106p6\nYear Discovered= 1900')
            
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
            ('>| Ce', 'Cerium', 'Atomic No= 58\nAtomic Mass= 140.12 u\nAtomic Radius= 235 pm\nState = Solid\nCategory = Lanthanide\nDensity= 6.770 g/cm³\nBoiling Point = 3697 K\n Melting point = 1071 K\n Electronic Configuration = [Xe]6s24f15d1\nYear Discovered= 1803'),
            ('Pr', 'Praseodymium', 'Atomic No= 59\nAtomic Mass= 140.90 u\nAtomic Radius= 239 pm\nState = Solid\nCategory = Lanthanide\nDensity= 6.77 g/cm³\nBoiling Point = 3793 K\nMelting point = 1204 K\nElectronic Configuration = [Xe]6s24f3\nYear Discovered= 1885'),
            ('Nd', 'Neodymium', 'Atomic No= 60\nAtomic Mass= 144.24 u\nAtomic Radius= 229 pm\nState = Solid\nCategory = Lanthanide\nDensity= 7.01 g/cm³\nBoiling Point = 3347 K\nMelting point = 1294 K \nElectronic Configuration = [Xe]6s24f4\nYear Discovered= 1885'),
            ('Pm', 'Prothemium', 'Atomic No= 61\nAtomic Mass= 144.91 u\nAtomic Radius= 236 pm\nState = Solid\nCategory = Lanthanide\nDensity= 7.26 g/cm³\nBoiling Point = 3271 K\nMelting point = 1315 K\nElectronic Configuration = [Xe]6s24f5\nYear Discovered= 1945'),
            ('Sm', 'Samarium', 'Atomic No= 62\nAtomic Mass= 150.4 u\nAtomic Radius= 229 pm\nState = Solid \nCategory = Lanthanide\nDensity= 7.52 g/cm³\nBoiling Point = 2067 K\nMelting point = 1347 K\nElectronic Configuration = [Xe]6s24f6\nYear Discovered= 1879'),
            ('Eu', 'Europium', 'Atomic No= 63\nAtomic Mass= 151.96 u\nAtomic Radius= 233 pm\nState = Solid\nCategory = Lanthanide\nDensity= 5.24 g/cm³\nBoiling Point = 1802 K\nMelting point = 1095 K\nElectronic Configuration = [Xe]6s24f7\nYear Discovered= 1901'),
            ('Gd', 'Gadolinium', 'Atomic No= 64\nAtomic Mass= 157.2 u\nAtomic Radius= 237 pm\nState = Solid\nCategory = Lanthanide\nDensity= 7.90 g/cm³\nBoiling Point = 3546 K\nMelting point = 1586 K\nElectronic Configuration = [Xe]6s24f75d1\nYear Discovered= 1880'),
            ('Tb', 'Terbium', 'Atomic No= 65\nAtomic Mass= 158.92 u\nAtomic Radius= 221 pm\nState = Solid\nCategory = Lanthanide\nDensity= 8.23 g/cm³\nBoiling Point = 3503 K\nMelting point = 1629 K\nElectronic Configuration = [Xe]6s24f9\nYear Discovered= 1843'),
            ('Dy', 'Dysprosium', 'Atomic No= 66\nAtomic Mass= 162.5 u\nAtomic Radius= 229 pm\nState = Solid\nCategory = Lanthanide\nDensity= 8.55 g/cm³\nBoiling Point = 2840 K\nMelting point = 1685 K\nElectronic Configuration = [Xe]6s24f10\nYear Discovered= 1886'),
            ('Ho', 'Holium', 'Atomic No= 67\nAtomic Mass= 164.93 u\nAtomic Radius= 216 pm\nState = Solid\nCategory = Lanthanide\nDensity= 8.80 g/cm³\nBoiling Point = 2973 K\nMelting point = 1747 K\nElectronic Configuration = [Xe]6s24f11\nYear Discovered= 1878'),
            ('Er', 'Erbium', 'Atomic No= 68\nAtomic Mass= 167.26 u\nAtomic Radius= 235 pm\nState = Solid\nCategory = Lanthanide\nDensity= 9.07 g/cm³\nBoiling Point = 3141 K\nMelting point = 1802 K\nElectronic Configuration = [Xe]6s24f12\nYear Discovered= 1843'),
            ('Tm', 'Thulium', 'Atomic No= 69\nAtomic Mass= 168.93 u\nAtomic Radius= 227 pm\nState = Solid\nCategory = Lanthanide\nDensity= 9.32 g/cm³\nBoiling Point = 2223 K\nMelting point = 1818 K\nElectronic Configuration = [Xe]6s24f13\nYear Discovered= 1879'),
            ('Yb', 'Ytterbium', 'Atomic No= 70\nAtomic Mass= 173 u\nAtomic Radius= 242 pm\nState = Solid\nCategory = Lanthanide\nDensity= 6.90 g/cm³\nBoiling Point = 1469 K\nMelting point = 1092 K\nElectronic Configuration = [Xe]6s24f14\nYear Discovered= 1878'),
            ('Lu', 'Lutetium', 'Atomic No= 71\nAtomic Mass= 174.96 u\nAtomic Radius= 221 pm\nState = Solid\nCategory = Lanthanide\nDensity= 9.84 g/cm³\nBoiling Point = 3675 K\nMelting point = 1936 K\nElectronic Configuration = [Xe]6s24f145d1\nYear Discovered= 1907')
            
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
            ('>| Th', 'Thorium', 'Atomic No= 90\nAtomic Mass= 232.03 u\nAtomic Radius= 237 pm\nState = Solid\nCategory = Actinide\nDensity= 11.72 g/cm³\nBoiling Point = 5061 K\nMelting point = 2023 K\nElectronic Configuration = [Rn]7s26d2\nYear Discovered= 1828'),
            ('Pa', 'Protactinium', 'Atomic No= 91\nAtomic Mass= 231.035 u\nAtomic Radius= 243 pm\nState = Solid\nCategory = Actinide\nDensity= 15.37 g/cm³\nBoiling Point = NA\nMelting point = 1845 K\nElectronic Configuration = [Rn]7s25f26d1\nYear Discovered= 1913'),
            ('U',  'Uranium', 'Atomic No= 92\nAtomic Mass= 238.028 u\nAtomic Radius= 240 pm\nState = Solid\nCategory = Actinide\nDensity= 18.95 g/cm³\nBoiling Point = 4404 K\nMelting point = 1408 K\nElectronic Configuration = [Rn]7s25f36d1\nYear Discovered= 1789'),
            ('Np', 'Neptunium', 'Atomic No= 93\nAtomic Mass= 237.04 u\nAtomic Radius= 221 pm\nState = Solid\nCategory = Actinide\nDensity= 20.25 g/cm³\nBoiling Point = 4175 K\nMelting point = 917 K\nElectronic Configuration = [Rn]7s25f46d1\nYear Discovered= 1940'),
            ('Pu', 'Plutonium', 'Atomic No= 94\nAtomic Mass= 244.06 u\nAtomic Radius= 243 pm\nState = Solid\nCategory = Actinide\nDensity= 19.84 g/cm³\nBoiling Point = 3501 K\nMelting point = 913 K\nElectronic Configuration = [Rn]7s25f6\nYear Discovered= 1940'),
            ('Am', 'Americium', 'Atomic No= 95\nAtomic Mass= 243.06 u\nAtomic Radius= 244 pm\nState = Solid\nCategory = Actinide\nDensity= 13.69 g/cm³\nBoiling Point = 2284 K\nMelting point = 1449 K\nElectronic Configuration = [Rn]7s25f7\nYear Discovered= 1944'),
            ('Cm', 'Curium', 'Atomic No= 96\nAtomic Mass= 247.07 u\nAtomic Radius= 245 pm\nState = Solid\nCategory = Actinide\nDensity= 13.51 g/cm³\nBoiling Point = 3400 K\nMelting point = 1618 K\nElectronic Configuration = [Rn]7s25f76d1\nYear Discovered= 1944'),
            ('Bk', 'Berkelium', 'Atomic No= 97\nAtomic Mass= 247.07 u\nAtomic Radius= 244 pm\nState = Solid\nCategory = Actinide\nDensity= 14 g/cm³\nBoiling Point = NA\nMelting point = 1323 K\nElectronic Configuration = [Rn]7s25f9\nYear Discovered= 1949'),
            ('Cf', 'Californium', 'Atomic No= 98\nAtomic Mass= 251.07 u\nAtomic Radius= 245 pm\nState = Solid\nCategory = Actinide\nDensity= NA\nBoiling Point = NA\nMelting point = 1173 K\nElectronic Configuration = [Rn]7s25f10\nYear Discovered=1950'),
            ('Es', 'Einsteinium', 'Atomic No= 99\nAtomic Mass= 252.08 u\nAtomic Radius= 245 pm\nState = Solid\nCategory = Actinide\nDensity= NA\nBoiling Point = NA\nMelting point = 1132 K\nElectronic Configuration = [Rn]7s25f11\nYear Discovered= 1952'),
            ('Fm', 'Fermium', 'Atomic No= 100\nAtomic Mass= 257.09 u\nAtomic Radius= NA\nState = Solid\nCategory = Actinide\nDensity= \nBoiling Point = NA\nMelting point = 1800 K\nElectronic Configuration = [Rn]5f127s2\nYear Discovered= 1952'),
            ('Md', 'Mendelevium', 'Atomic No= 101\nAtomic Mass= 258.09 u\nAtomic Radius= NA\nState = Solid\nCategory = Actinide\nDensity= NA\nBoiling Point = NA\nMelting point = 1100 K\nElectronic Configuration = [Rn]7s25f13\nYear Discovered= 1955'),
            ('No', 'Nobelium', 'Atomic No= 102\nAtomic Mass= 259.10 u\nAtomic Radius= NA\nState = Solid\nCategory = Actinide\nDensity= NA\nBoiling Point = NA\nMelting point = 1100K\nElectronic Configuration = [Rn]7s25f14\nYear Discovered= 1957'),
            ('Lr', 'Lawrencium', 'Atomic No= 103\nAtomic Mass= 266.12 u\nAtomic Radius= NA\nState = Solid\nCategory = Actinide\nDensity= NA\nBoiling Point = NA\nMelting point = 1900 K\nElectronic Configuration = [Rn]7s25f146d1\nYear Discovered= 1961')
            
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
# A Reset Button to reset the display values
        reset = [
            ('Reset', 'Click on an element for more info.', '')]
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
        
      


# The Main Function
def main():
    root = tk.Tk()
    a = App(root)
    a.grid(row=0, column=0, sticky='nsew') 
    a.mainloop()


if __name__ == "__main__": 
    main()
