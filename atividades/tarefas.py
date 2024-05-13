import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import messagebox

windows = ctk.CTk('#ffffdf')
windows.geometry('350x480')
windows.title("To do list")
windows.iconbitmap('atividades/check.ico')
#FUNCTIONS---------
def add_tarefa():
    tarefa = task.get()
    if tarefa:
        list.insert(0,tarefa)
        task.delete(0,END)
    else:
        messagebox.showerror("ERRO", 'Digite alguma tarefa!')
def remove_tarefa():
    task_select = list.curselection(0)
    if task_select:
        list.delete(task_select[0])
    else:
        messagebox.showerror("ERRO", 'Nehuma tarefa selecionada!!!')

#fonte
font1 =('AC+AB',30,'bold')
font2 =('AC+AB',20,'bold')
#painel
ctk.CTkLabel(windows,text='Lista de Tarefas',font= font1, text_color='black').pack(pady=10)

task = ctk.CTkEntry(windows,width=240,fg_color="#B9B4C7",border_color="#9C98A9",placeholder_text="Digite uma tarefa aqui")
task.pack(pady=30)

add = ctk.CTkButton(windows,text="adiconar",fg_color="#352F44",width=100,height=35,hover_color="#5C5470", command= add_tarefa)
add.place(relx = 0.1,rely= 0.3,anchor = 'w')

remove = ctk.CTkButton(windows,text="remover",fg_color="#352F44",width=100,height=35,hover_color="#5C5470", command= remove_tarefa)
remove.place(relx = 0.85,rely= 0.3,anchor = 'e')

ctk.CTkLabel(windows,text='Tarefas',font= font1, text_color='black').place(relx = 0.4,rely= 0.37,anchor = 'w')

list = Listbox(windows, width=40,height=15)
list.place(relx = 0.13,rely= 0.67,anchor = 'w')

windows.mainloop()