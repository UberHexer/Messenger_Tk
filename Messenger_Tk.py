from tkinter import *


def getText1(s):
    name1 = Name1.get()   
    if Window2 == 1:
        s = text1.get(1.0, END)
        text1.delete(1.0, END)
        ListBox2.insert(END, " "+ name1 +": " + s)
        ListBox1.insert(END, "Я: " + s)
    else:
        ListBox1.insert(END, "Вы не можете отправить сообщение, ваш собеседник вышел")


def getText2(s):
    if Window1 == 1:
        name2 = Name2.get()   
        s = text2.get(1.0, END)
        text2.delete(1.0, END)
        ListBox1.insert(END, " "+ name2 +": " + s)
        ListBox2.insert(END, "Я: " + s)
    else:
        ListBox2.insert(END, "Вы не можете отправить сообщение, ваш собеседник вышел")


def Exit1():
    global Window1
    name1 = Name1.get()
    Window1 = 0
    root1.destroy()   
    ListBox2.insert(END, "   ______ Пользователь "+ name1 +" вышел ______ ")


def Exit2():
    global Window2
    name2 = Name2.get()
    Window2 = 0
    root2.destroy() 
    ListBox1.insert(END, "   ______ Пользователь "+ name2 +" вышел ______ ")


# _________   №1   __________


root1 = Tk()
root1.title("___User №1___")
root1.geometry('690x320+100+100')
Window1 = 1   

f_top = Frame(root1)
f_bot = Frame(root1)
f_top.pack()
f_bot.pack()

# виджеты окна 1

LblName1 = Label(f_bot, text="Ваше имя:")
LblName1.pack(side=LEFT)

Name1 = Entry(f_bot, width=8)
Name1.pack(side=LEFT)
Name1.insert(0, "User_1")

ListBox1 = Listbox(f_top, width=68, height=10)
ListBox1.pack(side=TOP)

text1 = Text(f_bot, width=39, height=1)
text1.pack(side=LEFT)

get_1 = Button(f_bot, text="Отправить", width=10, height=1, command=getText1)
get_1.pack(side=LEFT)
text1.bind('<Return>', getText1)


# начальные параметры для настройки
ListBox1 ['font'] = ("Times New Roman",15)
Name1 ['font'] = ("Times New Roman",15)
text1 ['font'] = ("Times New Roman",15)
get_1 ['font'] = ("Times New Roman",15)
LblName1 ['font'] = ("Times New Roman",15)

root1 ["bg"] = "teal"
ListBox1 ['bg'] = "azure"
Name1 ['bg'] = "paleturquoise"
text1 ['bg'] = "lightcyan"
get_1 ['bg'] = "turquoise"

ListBox1 ['fg'] ="Black"
Name1 ['fg'] ="Black"
text1 ['fg'] ="Black"
get_1['fg'] ="Black"
LblName1 ['fg'] ="Black"

# Цвета 1
def light1():
   root1 ["bg"] = "Light Gray"
   ListBox1 ['bg'] = "White Smoke"
   Name1 ['bg'] = "Snow"
   text1 ['bg'] = "Ghost White"
   get_1 ['bg'] = "Old Lace"
   LblName1 ['bg'] = "Snow"
   ListBox1 ['fg'] ="Black"
   Name1 ['fg'] ="Black"
   text1 ['fg'] ="Black"
   get_1['fg'] ="Black"
   LblName1 ['fg'] ="Black"

def dark1():
   root1 ["bg"] = "Black"
   ListBox1 ['bg'] = "Black"
   ListBox1 ['fg'] = '#d8d8d8'
   Name1 ['bg'] = "Black"
   Name1 ['fg'] = '#d8d8d8'
   text1 ['bg'] = "Black"
   text1 ['fg'] = '#d8d8d8'
   get_1 ['bg'] = "Black"
   get_1 ['fg'] = '#d8d8d8'
   LblName1 ['bg'] = "Black"
   LblName1 ['fg'] ='#d8d8d8'


def blue1():
   root1 ["bg"] = "teal"
   ListBox1 ['bg'] = "azure"
   Name1 ['bg'] = "paleturquoise"
   text1 ['bg'] = "lightcyan"
   get_1 ['bg'] = "turquoise"
   LblName1 ['bg'] = "paleturquoise"
   ListBox1 ['fg'] ="Black"
   Name1 ['fg'] ="Black"
   text1 ['fg'] ="Black"
   get_1['fg'] ="Black"
   LblName1 ['fg'] ="Black"

def indigo1():
   root1 ["bg"] = "Dark Violet"
   ListBox1 ['bg'] = "Thistle"
   Name1 ['bg'] = "Light Steel Blue"
   text1 ['bg'] = "Light Pink"
   get_1 ['bg'] = "Medium Slate Blue"
   LblName1 ['bg'] = "Light Steel Blue"
   ListBox1 ['fg'] ="Black"
   Name1 ['fg'] ="Black"
   text1 ['fg'] ="Black"
   get_1['fg'] ="Black"
   LblName1 ['fg'] ="Black"

def orange1():
   root1 ["bg"] = "Darkorange"
   ListBox1 ['bg'] = "lightyellow"
   Name1 ['bg'] = "lemonchiffon"
   text1 ['bg'] = "cornsilk"
   get_1 ['bg'] = "gold"
   LblName1 ['bg'] = "lemonchiffon"
   ListBox1 ['fg'] ="Black"
   Name1 ['fg'] ="Black"
   text1 ['fg'] ="Black"
   get_1['fg'] ="Black"
   LblName1 ['fg'] ="Black"


# Font1
def Sans1():
    ListBox1 ['font'] = ("Comic Sans MS",12)
    Name1 ['font'] = ("Comic Sans MS",12)
    text1 ['font'] = ("Comic Sans MS",12)
    get_1 ['font'] = ("Comic Sans MS",12)
    LblName1 ['font'] = ("Comic Sans MS",12)

def Roman1():
    ListBox1 ['font'] = ("Times New Roman",15)
    Name1 ['font'] = ("Times New Roman",15)
    text1 ['font'] = ("Times New Roman",15)
    get_1 ['font'] = ("Times New Roman",15)
    LblName1 ['font'] = ("Times New Roman",15)

def Impact1():
    ListBox1 ['font'] = ("Impact",14)
    Name1 ['font'] = ("Impact",14)
    text1 ['font'] = ("Impact",14)
    get_1 ['font'] = ("Impact",14)
    LblName1 ['font'] = ("Impact",14)

def Segoe1():
    ListBox1 ['font'] = ("Segoe Print",10)
    Name1 ['font'] = ("Segoe Print",10)
    text1 ['font'] = ("Segoe Print",10)
    get_1 ['font'] = ("Segoe Print",10)
    LblName1 ['font'] = ("Segoe Print",10)
    text1 ['width'] = 43



# MENU 

mainmenu = Menu(root1)
root1.config(menu=mainmenu) 
 
optionsmenu = Menu(mainmenu, tearoff=0)

Exitmenu = Menu(mainmenu, tearoff=0)

Color = Menu(optionsmenu, tearoff=1)
Color.add_command(label="Светлая",command=light1)
Color.add_command(label="Темная",command=dark1)
Color.add_command(label="Бирюзовая",command=blue1)
Color.add_command(label="Индиго",command=indigo1)
Color.add_command(label="Оранжевая", command=orange1)

Font = Menu(optionsmenu, tearoff=1)
Font.add_command(label="Comic Sans MS",command=Sans1)
Font.add_command(label="Times New Roman",command=Roman1)
Font.add_command(label="Impact",command=Impact1)
Font.add_command(label="Segoe Print",command=Segoe1)


optionsmenu.add_cascade(label="Цветовая гамма", menu=Color)
optionsmenu.add_cascade(label="Шрифт текста",menu=Font)
#optionsmenu.add_cascade(label="Выход",command=Exit1) не обязательно должна быть в меню


mainmenu.add_cascade(label="Настройки", menu=optionsmenu)
mainmenu.add_cascade(label="Выход", command=Exit1)

# _________   №2   __________

root2 = Tk()
root2 ["bg"] = "Darkorange"
root2.title("___User №2___")
root2.geometry('690x320+800+100')
Window2 = 1

f_top = Frame(root2)
f_bot = Frame(root2)
f_top.pack()
f_bot.pack()


# виджеты окна 2

LblName2 = Label(f_bot, text="Ваше имя:")
LblName2.pack(side = LEFT)

Name2 = Entry(f_bot,width=8)
Name2.pack(side=LEFT)
Name2.insert(0,"User_2")

ListBox2 = Listbox(f_top, width=68, height=10)
ListBox2.pack(side=TOP)

text2 = Text(f_bot, width=39, height=1 )
text2.pack(side=LEFT)

get_2 = Button(f_bot, text="Отправить",width=10,height = 1, command=getText2)
get_2.pack(side=LEFT)
text2.bind('<Return>', getText2)

# начальные параметры для настройки

ListBox2 ['font'] = ("Times New Roman",15)
Name2 ['font'] = ("Times New Roman",15)
text2 ['font'] = ("Times New Roman",15)
get_2 ['font'] = ("Times New Roman",15)
LblName2 ['font'] = ("Times New Roman",15)

root2 ["bg"] = "Darkorange"
ListBox2 ['bg'] = "lightyellow"
Name2 ['bg'] = "lemonchiffon"
text2 ['bg'] = "cornsilk"
get_2 ['bg'] = "gold"
LblName2 ['bg'] = "lemonchiffon"
 
ListBox2 ['fg'] ="Black"
Name2 ['fg'] ="Black"
text2 ['fg'] ="Black"
get_2 ['fg'] ="Black"
LblName2 ['fg'] ="Black"

# Цвета 2
def light2():
   root2 ["bg"] = "Light Gray"
   ListBox2 ['bg'] = "White Smoke"
   Name2 ['bg'] = "Snow"
   text2 ['bg'] = "Ghost White"
   get_2 ['bg'] = "Old Lace"
   LblName2 ['bg'] = "Snow"
   ListBox2 ['fg'] ="Black"
   Name2 ['fg'] ="Black"
   text2 ['fg'] ="Black"
   get_2 ['fg'] ="Black"
   LblName2 ['fg'] ="Black"

def dark2():
   root2 ["bg"] = "Black"
   ListBox2 ['bg'] = "Black"
   ListBox2 ['fg'] = '#d8d8d8'
   Name2 ['bg'] = "Black"
   Name2 ['fg'] = '#d8d8d8'
   text2 ['bg'] = "Black"
   text2 ['fg'] = '#d8d8d8'
   get_2 ['bg'] = "Black"
   get_2 ['fg'] = '#d8d8d8'
   LblName2 ['bg'] = "Black"
   LblName2 ['fg'] ='#d8d8d8'


def blue2():
   root2 ["bg"] = "teal"
   ListBox2 ['bg'] = "azure"
   Name2 ['bg'] = "paleturquoise"
   text2 ['bg'] = "lightcyan"
   get_2 ['bg'] = "turquoise"
   LblName2 ['bg'] = "paleturquoise"
   ListBox2 ['fg'] ="Black"
   Name2 ['fg'] ="Black"
   text2 ['fg'] ="Black"
   get_2 ['fg'] ="Black"
   LblName2 ['fg'] ="Black"

def indigo2():
   root2 ["bg"] = "Dark Violet"
   ListBox2 ['bg'] = "Thistle"
   Name2 ['bg'] = "Light Steel Blue"
   text2 ['bg'] = "Light Pink"
   get_2 ['bg'] = "Medium Slate Blue"
   LblName2 ['bg'] = "Light Steel Blue"
   ListBox2 ['fg'] ="Black"
   Name2 ['fg'] ="Black"
   text2 ['fg'] ="Black"
   get_2 ['fg'] ="Black"
   LblName2 ['fg'] ="Black"

def orange2():
   root2 ["bg"] = "Darkorange"
   ListBox2 ['bg'] = "lightyellow"
   Name2 ['bg'] = "lemonchiffon"
   text2 ['bg'] = "cornsilk"
   get_2 ['bg'] = "gold"
   LblName2 ['bg'] = "lemonchiffon"
   ListBox2 ['fg'] ="Black"
   Name2 ['fg'] ="Black"
   text2 ['fg'] ="Black"
   get_2 ['fg'] ="Black"
   LblName2 ['fg'] ="Black"

# Font2
def Sans2():
    ListBox2 ['font'] = ("Comic Sans MS",12)
    Name2 ['font'] = ("Comic Sans MS",12)
    text2 ['font'] = ("Comic Sans MS",12)
    get_2 ['font'] = ("Comic Sans MS",12)
    LblName2 ['font'] = ("Comic Sans MS",12)

def Roman2():
    ListBox2 ['font'] = ("Times New Roman",15)
    Name2 ['font'] = ("Times New Roman",15)
    text2 ['font'] = ("Times New Roman",15)
    get_2 ['font'] = ("Times New Roman",15)
    LblName2 ['font'] = ("Times New Roman",15)

def Impact2():
    ListBox2 ['font'] = ("Impact",14)
    Name2 ['font'] = ("Impact",14)
    text2 ['font'] = ("Impact",14)
    get_2 ['font'] = ("Impact",14)
    LblName2 ['font'] = ("Impact",14)

def Segoe2():
    ListBox2 ['font'] = ("Segoe Print",10)
    Name2 ['font'] = ("Segoe Print",10)
    text2 ['font'] = ("Segoe Print",10)
    get_2 ['font'] = ("Segoe Print",10)
    LblName2 ['font'] = ("Segoe Print",10)
    text2 ['width'] = 43


# MENU2 
mainmenu = Menu(root2)
root2.config(menu=mainmenu) 
 
optionsmenu = Menu(mainmenu, tearoff=0)

Exitmenu = Menu(optionsmenu, tearoff=0)


Color = Menu(optionsmenu, tearoff=1)
Color.add_command(label="Светлая", command = light2)
Color.add_command(label="Темная", command = dark2)
Color.add_command(label="Бирюзовая",command=blue2)
Color.add_command(label="Индиго", command = indigo2)
Color.add_command(label="Оранжевая", command=orange2)

Font = Menu(optionsmenu, tearoff=1)
Font.add_command(label="Comic Sans MS",command=Sans2)
Font.add_command(label="Times New Roman",command=Roman2)
Font.add_command(label="Impact",command=Impact2)
Font.add_command(label="Segoe Print",command=Segoe2) 

optionsmenu.add_cascade(label="Цветовая гамма", menu=Color)
optionsmenu.add_cascade(label="Шрифт текста",menu=Font)
# optionsmenu.add_cascade(label="Выход",command=Exit2) не обязательно быть в меню


mainmenu.add_cascade(label="Настройки", menu=optionsmenu)
mainmenu.add_cascade(label="Выход", command=Exit2)

# mainloop
root1.mainloop()
root2.mainloop()

# код написан 25.02.2019
 