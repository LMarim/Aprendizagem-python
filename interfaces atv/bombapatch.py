import customtkinter as ct
import os

#funções-----------------
def desligar():
    os.system('shutdown /s /t 0')
def reiniciar():
    os.system('shutdown /r /t 0')
def bloquear():
    os.system('shutdow /l /t 0')
    
#--------------------------

ct.set_appearance_mode('dark')

janela=ct.CTk('#313131')
janela.minsize(300,500)
janela.maxsize(720,960)
janela.title("Bomba pacth💣")

botao= ct.CTkButton(janela,text='Desligar',fg_color='white',text_color='#000000',hover_color="#696969",font=('arial',20,'bold'),width=150,height=80,command=desligar)
botao.pack(pady=20)

botao= ct.CTkButton(janela,text='Reiniciar',fg_color='white',text_color='#000000',hover_color="#696969",font=('arial',20,'bold'),width=150,height=80,command=reiniciar)
botao.pack(pady=20)

botao= ct.CTkButton(janela,text='Bloquear',fg_color='white',text_color='#000000',hover_color="#696969",font=('arial',20,'bold'),width=150,height=80,command=bloquear)
botao.pack(pady=20)



janela.mainloop()