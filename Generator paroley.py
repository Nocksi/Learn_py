import random
from tkinter import *

sum = ''
i = 0
abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc1 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
sp = '!@#$%^&*+-/?()0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*+-/?()'

def var1():
    global sum, i, abc, abc1, sp
    n = int(ent.get())
    main_win.destroy()
    while i < n:
        sim = abc[random.randint(0, len(abc) - 1)]
        sum += sim
        i += 1
    pas_win = Tk()
    pas_win.title('Результат')
    pas_win.geometry('300x75')
    pas_win.resizable(width=False, height=False)
    pas_win['bg'] = 'black'
    rez = Label(pas_win, text='Ваш пароль:', bg='black', fg='white', font='Calibri 20')
    pas = Entry(pas_win, bg='white', fg='black', font='Calibri 20', justify='center', width='30', text=sum)
    pas.insert(END, sum)
    rez.pack()
    pas.pack()
    pas_win.mainloop()

def var2():
    global sum, i, abc, abc1, sp
    n = int(ent.get())
    main_win.destroy()
    while i < n:
        sim = abc1[random.randint(0, len(abc1) - 1)]
        sum += sim
        i += 1
    pas_win = Tk()
    pas_win.title('Результат')
    pas_win.geometry('300x75')
    pas_win.resizable(width=False, height=False)
    pas_win['bg'] = 'black'
    rez = Label(pas_win, text='Ваш пароль:', bg='black', fg='white', font='Calibri 20')
    pas = Entry(pas_win, bg='white', fg='black', font='Calibri 20', justify='center', width='30', text=sum)
    pas.insert(END, sum)
    rez.pack()
    pas.pack()
    pas_win.mainloop()

def var3():
    global sum, i, abc, abc1, sp
    n = int(ent.get())
    main_win.destroy()
    while i < n:
        sim = sp[random.randint(0, len(sp) - 1)]
        sum += sim
        i += 1
    pas_win = Tk()
    pas_win.title('Результат')
    pas_win.geometry('300x75')
    pas_win.resizable(width=False, height=False)
    pas_win['bg'] = 'black'
    rez = Label(pas_win, text='Ваш пароль:', bg='black', fg='white', font='Calibri 20')
    pas = Entry(pas_win, bg='white', fg='black', font='Calibri 20', justify='center', width='30', text=sum)
    pas.insert(END, sum)
    rez.pack()
    pas.pack()
    pas_win.mainloop()

main_win = Tk()

main_win.title('Генератор паролей')
main_win.geometry('600x300')
main_win.resizable(width=False, height=False)
main_win['bg'] = 'black'


welk = Label(main_win, text='ДОБРО ПОЖАЛОВАТЬ В ГЕНЕРАТОР ПАРОЛЕЙ', bg='black', fg='white', font='Calibri 21')
welk.pack()

ask = Label(main_win, text='Сколько символов в пароле?', bg='black', fg='white', font='Calibri 18')

ask.pack()

ent = Entry(main_win, bg='white', fg='black', font='Calibri 18', justify='center', width='10')
ent.pack()

btn1 = Button(main_win, text='Cтрочные + заглавные буквы', bg='black', fg='white', font='Calibri 18', width='30',
              height='1', command=var1)
btn1.pack()

btn2 = Button(main_win, text='Строчные + заглавные + цифры', bg='black', fg='white', font='Calibri 18', width='30',
              height='1', command=var2)
btn2.pack()

btn3 = Button(main_win, text='Буквы + цифры + символы', bg='black', fg='white', font='Calibri 18', width='30',
              height='1', command=var3)
btn3.pack()

main_win.mainloop()
