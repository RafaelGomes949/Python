import random
import string
from tkinter import *
from tkinter import messagebox, ttk

from PIL import Image, ImageTk

cor1 = "#444466"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

janela = Tk()
janela.title('Gerador de senha')
janela.geometry('295x360')
janela.configure(bg=cor1)
janela.iconphoto(False, PhotoImage(file='lock.png'))


estilo = ttk.Style(janela)
estilo.theme_use('clam')

# divisao da tela
frame_cima = Frame(janela, width=295, height=50,
                   bg=cor2, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310,
                    bg=cor2, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# frame cima
img = Image.open('senha.png')
img = img.resize((30, 30), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT,
                 padx=10, relief='flat', anchor='nw', bg=cor2)
app_logo.place(x=2, y=0)

app_nome = Label(frame_cima, height=1, text='GERADOR DE SENHAS', width=20, compound=LEFT,
                 padx=0, relief='flat', anchor='nw', bg=cor2, fg=cor1, font=('Ivy 16 bold'))
app_nome.place(x=35, y=0)

app_linha = Label(frame_cima, height=1, text='', width=295, compound=LEFT,
                  padx=0, bg=cor4, relief='flat', anchor='nw', fg=cor1, font=('Ivy 1'))
app_linha.place(x=0, y=35)
# gerar senha


def criarsenha():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '[]{}()-*;,/_'

    global combinar
    combinar = None

    # condicao para maiscula

    if estado1.get() == alfa_maior:
        if combinar == None:
            combinar = alfa_maior
        else:
            combinar = combinar + alfa_maior
    else:
        pass

        # condicao para minuscula

    if estado2.get() == alfa_menor:
        if combinar == None:
            combinar = alfa_menor
        else:
            combinar = combinar + alfa_menor
    else:
        pass

        # condicao para numeros

    if estado3.get() == numeros:
        if combinar == None:
            combinar = numeros
        else:
            combinar = combinar + numeros
    else:
        pass

        # condicao para simbolos

    if estado4.get() == simbolos:
        if combinar == None:
            combinar = simbolos
        else:
            combinar = combinar + simbolos
    else:
        pass

    comprimento = int(spin.get())
    senha = ''.join(random.sample(combinar, comprimento))

    app_linha['text'] = senha
    print(senha)

    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo('sucesso', 'A senha foi copiada com sucesso')

    # botao copiar
    botao_copiar = app_info = Button(frame_baixo, height=2, command=copiar_senha,
                                     text='Copiar', width=7,
                                     bg=cor2, relief='raised', overrelief='solid', anchor='center', fg=cor1, font=('Ivy 10 bold'))
    botao_copiar.grid(row=0, column=1, sticky=NW,
                      padx=6, pady=7, columnspan=1)


# frame baixo
app_linha = Label(frame_baixo, height=2, text='- - -', width=20,
                  padx=0, bg=cor2, relief='solid', anchor='center', fg=cor1, font=('Ivy 12 bold'))
app_linha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_baixo, height=1, text='Número total de caracteres na senha',
                 padx=0, bg=cor2, relief='flat', anchor='nw', fg=cor1, font=('Ivy 10 bold'))
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)


alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '[]{}()-*;,/_'


frame_caract = Frame(frame_baixo, width=295, height=210,
                     bg=cor2, padx=0, relief='flat')
frame_caract.grid(row=3, column=0, sticky=NSEW, columnspan=3)


# Letras maiusculas
estado1 = StringVar()
estado1.set(False)
check_1 = Checkbutton(frame_caract, width=1, var=estado1,
                      onvalue=alfa_maior, offvalue='off', relief='flat', bg=cor2)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)

app_info = Label(frame_caract, height=1, text='ABC Letras maisculas',
                 padx=0, bg=cor2, relief='flat', anchor='nw', fg=cor1, font=('Ivy 10 bold'))
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)

# Letras minusculas
estado2 = StringVar()
estado2.set(False)
check_2 = Checkbutton(frame_caract, width=1, var=estado2,
                      onvalue=alfa_menor, offvalue='off', relief='flat', bg=cor2)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)

app_info = Label(frame_caract, height=1, text='abc Letras minusculas',
                 padx=0, bg=cor2, relief='flat', anchor='nw', fg=cor1, font=('Ivy 10 bold'))
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)

# Numeros
estado3 = StringVar()
estado3.set(False)
check_3 = Checkbutton(frame_caract, width=1, var=estado3,
                      onvalue=numeros, offvalue='off', relief='flat', bg=cor2)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)

app_info = Label(frame_caract, height=1, text='123 Números',
                 padx=0, bg=cor2, relief='flat', anchor='nw', fg=cor1, font=('Ivy 10 bold'))
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5)

# Simbolos
estado4 = StringVar()
estado4.set(False)
check_4 = Checkbutton(frame_caract, width=1, var=estado4,
                      onvalue=simbolos, offvalue='off', relief='flat', bg=cor2)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)

app_info = Label(frame_caract, height=1, text='Simbolos',
                 padx=0, bg=cor2, relief='flat', anchor='nw', fg=cor1, font=('Ivy 10 bold'))
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5)

# botao senha
botao_gerar_senha = app_info = Button(frame_baixo, height=1, command=criarsenha, text='Gerar Senha', width=34,
                                      bg=cor4, relief='flat', overrelief='solid', anchor='center', fg=cor2, font=('Ivy 10 bold'))
botao_gerar_senha.grid(row=5, column=0, sticky=NSEW,
                       padx=6, pady=11, columnspan=5)


janela.mainloop()
