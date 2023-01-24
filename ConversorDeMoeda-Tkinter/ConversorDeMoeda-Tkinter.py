
import json
from tkinter import *
from tkinter import Tk, ttk

import requests
from PIL import Image, ImageTk

cor0 = "#FFFFFF"  # branco
cor1 = "#DC143C"  # supervermelho
cor2 = "#EB5D51"  # vermelho


window = Tk()
window.title('Conversor de Moeda')
window.geometry('300x320')
window.iconphoto(False, PhotoImage(file='coin.png'))
window.configure(bg=cor0)
window.resizable(height=FALSE, width=FALSE)

top = Frame(window, width=300, height=60, bg=cor1)
top.grid(row=0, column=0)


main = Frame(window, width=300, height=260, bg=cor0)
main.grid(row=1, column=0)

# conversor


def conversor():

    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    moeda_1 = combo1.get()
    moeda2 = combo2.get()
    amount = value.get()

    querystring = {"from": moeda_1, "to": moeda2, "amount": amount}

    if moeda2 == 'USD':
        simbolo = '$'

    elif moeda2 == 'INR':
        simbolo = '₹'

    elif moeda2 == 'BRL':
        simbolo = 'R$'

    elif moeda2 == 'EUR':
        simbolo = '€'

    elif moeda2 == 'CAD':
        simbolo = 'CA $'

    headers = {
        "X-RapidAPI-Key": "d0eb503632mshd0751a077c16f28p14d750jsncb991f80ca32",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    dinheiro_convertido = data['result']['convertedAmount']
    formatado = simbolo + " {:,.2f}".format(dinheiro_convertido)

    result['text'] = formatado
    print(dinheiro_convertido, formatado)


# cima
img = Image.open('Gold_coin.png')
img = img.resize((40, 40))
img = ImageTk.PhotoImage(img)

app_nome = Label(top, image=img, text='Conversor de Moeda', height=5, compound=LEFT,
                 padx=10, pady=30, anchor=CENTER, bg=cor1, fg=cor0, font=('Arial 16 bold'))
app_nome.place(x=0, y=0)

# main
result = Label(main, text='', height=2, width=16,
               pady=7, relief='solid', anchor=CENTER, bg=cor2, fg=cor0, font=('Ivy 16 bold'))
result.place(x=50, y=10)

currency = ['BRL', 'CAD', 'EUR', 'INR', 'USD']

# de
moeda1 = Label(main, text='De', height=1, width=8,
               relief='flat', anchor=NW, bg=cor0, fg=cor1, font=('Ivy 10 bold'))
moeda1.place(x=48, y=90)

combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo1['value'] = (currency)
combo1.place(x=50, y=115)

# para
moeda2 = Label(main, text='Para', height=1, width=8,
               relief='flat', anchor=NW, bg=cor0, fg=cor1, font=('Ivy 10 bold'))
moeda2.place(x=150, y=90)

combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo2['value'] = (currency)
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER,
              font=('Ivy 12 bold'), relief=SOLID)
value.place(x=50, y=155)

# baixo
button = Button(main, text="Converter", width=19, command=conversor, padx=5, height=1,
                bg=cor2, fg=cor0, font=('Ivy 12 bold'), relief=SOLID)
button.place(x=50, y=210)


window.mainloop()
