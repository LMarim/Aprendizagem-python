import customtkinter as ct


ct.set_appearance_mode('dark')

janela = ct.CTk('#303030')
janela.title('Tela de login')
janela.minsize(500,500)
janela.maxsize(1980,1020)

titula = ct.CTkLabel(janela,text="Tela de Login",font=('arial',30,"bold"),text_color="#803030")
titula.pack(pady=20)

login = ct.CTkEntry(janela,placeholder_text='Digite seu login',width=300,height=40,fg_color='lightgrey',text_color="#696969")
login.pack(pady=10)

senha = ct.CTkEntry(janela,placeholder_text='Digite sua senha',width=300,height=40,fg_color='lightgrey',show='♦',text_color='#696969')
senha.pack(pady=10)

lembrar = ct.CTkCheckBox(janela,text='Lembrar de mim',text_color='lightgrey',fg_color='darkgrey',)
lembrar.pack()

botao= ct.CTkButton(janela,text='Entrar',fg_color='darkgrey',text_color='#803030',hover_color="#696969")
botao.pack(pady=10)

janela.mainloop()