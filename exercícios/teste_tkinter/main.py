from tkinter import *
from PIL import Image, ImageTk

class Botao(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, width='70', relief='raised', bd=2, bg='#202020', activebackground='#202020', highlightcolor='#202020', highlightbackground='black', command= lambda: pressionaBotao(self))
        self.__isPressed = False
    
    def reseta(self):
        self.config(relief='raised', bg='#202020', activebackground='#202020')
        self.__isPressed = False
    
    def isPressed(self):
        return self.__isPressed

    def setIsPressed(self):
        self.__isPressed = True

def pressionaBotao(botao):
    botaoCabelo.reseta()
    botaoFace.reseta()
    botaoTorso.reseta()
    botaoPerna.reseta()
    botao.config(relief='sunken', bg='#161616', activebackground='#161616')
    botao.setIsPressed()

def limitaEntrada(*args):
    aux = nome.get()
    if len(aux) > 16:
        nome.set(aux[:16])

def percorreCabide(direita):
    global indiceCabelo
    if botaoCabelo.isPressed():
        if direita:
            try:
                indiceCabelo += 1
                vestir(cabideCabelo[indiceCabelo], 148, 18)
            except IndexError:
                indiceCabelo = 0
                vestir(None)
        else:
            if indiceCabelo-1 >= 0:
                indiceCabelo -= 1
                vestir(cabideCabelo[indiceCabelo], 148, 18)
            else:
                indiceCabelo = len(cabideCabelo)-1
                vestir(cabideCabelo[indiceCabelo], 148, 18)

def vestir(item, x=0, y=0):
    if item == None:
        corpo.config(image=imgTkCorpo)
    else:
        imgCorpo = Image.open('./corpo.png')
        imgCorpo = imgCorpo.resize((550,300), Image.ANTIALIAS)
        imgCorpo.paste(item, (x,y), item)
        imgTkItem = ImageTk.PhotoImage(imgCorpo)
        corpo.image = imgTkItem
        corpo['image'] = corpo.image

janelaPrincipal = Tk()
janelaPrincipal.title('Criação de Personagem')
janelaPrincipal.geometry("900x600")
janelaPrincipal.resizable(False, False)
janelaPrincipal.config(background="black")

janelaPersonagem = Frame(janelaPrincipal, bg='black', width='300', height='480')
janelaPersonagem.place(x='-10' ,y='160')
imgCorpo = Image.open('./corpo.png')
imgCorpo = imgCorpo.resize((550,300), Image.ANTIALIAS)
imgTkCorpo = ImageTk.PhotoImage(imgCorpo)
corpo = Label(janelaPersonagem, bg='black', image=imgTkCorpo)
#corpo.image = imgTkCorpo
#corpo['image'] = corpo.image
corpo.pack()

imgKyleHat = Image.open('./KyleHat.png')
imgKyleHat = imgKyleHat.resize((250, 150), Image.ANTIALIAS)
indiceCabelo = 0
cabideCabelo = [None, imgKyleHat]

janelaEscolha = Frame(janelaPrincipal, bg='black', width='300', height='420')
janelaEscolha.place(x='560', y='60')
imgCabelo = Image.open('./cabeloIcone.png')
imgCabelo = imgCabelo.resize((35,35), Image.ANTIALIAS)
imgTkCabelo = ImageTk.PhotoImage(imgCabelo)
botaoCabelo = Botao(janelaEscolha, image=imgTkCabelo)
botaoCabelo.grid(row=0, column=0)
imgFace = Image.open('./faceIcone.png')
imgFace = imgFace.resize((35,35), Image.ANTIALIAS)
imgTkFace = ImageTk.PhotoImage(imgFace)
botaoFace = Botao(janelaEscolha, image=imgTkFace)
botaoFace.grid(row=0, column=1)
imgTorso = Image.open('./torsoIcone.png')
imgTorso = imgTorso.resize((35,35), Image.ANTIALIAS)
imgTkTorso = ImageTk.PhotoImage(imgTorso)
botaoTorso = Botao(janelaEscolha, image=imgTkTorso)
botaoTorso.grid(row=0, column=2)
imgPerna = Image.open('./pernaIcone.png')
imgPerna = imgPerna.resize((35,35), Image.ANTIALIAS)
imgTkPerna = ImageTk.PhotoImage(imgPerna)
botaoPerna = Botao(janelaEscolha, image=imgTkPerna)
botaoPerna.grid(row=0, column=3)
botaoEsquerda = Button(janelaEscolha, text='<', height='2', bd=2, bg='#202020', activebackground='#202020', highlightcolor='#202020', highlightbackground='black', command= lambda: percorreCabide(False))
botaoEsquerda.grid(row=1, column=0, columnspan=2, sticky='WE')
botaoDireita = Button(janelaEscolha, text='>', height='2', bd=2, bg='#202020', activebackground='#202020', highlightcolor='#202020', highlightbackground='black', command= lambda: percorreCabide(True))
botaoDireita.grid(row=1, column=2, columnspan=2, sticky='WE')

janelaNome = Frame(janelaPrincipal, width='300', height='60')
janelaNome.place(x='560', y='480')
textoNome = Label(janelaPrincipal, text='Nome', font=('Quicksand', 24, 'bold'), bg='black', fg='white')
textoNome.place(x='670', y='436')
nome = StringVar()
nome.trace('w', limitaEntrada)
campoNome = Entry(janelaNome, textvariable=nome, font=('Quicksand', 24, 'bold'), bg='#202020', highlightbackground='black', bd=2)
campoNome.place(width='300', height='60')

janelaPrincipal.mainloop()
