from tkinter import ttk
import random

def random_num():
    x=randint(1,9)
    for i in range(1,3):
        x+=randint(0,9)*(10**i)
    return x

def game():
    global button_1, button_2
    
    game_window=tkinter.Tk()
    game_window.title('New Game')
    game_window.geometry('500x1000')
    
    ttk.Label(master=game_window, text='what's the number..??').pack(pady=15)

    guess_1 = ttk.Label(master=game_window, text= )#here eeee

rules = ''

window = tkinter.Tk()
window.title('1. Bagels')
window.geometry('300x500')

ttk.Label(master=window, text='WELCOME TO BAGELS', font='calibri 20 bold').pack(pady=15)

button_1 = ttk.Button(master=window, text='-] New Game', command=game, width=20)
button_1.pack(pady=10)

button_2 = ttk.Button(master=window, text='rules', command=lambda: print(rules))
button_2.pack(pady=10)


window.mainloop()