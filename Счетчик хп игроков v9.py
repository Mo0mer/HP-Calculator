from tkinter import *
from tkinter import messagebox
from random import randint

UserName = ''
sus = []
k = 0
index = 0
char = []
charc = []
r1 = 0
r2 = 0
r3 = 0
r4 = 0
flag = ''
soprflag = False
uizflag = False
dpflag = False
sopr = []
uiz = []
dpdg = []


def dpdmg():
    global dpflag
    global dpdg
    dpflag = True
    dg = urbox.get(urbox.curselection()[0])
    dpdg.append(dg)


def soprf():
    global soprflag
    global sopr
    soprflag = True
    sr = elbox.get(elbox.curselection()[0])
    sopr.append(sr)


def uizf():
    global uizflag
    global uiz
    uizflag = True
    uz = urbox.get(urbox.curselection()[0])
    uiz.append(uz)


def elnabf():
    elbox.place(x=0, y=0)
    urbox.place(x=300, y=0)
    soprdmg.place(x=120, y=60)
    uizdmg.place(x=420, y=60)


def probf():
    global sus
    global r4
    global index
    r4 = 0
    prob.place_forget()
    chlistbox.place_forget()
    name.place_forget()
    choiceclick.place_forget()
    bonpout.place_forget()
    atackclick.place_forget()
    hilclick.place_forget()
    hl.place_forget()
    bonp.place_forget()
    fzgamet.set("Фаза урона")
    nametext.set('Кол-во костей')
    kdtext.set('Вид кости')
    hptext.set('Доп. урон')
    messagebox.showinfo('Счетчик хп', 'Пробит без шанса')
    sus = chlistbox.get(chlistbox.curselection()[0])
    index = chlistbox.curselection()[0]
    sus = list(sus)
    name.place(x=10, y=70 + 30, width=150)  # Кол-во костей(текст)
    kdout.place(x=175, y=70 + 30, width=150)  # Вид кости(текст)
    hpout.place(x=340, y=70 + 30, width=150)  # Доп урон(текст)
    fzgame.place(x=0, y=0 + 30, width=500)
    namehero.place(x=10, y=100 + 30, width=150)  # Кол-во костей
    hp.place(x=175, y=100 + 30, width=150)  # Вид кости
    kd.place(x=340, y=100 + 30, width=150)  # Доп урон
    dmgclick.place(x=0, y=150 + 30, width=500)  # Кнопка бам


def atkf():
    global r4
    if r4 == 0:
        prob.place(x=345, y=30, width=30)
        r4 += 1
    else:
        prob.place_forget()
        r4 = 0


def plus():
    global r3
    kdpl = int(ism.get())
    indx = chlistbox.curselection()[0]
    ss = chlistbox.get(indx)
    sos = list(ss)
    sos[2] = sos[2] + kdpl
    char[indx] = sos
    chlistbox.delete(0, END)
    for i in char:
        chlistbox.insert(END, i)
    print(*char)
    r3 = 0
    ism.place_forget()
    ismkdpl.place_forget()
    ismkdmn.place_forget()


def minus():
    global r3
    kdpl = int(ism.get())
    indx = chlistbox.curselection()[0]
    ss = chlistbox.get(indx)
    sos = list(ss)
    sos[2] = sos[2] - kdpl
    char[indx] = sos
    chlistbox.delete(0, END)
    for i in char:
        chlistbox.insert(END, i)
    print(*char)
    r3 = 0
    ism.place_forget()
    ismkdpl.place_forget()
    ismkdmn.place_forget()


def iskd():
    ismkd.place_forget()
    ism.place(x=210, y=35, width=100)
    ismkdpl.place(x=220, y=60, width=30)
    ismkdmn.place(x=260, y=60, width=30)


def vkd():
    global r3
    if r3 == 0:
        ismkd.place(x=245, y=30, width=30)
        r3 += 1
    else:
        ismkd.place_forget()
        r3 = 0


def dopf():
    global r1
    if r1 == 0:
        otkat.place(x=10, y=30)
        revclick.place(x=50, y=30)
        r1 += 1
    else:
        otkat.place_forget()
        revclick.place_forget()
        r1 = 0


def pref():
    global r2
    if r2 == 0:
        pry.place(x=120, y=30)
        pm.place(x=120, y=57)
        pmn.place(x=120, y=83)
        r2 += 1
    else:
        pry.place_forget()
        pm.place_forget()
        pmn.place_forget()
        r2 = 0


def otk():
    if not char:
        pass
    else:
        bonp.place_forget()
        namehero.place_forget()
        hp.place_forget()
        kd.place_forget()
        hl.place_forget()
        revnab.place_forget()
        endnab.place_forget()
        atackclick.place_forget()
        dmgclick.place_forget()
        hilclick.place_forget()
        choiceclick.place_forget()
        name.place_forget()
        hpout.place_forget()
        kdout.place_forget()
        bonpout.place_forget()
        cthero.place_forget()
        fzgamet.set("Фаза выбора")
        fzgame.place(x=0, y=0 + 30, width=500)
        chlistbox.place(x=110, y=100 + 30, width=150)
        nametext.set("Имя персонажа")
        name.place(x=110, y=60 + 30, width=150)
        choiceclick.place(x=280, y=75 + 30)


def reverend():
    global char
    global k
    bonp.place_forget()
    namehero.place_forget()
    hp.place_forget()
    kd.place_forget()
    hl.place_forget()
    revnab.place_forget()
    endnab.place_forget()
    atackclick.place_forget()
    dmgclick.place_forget()
    hilclick.place_forget()
    choiceclick.place_forget()
    name.place_forget()
    hpout.place_forget()
    kdout.place_forget()
    bonpout.place_forget()
    cthero.place_forget()
    revclickend.place_forget()
    chlistbox.delete(0, END)
    char = charc
    for i in charc:
        chlistbox.insert(END, i)
    print(*charc)
    revclick.place_forget()
    k = 0
    fzgamet.set("Фаза выбора")
    fzgame.place(x=0, y=0 + 30, width=500)
    chlistbox.place(x=110, y=100 + 30, width=150)
    nametext.set("Имя персонажа")
    name.place(x=110, y=60 + 30, width=150)
    choiceclick.place(x=280, y=75 + 30)
    dop.place(x=0, y=0, width=100)
    pre.place(x=105, y=0, width=100)


def rever():
    global char
    global k
    if not char:
        pass
    else:
        bonp.place_forget()
        namehero.place_forget()
        hp.place_forget()
        kd.place_forget()
        hl.place_forget()
        revnab.place_forget()
        endnab.place_forget()
        atackclick.place_forget()
        dmgclick.place_forget()
        hilclick.place_forget()
        choiceclick.place_forget()
        name.place_forget()
        hpout.place_forget()
        kdout.place_forget()
        bonpout.place_forget()
        cthero.place_forget()
        chlistbox.delete(0, END)
        for i in charc:
            chlistbox.insert(END, i)
        print(*charc)
        k = 0
        fzgamet.set("Фаза выбора")
        fzgame.place(x=0, y=0 + 30, width=500)
        chlistbox.place(x=110, y=100 + 30, width=150)
        nametext.set("Имя персонажа")
        name.place(x=110, y=60 + 30, width=150)
        choiceclick.place(x=280, y=75 + 30)


def nextfaze():  # Функция для выбора
    global sus
    sus = chlistbox.get(chlistbox.curselection()[0])
    if sus == '':
        pass
    chlistbox.place_forget()
    name.place_forget()
    choiceclick.place_forget()
    fzgamet.set("Фаза действия")
    nametext.set("Кол-во хила")
    bonpt.set("Бонус попадания")
    name.place(x=285, y=50 + 30, width=150)
    bonpout.place(x=65, y=50 + 30, width=150)
    atackclick.place(x=65, y=140 + 30, width=150)
    hilclick.place(x=285, y=140 + 30, width=150)
    hl.place(x=285, y=100 + 30, width=150)
    bonp.place(x=65, y=100 + 30, width=150)
    fzgame.place(x=0, y=0 + 30, width=500)


def hil():  # Функция исцеления
    hh = int(hl.get())
    indx = chlistbox.curselection()[0]
    ss = chlistbox.get(indx)
    sos = list(ss)
    sos[1] = sos[1] + hh
    hn = sos[0]
    char[indx] = sos
    messagebox.showinfo(hn, 'Хп восстановлено: ' + str(hh))
    messagebox.showinfo(hn, 'Текущее хп: ' + str(sos[1]))
    print('-----------------------------------')
    print('ХП восполнено: ', hh)
    print('-----------------------------------')
    chlistbox.delete(0, END)
    for i in char:
        chlistbox.insert(END, i)
    print(*char)
    name.place_forget()
    bonpout.place_forget()
    atackclick.place_forget()
    hilclick.place_forget()
    hl.place_forget()
    bonp.place_forget()
    fzgamet.set("Фаза выбора")
    fzgame.place(x=0, y=0 + 30, width=500)
    chlistbox.place(x=110, y=100 + 30, width=150)
    nametext.set("Имя персонажа")
    name.place(x=110, y=60 + 30, width=150)
    choiceclick.place(x=280, y=75 + 30)


def mybtnclick():  # Функция нажатия на кнопку ОК
    global k
    MyBtn.place_forget()
    nametext.set("Имя героя")
    hptext.set("ХП героя")
    kdtext.set("КД героя")
    fzgamet.set("Фаза создания")
    elnab.place(x=370, y=150)
    fzgame.place(x=0, y=30, width=500)
    name.place(x=50, y=70 + 20, width=100)
    hpout.place(x=200, y=70 + 20, width=100)
    kdout.place(x=350, y=70 + 20, width=100)
    namehero.place(x=50, y=100 + 20, width=100)
    hp.place(x=200, y=100 + 20, width=100)
    kd.place(x=350, y=100 + 20, width=100)
    revnab.place(x=245, y=180, width=120)
    endnab.place(x=370, y=180, width=120)
    dop.place(x=0, y=0, width=100)
    pre.place(x=105, y=0, width=100)
    inkd.place(x=210, y=0, width=100)
    atk.place(x=315, y=0, width=100)


def choiceplace():  # Функция нажатия на кнопку Закончить набор
    print('-----------------------------')
    messagebox.showinfo('Счетчик хп', 'Набор закончен')
    for i in char:
        chlistbox.insert(END, i)
    cthero.place_forget()
    name.place_forget()
    hpout.place_forget()
    kdout.place_forget()
    namehero.place_forget()
    hp.place_forget()
    kd.place_forget()
    revnab.place_forget()
    endnab.place_forget()
    soprdmg.place_forget()
    uizdmg.place_forget()
    elbox.place_forget()
    elnab.place_forget()
    fzgamet.set("Фаза выбора")
    fzgame.place(x=0, y=30, width=500)
    chlistbox.place(x=110, y=100 + 30, width=150)
    nametext.set("Имя персонажа")
    name.place(x=110, y=60 + 30, width=150)
    choiceclick.place(x=280, y=75 + 30)
    urbox.place(x=250, y=0)
    dpdmg.place(x=0, y=0)


def nabhero():  # Функция для создания героев
    global sopr
    global uiz
    global soprflag
    global uizflag
    global k
    global char
    global charc
    k += 1
    ctherot.set('Кол-во героев: ' + str(k))
    cthero.place(x=0, y=180)
    st = []
    nh = namehero.get()
    hph = int(hp.get())
    kdh = int(kd.get())
    st.append(nh)
    st.append(hph)
    st.append(kdh)
    if soprflag and uizflag is False:
        st.append('| Сопр -')
        st.append(sopr)
    elif uizflag and soprflag is False:
        st.append('| Уяз -')
        st.append(uiz)
    elif soprflag is True and uizflag is True:
        st.append('| Сопр -')
        st.append(sopr)
        st.append('| Уяз -')
        st.append(uiz)
    print(*st)
    char.append(st)
    charc.append(st)
    sopr = []
    uiz = []
    uizflag = False
    soprflag = False
    nameinp.set('')
    hpinp.set('')
    kdinp.set('')


def prdamage():  # Функция для опеределения пробития
    global flag
    global sus
    global index
    prb = bonp.get()
    if prb == '':
        prb = 0
    else:
        prb = int(prb)
    sus = chlistbox.get(chlistbox.curselection()[0])
    index = chlistbox.curselection()[0]
    sus = list(sus)
    sp = [randint(1, 20) for _ in range(2)]
    if tp.get() == 1:
        messagebox.showinfo('Счетчик хп', 'Атака с преимуществом')
        bp = max(sp)
    elif tp.get() == 2:
        messagebox.showinfo('Счетчик хп', 'Атака с помехой')
        bp = min(sp)
    else:
        bp = randint(1, 20)
    if bp == 1:
        pr = 1
    elif bp == 20:
        flag = True
        pr = 10 ** 5
    else:
        pr = bp + prb
    print('-----------------------------------')
    print('D20 + БП: ', pr)
    print('КД героя: ', sus[2])
    print('-----------------------------------')
    if pr > sus[2]:
        messagebox.showinfo('Счетчик хп', 'Есть пробитие')
        name.place_forget()
        bonpout.place_forget()
        bonp.place_forget()
        chlistbox.place_forget()
        name.place_forget()
        bonpout.place_forget()
        atackclick.place_forget()
        hilclick.place_forget()
        hl.place_forget()
        krit.place_forget()
        bonp.place_forget()
        fzgamet.set("Фаза урона")
        nametext.set('Кол-во костей')
        kdtext.set('Вид кости')
        hptext.set('Доп. урон')
        kritt.set('Урон будет увеличен вдвое')
        if flag:
            krit.place(x=125, y=65, width=250)
        name.place(x=10, y=70 + 30, width=150)  # Кол-во костей(текст)
        kdout.place(x=175, y=70 + 30, width=150)  # Вид кости(текст)
        hpout.place(x=340, y=70 + 30, width=150)  # Доп урон(текст)
        fzgame.place(x=0, y=0 + 30, width=500)
        namehero.place(x=10, y=100 + 30, width=150)  # Кол-во костей
        hp.place(x=175, y=100 + 30, width=150)  # Вид кости
        kd.place(x=340, y=100 + 30, width=150)  # Доп урон
        dmgclick.place(x=0, y=150 + 30, width=500)  # Кнопка бам
    else:
        messagebox.showinfo('Счетчик хп', 'Рикошет')
        name.place_forget()
        bonpout.place_forget()
        atackclick.place_forget()
        hilclick.place_forget()
        hl.place_forget()
        bonp.place_forget()
        krit.place_forget()
        fzgamet.set("Фаза выбора")
        fzgame.place(x=0, y=0 + 30, width=500)
        chlistbox.place(x=110, y=100 + 30, width=150)
        nametext.set("Имя персонажа")
        name.place(x=110, y=60 + 30, width=150)
        choiceclick.place(x=280, y=75 + 30)


def damage():
    global flag
    global dpflag
    global dpdg
    cd, dice, diceb = int(namehero.get()), int(hp.get()), int(kd.get())
    dmg = 0
    for i in range(cd):
        dmg += randint(1, dice)
    if diceb != '':
        dmg += int(diceb)
    if flag:
        dmg = dmg * 2
    if dpflag:
        if dpdg[0] in els:
            messagebox.showinfo(sus[0], 'Сопротивление')
            dmg = int(dmg / 2)
        elif dpdg[0] in ur:
            messagebox.showinfo(sus[0], 'Уязвимость')
            dmg = dmg * 2
    sus[1] = sus[1] - dmg
    char[index] = sus
    flag = False
    dpflag = False
    messagebox.showinfo(sus[0], 'Нанесенный урон: ' + str(dmg))
    print('-----------------------------------')
    print('Нанесенный урон: ', dmg)
    print('-----------------------------------')

    if sus[1] <= 0:
        messagebox.showinfo(sus[0], 'Нокаут')
        char.remove(sus)
    else:
        messagebox.showinfo(sus[0], 'Оставшееся хп: ' + str(sus[1]))
    if not char:
        print()
        print('-----------------------------')
        print()
        print('Game Over')
        messagebox.showinfo('Счетчик хп', 'Все герои мертвы, игра закончена')
        krit.place_forget()
        name.place_forget()
        kdout.place_forget()
        hpout.place_forget()
        fzgame.place_forget()
        namehero.place_forget()
        hp.place_forget()
        kd.place_forget()
        dmgclick.place_forget()
        revclick.place_forget()
        otkat.place_forget()
        dop.place_forget()
        pre.place_forget()
        inkd.place_forget()
        revclickend.place(x=220, y=50)
        revclickend.configure(font='Times 40', fg='#008000')
    else:
        chlistbox.delete(0, END)
        krit.place_forget()
        name.place_forget()
        kdout.place_forget()
        hpout.place_forget()
        namehero.place_forget()
        hp.place_forget()
        kd.place_forget()
        dmgclick.place_forget()
        fzgamet.set("Фаза выбора")
        fzgame.place(x=0, y=0 + 30, width=500)
        chlistbox.place(x=110, y=100 + 30, width=150)
        nametext.set("Имя персонажа")
        choiceclick.place(x=280, y=75 + 30)
        name.place(x=110, y=60 + 30, width=150)
        for i in char:
            chlistbox.insert(END, i)
        print(*char)
        print(dpdg)
        dpdg = []


root = Tk()  # Главное окно
root.title('Счетчик хп')
root.geometry('500x220+300+200')

root1 = Tk()  # Главное окно
root1.title('Счетчик хп')
root1.geometry('500x220+400+300')

MyBtn = Button(root.configure(bg='#241000'), text="Start", font='Times 40', bg="#EE8A3C", fg='#FFB57C', width=3, command=mybtnclick)  # Кнопка
MyBtn.place(x=200, y=50)

nametext = StringVar()
hptext = StringVar()
kdtext = StringVar()
bonpt = StringVar()
ctherot = StringVar()
fzgamet = StringVar()
kritt = StringVar()

name = Label(root, textvariable=nametext, fg="#FFF8DC", bg="#800000", font='Times 14')  # Имя героя(текст)
hpout = Label(root, textvariable=hptext, fg="#FFF8DC", bg="#800000", font='Times 14')  # Хп героя(текст)
kdout = Label(root, textvariable=kdtext, fg="#FFF8DC", bg="#800000", font='Times 14')  # Кд героя(текст)
bonpout = Label(root, textvariable=bonpt, fg="#FFF8DC", bg="#800000", font='Times 14')  # Бонус к попаданию(текст)
cthero = Label(root, textvariable=ctherot, fg="#FFF8DC", bg="#800000", font='Times 14')  # Кол-во героев(текст)
fzgame = Label(root, textvariable=fzgamet, fg="#FFF8DC", bg="#800000", font='Times 14')  # Фаза игры
krit = Label(root, textvariable=kritt, fg="#FFF8DC", bg="#800000", font='Times 14')

nameinp = StringVar()
hpinp = StringVar()
kdinp = StringVar()
bonpinp = StringVar()
hilinp = StringVar()
iskdinp = StringVar()

ism = Entry(root, textvariable=iskdinp)
bonp = Entry(root, textvariable=bonpinp)  # Ввод бонуса попадания
namehero = Entry(root, textvariable=nameinp)  # Вводи имени героя
hp = Entry(root, textvariable=hpinp)  # Ввод хп героя
kd = Entry(root, textvariable=kdinp)  # Ввод кд героя
hl = Entry(root, textvariable=hilinp)  # Ввод хила

revnab = Button(root, text="Добавить героя", font='Times 12', fg="#FFF8DC", command=nabhero)  # Кнопка +герой
endnab = Button(root, text='Закончить набор', font='Times 12', fg='#FFF8DC', command=choiceplace)  # Кнопка завершения
atackclick = Button(root, text='Атака', font='Times 18', fg='#FFF8DC', command=prdamage)  # Кнопка ОК
dmgclick = Button(root, text='Бам!', font='Times 18', fg='#FFF8DC', command=damage)  # Кнопка нанесения урона
hilclick = Button(root, text='Исцеление', font='Times 18', fg='#FFF8DC', command=hil)  # Кнопка исцеления
choiceclick = Button(root, text='OK', font='Times 18', fg='#FFF8DC', command=nextfaze)  # Кнопка продолжения
revclick = Button(root, text='↺', font='Times 11', width=3, fg='#FFF8DC', bg='#800000', command=rever)
revclickend = Button(root, text='↺', font='Times 40', width=3, fg='#FFF8DC', command=reverend)
otkat = Button(root, text='⟸', font='Times 11', fg='#FFF8DC', bg='#800000', command=otk)
dop = Button(root, text='Доп.действия', font='Times 11', fg='#FFF8DC', command=dopf)
pre = Button(root, text='Доп.ВА', font='Times 11', fg='#FFF8DC', command=pref)
inkd = Button(root, text='Изм.Кд', font='Times 11', fg='#FFF8DC', command=vkd)
ismkd = Button(root, text='⊚', font='Times 13', fg='#FFF8DC', bg='#800000', command=iskd)
ismkdpl = Button(root, text='+', font='Times 11', fg='#FFF8DC', bg='#800000', command=plus)
ismkdmn = Button(root, text='-', font='Times 11', fg='#FFF8DC', bg='#800000', command=minus)
prob = Button(root, text='➴', font='Times 11', fg='#FFF8DC', bg='#800000', command=probf)
atk = Button(root, text='Доп.атака', font='Times 11', fg='#FFF8DC', command=atkf)
elnab = Button(root, text='Доб.хар.', font='Times 11', fg='#FFF8DC', command=elnabf)
soprdmg = Button(root1, text='Доб.сопр', font='Times 11', fg='#FFF8DC', command=soprf)
uizdmg = Button(root1, text='Доб.уязв', font='Times 11', fg='#FFF8DC', command=uizf)
dpdmg = Button(root1, text='Доб.урон', font='Times 11', fg='#FFF8DC', command=dpdmg)

chlistbox = Listbox(root, height=3, width=20, selectmode=SINGLE)  # Список с героями

urbox = Listbox(root1, height=12, width=20, selectmode=SINGLE)
elbox = Listbox(root1, height=12, width=20, selectmode=SINGLE)

els = ['1.Колющий', '2.Рубящий', '3.Дробящий', '4.Кислотный', '5.Холодом', '6.Огненный', '7.Силовой', '8.Молнией',
       '9.Некротический', '10.Ядовитый', '11.Психический', '12.Свет']
ur = ['1.Колющий', '2.Рубящий', '3.Дробящий', '4.Кислотный', '5.Холодом', '6.Огненный', '7.Силовой', '8.Молнией',
      '9.Некротический', '10.Ядовитый', '11.Психический', '12.Свет']

for q in els:
    elbox.insert(END, q)

for y in ur:
    urbox.insert(END, y)

tp = IntVar()
tp.set(10)
pry = Radiobutton(root, text='Преим.', fg='#FFF8DC', bg='#800000', variable=tp, value=1)
pm = Radiobutton(root, text='Помех.', fg='#FFF8DC', bg='#800000', variable=tp, value=2)
pmn = Radiobutton(root, text='Норма.', fg='#FFF8DC', bg='#800000', variable=tp, value=0)

root.mainloop()
