from cProfile import label
from tkinter import *
from turtle import width

janela = Tk()
janela.geometry("720x300")
janela.title("OS MELHORES DEVS DO MUNDO")
#janela.configure(background="red")

texto = Label(
    janela,
    text = "OS MELHORES DO MUNDO!!!",
    font = (
        "Helvetica", 18, "bold"
    )

)
        

    
texto.place(
    x = 40,
    y = 0,
    width = 500,
    height = 30

)












janela.mainloop()
