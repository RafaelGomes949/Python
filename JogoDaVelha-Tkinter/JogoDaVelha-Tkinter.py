from tkinter import *
from tkinter import messagebox, ttk

janela = Tk()
janela.title('Jogo da velha')
janela.iconphoto(False, PhotoImage(file='velha.png'))

clicked = True
contador = 0


def desativar_b():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def checkvenceu():
    global vencedor
    vencedor = False

# checando X
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O X venceu!!")
        desativar_b()

    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O X venceu!!")
        desativar_b()

    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O X venceu!!")
        desativar_b()

    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b7.config(bg='red')
        b1.config(bg='red')
        b4.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O X venceu!!")
        desativar_b()

    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O X venceu!!")
        desativar_b()

    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O X venceu!!")
        desativar_b()

    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O X venceu!!")
        desativar_b()

    elif b3['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O X venceu!!")
        desativar_b()
    # checando O
    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O venceu!!")
        desativar_b()

    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O venceu!!")
        desativar_b()

    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O venceu!!")
        desativar_b()

    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b7.config(bg='red')
        b1.config(bg='red')
        b4.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O venceu!!")
        desativar_b()

    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O venceu!!")
        desativar_b()

    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O venceu!!")
        desativar_b()

    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O venceu!!")
        desativar_b()

    elif b3['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        vencedor = True
        messagebox.showinfo("Jogo da Velha", "O venceu!!")
        desativar_b()
    if contador == 9 and vencedor == False:
        messagebox.showinfo("Jogo da Velha", "Empate!!")


def b_click(b):
    global clicked, contador
    if b['text'] == " " and clicked == True:
        b['text'] = 'X'
        clicked = False
        contador += 1
        checkvenceu()

    elif b['text'] == " " and clicked == False:
        b['text'] = 'O'
        clicked = True
        contador += 1
        checkvenceu()

    else:
        messagebox.showerror(
            "Jogo da Velha", "Esse lugar já foi selecionado\n Por favor, selecione outro")


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global contador, clicked
    clicked = True
    contador = 0
    b1 = Button(janela, text=' ', font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b1.grid(row=0, column=0)

    b2 = Button(janela, text=' ', font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b2.grid(row=0, column=1)

    b3 = Button(janela, text=' ', font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
    b3.grid(row=0, column=2)

    b4 = Button(janela, text=' ', font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b4.grid(row=1, column=0)

    b5 = Button(janela, text=' ', font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b5.grid(row=1, column=1)

    b6 = Button(janela, text=' ', font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
    b6.grid(row=1, column=2)

    b7 = Button(janela, text=' ', font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b7.grid(row=2, column=0)

    b8 = Button(janela, text=' ', font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b8.grid(row=2, column=1)

    b9 = Button(janela, text=' ', font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b9))
    b9.grid(row=2, column=2)


# criando menu
select = Menu(janela)
janela.config(menu=select)

# opções menu
options_menu = Menu(select, tearoff=False)
select.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Começar outro jogo", command=reset)
reset()

janela.mainloop()
