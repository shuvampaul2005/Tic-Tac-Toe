from tkinter import *
from time import sleep
from random import randint

allPossible = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')


def Map(char):
    if char == 'A1': h,k = 30,30
    elif char == 'B1': h,k = 30, 167+30
    elif char == 'C1': h,k = 30, 167*2-10+30
    elif char == 'A2': h,k = 167+30,30
    elif char == 'B2': h,k = 167+30,167+30
    elif char == 'C2': h,k = 167+30,167*2-10+30
    elif char == 'A3': h,k = 167*2-10+30,30
    elif char == 'B3': h,k = 167*2-10+30,167+30
    elif char == 'C3': h,k = 167*2-10+30,167*2-10+30

    return h,k

def OppositeOfMode(p):
    l=[];o =[];v=[]
    for i in p:
        if i not in l:
            l.append(i)
    for i in l:
        f = p.count(i)
        v.append(f)
    f = min(v)
    for i in l:
        if p.count(i) == f and i not in o:
            o.append(i)
    return o[randint(0, len(o)-1)]

def Mode(p):
    l=[];o =[];v=[]
    for i in p:
        if i not in l:
            l.append(i)
    for i in l:
        f = p.count(i)
        v.append(f)
    if len(v) == 0:
        return None
    else:
        f = max(v)
        for i in l:
            if p.count(i) == f and i not in o:
                o.append(i)
        if len(o) >= 5:
            return None
        else:
            return o[randint(0, len(o)-1)]



def ComputerMove(moveSeq):
    good = []; bad = []; follow = [];avoid=[]

    g = open('Owin.txt','r')
    good0 = g.read().split('\n')
    g.close()

    for i in good0:
        if len(i) > 1 and i[0] == '[':
            f = eval(i)
            good.append(f)
    #got the list called good

    g = open('Xwin.txt', 'r')
    bad0 = g.read().split('\n')
    g.close()

    for i in bad0:
        if len(i) > 1 and i[0] == '[':
            f = eval(i)
            bad.append(f)
    #got the list called bad

    for i in good:
        if len(i)>len(moveSeq) and moveSeq == i[0:len(moveSeq)]: 
            follow.append(i[len(moveSeq)])

    for i in bad:
        if len(i)>len(moveSeq) and moveSeq == i[0:len(moveSeq)]:
            avoid.append(i[len(moveSeq)])

    possible = list(allPossible)
    for i in moveSeq:
        possible.remove(i)
    
    poss = list(possible)
    for i in avoid:
        try: poss.remove(i)
        except: pass

    c = Mode(follow)
    if c == None:
        try: c = poss[randint(0, len(poss)-1)]
        except: c = OppositeOfMode(avoid)
    return c
            

def Experience(data, w):
    if w == "Computer":
        good=[]
        g = open("Owin.txt", "r")
        good0 = g.read().split('\n')
        g.close()

        for i in good0:
            if len(i) > 1 and i[0] == "[":
                f = eval(i)
                good.append(f)
        
        f = open("Owin.txt", "a")
        if data not in good:
            f.write(str(data) + '\n')
        f.close()

    elif w == "Player":
        bad=[]
        b = open("Xwin.txt", "r")
        bad0 = b.read().split('\n')
        b.close()

        for i in bad0:
            if len(i) > 1 and i[0] == "[":
                f = eval(i)
                bad.append(f)
        
        f = open("Xwin.txt", "a")
        if data not in bad:
            f.write(str(data) + '\n')
        f.close()
    else:
        pass


def winCheck(gridValue, moveSeq):
    allPossible = set( ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3') )

    condition = gridValue["A1"]==gridValue["A2"]==gridValue["A3"]=="X" or gridValue["A1"]==gridValue["A2"]==gridValue["A3"]=="O" \
                or gridValue["B1"]==gridValue["B2"]==gridValue["B3"]=="X" or gridValue["B1"]==gridValue["B2"]==gridValue["B3"]=="O" \
                or gridValue["C1"]==gridValue["C2"]==gridValue["C3"]=="X" or gridValue["C1"]==gridValue["C2"]==gridValue["C3"]=="O" \
                or gridValue["A1"]==gridValue["B1"]==gridValue["C1"]=="X" or gridValue["A1"]==gridValue["B1"]==gridValue["C1"]=="O" \
                or gridValue["A2"]==gridValue["B2"]==gridValue["C2"]=="X" or gridValue["A2"]==gridValue["B2"]==gridValue["C2"]=="O" \
                or gridValue["A3"]==gridValue["B3"]==gridValue["C3"]=="X" or gridValue["A3"]==gridValue["B3"]==gridValue["C3"]=="O" \
                or gridValue["A1"]==gridValue["B2"]==gridValue["C3"]=="X" or gridValue["A1"]==gridValue["B2"]==gridValue["C3"]=="O"\
                or gridValue["A3"]==gridValue["B2"]==gridValue["C1"]=="X" or gridValue["A3"]==gridValue["B2"]==gridValue["C1"]=="O"

    if condition and gridValue[moveSeq[-1]] == 'X':
        winner = 'Player'
    elif condition and gridValue[moveSeq[-1]] == 'O':
        winner = 'Computer'
    elif not condition and allPossible == set(moveSeq):
        winner = 'Draw'
    else:
        winner = 'undefined'
    return winner

    
def Start(scr, cv, hl,vl, B, X, gridValue, moveSeq, screen2):
    screen2.grab_release()
    screen2.destroy()
    NewGame(scr, cv, hl,vl, B, X, gridValue, moveSeq)


def Pics(cpic, ppic, dpic, qpic, npic, opic):
    global c, p, d, q, n, O
    c, p, d, q, n, O = cpic, ppic, dpic, qpic, npic, opic
    


def EndGame(scr, cv, hl, vl, B, X, gridValue, moveSeq, win):
    gridValue = {'A1':'', 'A2':'', 'A3':'', 'B1':'', 'B2':'', 'B3':'', 'C1':'', 'C2':'', 'C3':''}
    moveSeq.clear()

    if win == 'Computer':
        screen2 = Toplevel(scr)
        screen2.geometry('500x500')
        screen2.title(win+' Wins')
        screen2.grab_set()
        m = Label(screen2, image = c)
    elif win == 'Player':
        screen2 = Toplevel(scr)
        screen2.geometry('500x500')
        screen2.title(win+' Wins')
        screen2.grab_set()
        m = Label(screen2, image = p)
    elif win == 'Draw':
        screen2 = Toplevel(scr)
        screen2.geometry('500x500')
        screen2.title(win)
        screen2.grab_set()
        m = Label(screen2, image = d)
    m.place(x = 0, y = 0)

    bq = Button(screen2, image = q, command = quit)
    bq.place(x = 57, y = 354)

    bn = Button(screen2, image = n, command = lambda: Start(scr, cv, hl, vl, B, X, gridValue, moveSeq, screen2))
    bn.place(x = 250 + 57, y = 354)






def cmd(h, v, p, X, gridValue, moveSeq, cv, hl, vl, scr, B):
    print(p)
    sym = Label(cv, image = X).place(x = h, y = v)
    gridValue[p] = 'X' 
    moveSeq.append(p)

    whoWin = winCheck(gridValue, moveSeq)

    if whoWin != 'undefined':
        print('game end')
        Experience(moveSeq, whoWin)
        EndGame(scr, cv, hl, vl, B, X, gridValue, moveSeq, whoWin)
    else:
        cMove = ComputerMove(moveSeq)
        xVal, yVal = Map(cMove)
        sym = Label(cv,  image = O).place(x = xVal, y = yVal)
        gridValue[cMove] = 'O'
        moveSeq.append(cMove)

        whoWin =  winCheck(gridValue, moveSeq)

        if whoWin != 'undefined':
            print('game end')
            Experience(moveSeq, whoWin)
            EndGame(scr, cv, hl, vl, B, X, gridValue, moveSeq, whoWin)
        

def NewGame(scr, cv, hl, vl, B, X, grid, moves):
    cv.destroy()
    cv = Canvas(scr, width = 500, height = 500)
    cv.pack()

    b1 = Label(cv, image = vl)
    b1.place(x = 167, y = 0)
    b2 = Label(cv, image = vl)
    b2.place(x = 167*2 - 10, y = 0)
    b3 = Label(cv, image = hl)
    b3.place(x = 0, y = 167)
    b4 = Label(cv, image = hl)
    b4.place(x = 167, y = 167)
    b5 = Label(cv, image = hl)
    b5.place(x = 167*2 - 10, y = 167)
    b6 = Label(cv, image = vl)
    b6.place(x = 167, y = 167)
    b7 = Label(cv, image = vl)
    b7.place(x = 167*2 - 10, y = 167)
    b8 = Label(cv, image = hl)
    b8.place(x = 0, y = 167*2 - 10)
    b9 = Label(cv, image = hl)
    b9.place(x = 167, y = 167*2 - 10)
    b10 = Label(cv, image = hl)
    b10.place(x = 167*2 - 10, y = 167*2 - 10)
    b11 = Label(cv, image = vl)
    b11.place(x = 167, y = 167*2 - 10)
    b12 = Label(cv, image = vl)
    b12.place(x = 167*2 - 10, y = 167*2 - 10)

    A1 = Button(cv, image = B, command = lambda: cmd(30,30, 'A1', X, grid, moves, cv, hl, vl, scr, B))
    A1.place(x = 30, y = 30)

    A2 = Button(cv, image = B, command = lambda: cmd(167 + 30,30, 'A2', X, grid, moves, cv, hl, vl, scr, B))
    A2.place(x = 167 + 30, y = 30)

    A3 = Button(cv, image = B, command = lambda: cmd(167*2 - 10 + 30,30, 'A3', X, grid, moves, cv, hl, vl, scr, B))
    A3.place(x = 167*2 - 10 + 30, y = 30)

    B1 = Button(cv,  image = B, command = lambda: cmd(30,167+30, 'B1', X, grid, moves, cv, hl, vl, scr, B))
    B1.place(x = 30, y = 167 + 30)

    B2 = Button(cv, image = B, command = lambda: cmd(167+30,167+30, 'B2', X, grid, moves, cv, hl, vl, scr, B))
    B2.place(x = 167 + 30, y = 167+30)

    B3 = Button(cv, image = B, command = lambda: cmd(167*2 - 10 + 30,167+30, 'B3', X, grid, moves, cv, hl, vl, scr, B))
    B3.place(x = 167*2 - 10 + 30, y = 167+30)

    C1 = Button(cv, image = B, command = lambda: cmd(30,167*2 - 10 + 30, 'C1', X, grid, moves, cv, hl, vl, scr, B))
    C1.place(x = 30, y = 167*2 - 10 + 30)

    C2 = Button(cv,  image = B, command = lambda: cmd(167+30,167*2 - 10 + 30, 'C2', X, grid, moves, cv, hl, vl, scr, B))
    C2.place(x = 167 + 30, y = 167*2 - 10 + 30)

    C3 = Button(cv, image = B, command = lambda: cmd(167*2 - 10 + 30, 167*2 - 10 + 30, 'C3', X, grid, moves, cv, hl, vl, scr, B))
    C3.place(x = 167*2 - 10 + 30, y = 167*2 - 10 + 30)

