#pip install tkinter
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import webbrowser
#GUI

root = tk.Tk()
root.iconbitmap("Textures\icon.ico")
menubar = Menu(root, background="#16191f", foreground="white")
root.configure(bg="#005a75")
root.config(menu=menubar)
root.title("PyCurrency(Made By Ahmed Barakat)")
root.resizable(0,0)
def about():
    hi = Tk()
    hi.geometry("300x180")
    hi.title("About")
    hi.resizable(0,0)
    hi.configure(bg="#005a75")
    hi.iconbitmap("Textures\icon.ico")
    def github():
        webbrowser.open("https://www.github.com/ahmedbarakat2007")
    def myweb():
        webbrowser.open("https://ahmed-barakat.netlify.app/")
    
    Label(hi, text="",bg="#005a75").pack()
    Label(hi, text="PyConvertor", font='san-serif 14 bold',bg="#005a75",fg="white").pack()
    Label(hi, text="Version 1.5.0", font='san-serif 8 bold',bg="#005a75",fg="white").pack()
    Label(hi, text="Made by Ahmed Barakat", font='san-serif 10 bold',bg="#005a75",fg="white").pack()
    Label(hi, text="",bg="#005a75",borderwidth=0).pack()
    Button(hi, text = "Github", command= github,bg="#2b686e", fg="white", borderwidth=0).pack()
    Label(hi, text="",bg="#005a75",borderwidth=0).pack()
    Button(hi, text = "My Website", command= myweb,bg="#2b686e", fg="white", borderwidth=0).pack()
	
    hi.mainloop()

# create a menu
file_menu = Menu(menubar)
file_menu.add_command(
    label='About',
    command=about
)

file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="Menu",
    menu=file_menu
)

Tops = Frame(root, bg="#005a75", pady=0,padx=0, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)
img = Image.open('Textures\icon.png')
img = img.resize((75, 70))    
img = ImageTk.PhotoImage(img)
panel = Label(Tops, image=img,bg="#005a75")
panel.image = img
panel.grid()

headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='PyCurrency',bg="#005a75", fg='white',padx=20)
headlabel.grid()

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("From")
variable2.set("To")
#Function To For Real Time Currency Conversion

def RealTimeCurrencyConversion():
	from forex_python.converter import CurrencyRates
	c = CurrencyRates()

	from_currency = variable1.get()
	to_currency = variable2.get()

	if (Amount1_field.get() == ""):
		tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")

	elif (from_currency == "currency" or to_currency == "currency"):
		tkinter.messagebox.showinfo("Error !!",
									"Currency Not Selected.\n Please select FROM and TO Currency form menu.")

	else:
		new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
		tkinter.messagebox.showinfo("Result",
									str(new_amt) + " " + to_currency)

#clearing all the data entered by the user
def clear_all():
	Amount1_field.delete(0, tk.END)


CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR","EGP",'JPY','TRY']

root.configure(background="#005a75")
root.geometry("500x400")

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="",bg="#005a75", fg='white', padx=0, pady=2)
Label_1.grid(row=0, column=0, sticky=W)
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="",bg="#005a75", fg='white', padx=0, pady=2)
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="  Amount",bg="#005a75", fg='white')
label1.grid(row=2, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=0, pady=2,bg="#005a75", fg='white')
Label_1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="  From Currency",bg="#005a75", fg='white')
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="  To Currency",bg="#005a75", fg='white')
label1.grid(row=6, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=0, pady=2,bg="#005a75", fg='white')
Label_1.grid(row=7, column=0, sticky=W)
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=0, pady=2,bg="#005a75", fg='white')
Label_1.grid(row=5, column=0, sticky=W)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)

FromCurrency_option.grid(row=4, column=0, ipadx=15)
ToCurrency_option.grid(row=6, column=0, ipadx=23)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28)


Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Convert ",bg="#2b686e", fg='white',
				command=RealTimeCurrencyConversion, borderwidth=0)
Label_9.grid(row=9, column=0)
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=0, pady=2,bg="#005a75", fg='white')
Label_1.grid(row=10, column=0, sticky=W)
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=0, pady=2,bg="#005a75", fg='white')
Label_1.grid(row=11, column=0, sticky=W)

Tops.grid(row=0, column=0, sticky="NESW")
Tops.grid_rowconfigure(0, weight=1)
Tops.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


root.mainloop()



    
    
    