from tkinter import *
from tkinter import messagebox
 
root = Tk()
root.title("Вікторина")
root.geometry("400x400")
 
def que1():
    q1 = Label(root, text="Каких камней нет ни в одном море?")
    v1 = Entry()
    btn = Button(root, text="Ответ!", command=lambda: game1(que2))
    q1.pack(pady=10)
    v1.pack(pady=10)
    btn.pack(pady=10)
    
    def game1(que2):
        if v1.get().lower() == "сухих":
            que2()
        else:
            messagebox.showerror("Ошибка!", "Попробуйте еще раз!")
            
 
def que2():
    q2 = Label(root, text="Белым снегом всё одето,\n значит наступило:.")
    v2 = Entry()
    btn2 = Button(root, text="Ответ!", command=lambda: game2(que2))
    q2.pack(pady=10)
    v2.pack(pady=10)
    btn2.pack(pady=10)
    
    def game2(que2):
        if v2.get().lower() == "зима":
            messagebox.showinfo("Ты выиграл!!", "молодец!")
        else:
            messagebox.showerror("Ошибка!", "Попробуйте ещё раз!")


def que3():
    q3 = Label(root, text="Что было «завтра», а будет «вчера»?")
    v3 = Entry()
    btn3 = Button(root, text="Ответ!", command=lambda: game3(que3))
    q3.pack(pady=10)
    v3.pack(pady=10)
    btn3.pack(pady=10)
    
    def game3(que3):
        if v3.get().lower() == "сегодня":
            messagebox.showinfo("Ты выиграл!!", "молодец!")
        else:
            messagebox.showerror("Ошибка!", "Попробуйте ещё раз!")

    
que1()    
