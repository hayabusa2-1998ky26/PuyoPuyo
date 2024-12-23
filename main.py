import tkinter
import random
import time
import _thread
import sys
# 画面作成
version = tkinter.Tcl().eval('info patchlevel')
root = tkinter.Tk()
canvas = tkinter.Canvas(width=1920, height=1080, bg="white")
canvas.pack()
root.title("PUYOPUYO")
key = ""
puyo1 = 0
puyo2 = 0
count1 = 0
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""
def puyo_down():
    global maps, putting, puyor, puyo1, puyo2, i, puyos1, puyos2
    maps[puyo1[0]][puyo1[1]] = 0
    maps[puyo2[0]][puyo2[1]] = 0
    serch_y = 1
    if maps[puyo1[0]][puyo1[1] + serch_y] == 0 and maps[puyo2[0]][puyo2[1] + serch_y] == 0:
        serch_y += 1
    else:
        putting = 1
    puyo1[1] = puyo1[1] + serch_y - 1
    puyo2[1] = puyo2[1] + serch_y - 1
    puyor[1] = puyor[1] + serch_y - 1
    maps[puyo1[0]][puyo1[1]] = puyos1[i]
    maps[puyo2[0]][puyo2[1]] = puyos2[i]
def put():
    global putting
    time.sleep(0.1)
    putting = 0
def byouga(puyo1, puyo2, maps_kotei, maps, falls):
    global count1, size, hold_puyo, hold_puyo2, next_puyo, next_puyo2, puyo, i
    all_base = 0 + size * (len(maps) + 1)
    try:
        canvas.delete("block")
        canvas.delete("label")
    except:
        print("finish!")
        sys.exit()
    s = 0
    if falls == "y":
        fall()
        s = erase()
    try:
        for x in range(8):
            for y in range(14):
                base_x = all_base - size * 6 + x*size
                if maps[x][y] == 9:
                    canvas.create_rectangle(base_x, y*size, base_x + size, y*size + size, fill="black", tag="block")
                if maps[x][y] == 0:
                    canvas.create_rectangle(base_x, y*size, base_x + size, y*size + size, fill="gray", tag="block")
                if maps[x][y] == 1:
                    canvas.create_rectangle(base_x, y*size, base_x + size, y*size + size, fill="red", tag="block")
                if maps[x][y] == 2:
                    canvas.create_rectangle(base_x, y*size, base_x + size, y*size + size, fill="yellow", tag="block")
                if maps[x][y] == 3:
                    canvas.create_rectangle(base_x, y*size, base_x + size, y*size + size, fill="green", tag="block")
                if maps[x][y] == 4:
                    canvas.create_rectangle(base_x, y*size, base_x + size, y*size + size, fill="purple", tag="block")
        canvas.create_rectangle(all_base - size * 6 + -3*size, 4*size, all_base - size * 6, 0, fill="gray", tag="block")
        canvas.create_rectangle(all_base - size * -2, 4*size, all_base - size * -5, 0, fill="gray", tag="block")
        canvas.create_text(all_base - size * 7.5, 1*size, text="Hold", font=("HG丸ｺﾞｼｯｸM-PRO",10), tag="label")
        canvas.create_text(all_base - size * -3.5, 1*size, text="Next", font=("HG丸ｺﾞｼｯｸM-PRO",10), tag="label")
        base = all_base - size * 6
        colors = ["", "red", "yellow", "green", "purple"]
        if hold_puyo != "":
            canvas.create_rectangle(base - 1.5*size, size*2.25, base - 2.0*size, size*2.75, fill=colors[hold_puyo], tag="block")
            canvas.create_rectangle(base - 1.0*size, size*2.25, base - 1.5*size, size*2.75, fill=colors[hold_puyo2], tag="block")
        base = all_base - size * -5
        if next_puyo != "":
            canvas.create_rectangle(base - 1.5*size, size*2.25, base - 2.0*size, size*2.75, fill=colors[next_puyo], tag="block")
            canvas.create_rectangle(base - 1.0*size, size*2.25, base - 1.5*size, size*2.75, fill=colors[next_puyo2], tag="block")
        try:
            serch_y = 1
            while True:
                if i == 0:
                    if (maps_kotei[puyo1[0]][puyo1[1] + serch_y + 1] == 0 or maps_kotei[puyo1[0]][puyo1[1] + serch_y + 1] == puyos1[i] or maps_kotei[puyo1[0]][puyo1[1] + serch_y + 1] == puyos2[i]):
                        serch_y += 1
                    else:
                        break
                else:
                    if maps_kotei[puyo1[0]][puyo1[1] + serch_y + 1] == 0:
                        serch_y += 1
                    else:
                        break
            puyo1g = list(tuple(puyo1))
            puyo1g[1] = puyo1[1] + serch_y
            serch_y = 1
            while True:
                if i == 0:
                    if (maps_kotei[puyo2[0]][puyo2[1] + serch_y + 1] == 0 or maps_kotei[puyo2[0]][puyo2[1] + serch_y + 1] == puyos2[i] or maps_kotei[puyo2[0]][puyo2[1] + serch_y + 1] == puyos1[i]):
                        serch_y += 1
                    else:
                        break
                else:
                    if maps_kotei[puyo2[0]][puyo2[1] + serch_y + 1] == 0:
                        serch_y += 1
                    else:
                        break
            puyo2g = list(tuple(puyo2))
            puyo2g[1] = puyo2[1] + serch_y
            x = [puyo1g[0], puyo2g[0]]
            y = [puyo1g[1], puyo2g[1]]
            if x[0] == x[1] and y[0] == y[1]:
                if puyo1[1] > puyo2[1]:
                    y[1] = y[1] - 1
                else:
                    y[0] = y[0] - 1
            j = i
            if falls == "y" or falls == "screen":
                for k in range(2):
                    if maps[x[k]][y[k]] == 0:
                        base_x = all_base - size * 6 + x[k]*size
                        if puyos1[j] == 1 and k == 0:
                            canvas.create_rectangle(base_x + 10, y[k]*size + 10, base_x + size - 10, y[k]*size + size - 10, fill="red", tag="block")
                        if puyos1[j] == 2 and k == 0:
                            canvas.create_rectangle(base_x + 10, y[k]*size + 10, base_x + size - 10, y[k]*size + size - 10, fill="yellow", tag="block")
                        if puyos1[j] == 3 and k == 0:
                            canvas.create_rectangle(base_x + 10, y[k]*size + 10, base_x + size - 10, y[k]*size + size - 10, fill="green", tag="block")
                        if puyos1[j] == 4 and k == 0:
                            canvas.create_rectangle(base_x + 10, y[k]*size + 10, base_x + size - 10, y[k]*size + size - 10, fill="purple", tag="block")
                        if puyos2[j] == 1 and k == 1:
                            canvas.create_rectangle(base_x + 10, y[k]*size + 10, base_x + size - 10, y[k]*size + size - 10, fill="red", tag="block")
                        if puyos2[j] == 2 and k == 1:
                            canvas.create_rectangle(base_x + 10, y[k]*size + 10, base_x + size - 10, y[k]*size + size - 10, fill="yellow", tag="block")
                        if puyos2[j] == 3 and k == 1:
                            canvas.create_rectangle(base_x + 10, y[k]*size + 10, base_x + size - 10, y[k]*size + size - 10, fill="green", tag="block")
                        if puyos2[j] == 4 and k == 1:
                            canvas.create_rectangle(base_x + 10, y[k]*size + 10, base_x + size - 10, y[k]*size + size - 10, fill="purple", tag="block")
        except:
            a = 0
        canvas.update()
        count1 += 1
    except:
        print("Finish!")
        sys.exit()
    try:
        time.sleep(max(s, 0))
    except:
        a = 0
def make_puyo():
    global puyo1, puyo2, maps, puyor, puyos1, puyos2
    puyor = [3, 1]
    puyo1 = [3, 1]
    puyo2 = [4, 1]
    maps[3][1] = puyos1[i]
    maps[4][1] = puyos2[i]
def nanimosinai():
    aaa = 0
def fall():
    global maps, putting, puyor, maps_kotei, erased, puyo1, puyo2
    if putting == 1:
        tates = tateyoko(maps)
        i = 0
        erases = 1
        while True:
            erases -= 1
            for x in reversed(range(len(tates))):
                for y in range(len(tates[x])):
                    if tates[x][y] != 0 and tates[x][y] != 9:
                        if tates[x + 1][y] == 0:
                            maps3 = tateyoko(tates)
                            byouga(puyo1, puyo2, maps_kotei, maps3, "n")
                            tates[x][y], tates[x + 1][y] = tates[x + 1][y], tates[x][y]
                            erases = 1
            if erases > 0:
                time.sleep(0.1)
            if erases == 0:
                break
        maps = tateyoko(tates)
def erase():
    global putting, puyor, erased, maps, erasea
    if erasea > 0:
        fall()
    maps2 = copy(maps)
    if putting == 1:
        erasea = 0
        for y in range(len(maps2)):
            for x in range(len(maps2[y])):
                if maps2[y][x] != 0 and maps2[y][x] != 9 and maps2[y][x] != "*":
                    p = [[y, x]]
                    watch = 0
                    if maps2[y][x] == 1:
                        watch = 1
                    elif maps2[y][x] == 2:
                        watch = 2
                    elif maps2[y][x] == 3:
                        watch = 3
                    elif maps2[y][x] == 4:
                        watch = 4
                    else:
                        print(maps[y][x])
                    count = 1
                    maps2[y][x] = "*"
                    p_hozon = [[y, x]]
                    while True:
                        for l in range(len(p)):
                            if p[l] != []:
                                can = 0
                                if p[l][0] != 1 and maps2[p[l][0]][p[l][1] - 1] == watch:
                                    can = 1
                                    count += 1
                                    maps2[p[l][0]][p[l][1] - 1] = "*"
                                    p.append([p[l][0], p[l][1] - 1])
                                    p_hozon.append([p[l][0], p[l][1] - 1])
                                if p[l][1] != 1 and maps2[p[l][0] - 1][p[l][1]] == watch:
                                    can = 1
                                    count += 1
                                    maps2[p[l][0] - 1][p[l][1]] = "*"
                                    p.append([p[l][0] - 1, p[l][1]])
                                    p_hozon.append([p[l][0] - 1, p[l][1]])
                                if p[l][0] != len(maps2) - 1 and maps2[p[l][0]][p[l][1] + 1] == watch:
                                    can = 1
                                    count += 1
                                    maps2[p[l][0]][p[l][1] + 1] = "*"
                                    p.append([p[l][0], p[l][1] + 1])
                                    p_hozon.append([p[l][0], p[l][1] + 1])
                                if p[l][1] != len(maps2[y]) - 1 and maps2[p[l][0] + 1][p[l][1]] == watch:
                                    can = 1
                                    count += 1
                                    maps2[p[l][0] + 1][p[l][1]] = "*"
                                    p.append([p[l][0] + 1, p[l][1]])
                                    p_hozon.append([p[l][0] + 1, p[l][1]])
                                if can != 1:
                                    p[l] = []
                                #debug(maps2)
                                
                        if p.count([]) == len(p):
                            break
                    if count >= 4:
                        for a in range(len(p_hozon)):
                            maps[p_hozon[a][0]][p_hozon[a][1]] = 0
                        byouga(puyo1, puyo2, maps_kotei, maps, "n")
                        time.sleep(0.5)
                        fall()
                        erase()
                        erasea = 2
                        if len(p_hozon) != 0:
                            return 0
                        else:
                            return 0
def hold():
    global maps, hold_puyo, hold_puyo2, i, puyo, puyo1, puyo2, holding, break_
    break_ = 1
    if holding != i:
        maps[puyo1[0]][puyo1[1]] = 0
        maps[puyo2[0]][puyo2[1]] = 0
        puyo1[1] = 5
        puyo2[1] = 5
        if hold_puyo != "":
            puyos1[i], hold_puyo = hold_puyo, puyos1[i]
            puyos2[i], hold_puyo2 = hold_puyo2, puyos2[i]
            holding = i
            i -= 1
        else:
            hold_puyo = puyos1[i]
            hold_puyo2 = puyos2[i]
            holding = i + 1
    else:
        break_ = 0
def debug(list1):
    for aaa in range(len(list1)):
        print(list1[aaa])
def copy(list1):
    return1 = []
    for y in range(len(list1)):
        return1.append([])
        for x in range(len(list1[y])):
            return1[y].append(list1[y][x])
    return return1
def tateyoko(map1):
    tates = []
    for i in range(len(map1[0])):
        tate = []
        for j in range(len(map1)):
            tate.append(map1[j][i])
        tates.append(tate)
    return tates
size = 50
erasea = 0
maps = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9]
]
game_over = 0
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
putting = 0
puyor = []
hold_puyo = ""
hold_puyo2 = ""
next_puyo = ""
next_puyo2 = ""
holding = -1
erased = 0
break_ = 0
while True:
    if game_over == 1:
        break
    serch_y = 0
    serch_x = 0
    puyos1 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    puyos2 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    random.shuffle(puyos1)
    random.shuffle(puyos2)
    i = -1
    while True:
        i += 1
        if len(puyos1) - i < 5:
            puyo_ = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
            random.shuffle(puyo_)
            for j in range(7):
                puyos1.append(puyo_[j])
            puyo_ = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
            random.shuffle(puyo_)
            for j in range(7):
                puyos2.append(puyo_[j])
        if break_ != 1:
            maps_kotei = maps.copy()
            root.after(0, byouga(puyo1, puyo2, maps_kotei, maps, "y"))
            maps_kotei = maps.copy()
            root.after(20, byouga(puyo1, puyo2, maps_kotei, maps, "y"))
        break_ = 0
        putting = 0
        stop = 0
        if game_over == 1:
            break
        make_puyo()
        t_down_lock = 0
        time.sleep(0.02)
        t_down = time.time()
        putting = 0
        while True:
            before_key = key
            if time.time() - t_down > 1:
                t_down = time.time()
                puyo_down()
            if putting == 1:
                break
            if game_over == 1:
                break
            while key == "Up":
                root.after(20, byouga(puyo1, puyo2, maps_kotei, maps, "y"))
            fps1 = time.time()
            root.after(20, byouga(puyo1, puyo2, maps_kotei, maps, "y"))
            next_puyo = puyos1[i + 1]
            next_puyo2 = puyos2[i + 1]
            if key == "p":
                canvas.create_text(960, 540, text="Pause", font=("HG丸ｺﾞｼｯｸM-PRO",10), tag="label")
                canvas.update()
                print("Hi")
                time.sleep(0.5)
                print("yes")
                while True:
                    time.sleep(0.1)
                    if key == "p":
                        break
                print("Succeses")
            if key == "Up":
                maps[puyo1[0]][puyo1[1]] = 0
                maps[puyo2[0]][puyo2[1]] = 0
                serch_y = 0
                while True:
                    if maps[puyo1[0]][puyo1[1] + serch_y] == 0 and maps[puyo2[0]][puyo2[1] + serch_y] == 0:
                        serch_y += 1
                    else:
                        break
                puyo1[1] = puyo1[1] + serch_y - 1
                puyo2[1] = puyo2[1] + serch_y - 1
                puyor[1] = puyor[1] + serch_y - 1
                maps[puyo1[0]][puyo1[1]] = puyos1[i]
                maps[puyo2[0]][puyo2[1]] = puyos2[i]
                putting = 1
                break
            if key == "Down":
                maps[puyo1[0]][puyo1[1]] = 0
                maps[puyo2[0]][puyo2[1]] = 0
                serch_y = 1
                if maps[puyo1[0]][puyo1[1] + serch_y] == 0 and maps[puyo2[0]][puyo2[1] + serch_y] == 0:
                    serch_y += 1
                else:
                    if t_down_lock != 1:
                        t_down = time.time()
                        t_down_lock = 1
                puyo1[1] = puyo1[1] + serch_y - 1
                puyo2[1] = puyo2[1] + serch_y - 1
                puyor[1] = puyor[1] + serch_y - 1
                maps[puyo1[0]][puyo1[1]] = puyos1[i]
                maps[puyo2[0]][puyo2[1]] = puyos2[i]
            if key == "Right":
                serch_x = 1
                maps[puyo1[0]][puyo1[1]] = 0
                maps[puyo2[0]][puyo2[1]] = 0
                if maps[puyo1[0] + serch_x][puyo1[1]] == 0 and maps[puyo2[0] + serch_x][puyo2[1]] == 0:
                    serch_x = 1
                else:
                    serch_x = 0
                puyo1[0] = puyo1[0] + serch_x
                puyo2[0] = puyo2[0] + serch_x
                puyor[0] = puyor[0] + serch_x
                maps[puyo1[0]][puyo1[1]] = puyos1[i]
                maps[puyo2[0]][puyo2[1]] = puyos2[i]
                byouga(puyo1, puyo2, maps_kotei, maps, "screen")
                time.sleep(0.1)
            if key == "Left":
                serch_x = -1
                maps[puyo1[0]][puyo1[1]] = 0
                maps[puyo2[0]][puyo2[1]] = 0
                if maps[puyo1[0] + serch_x][puyo1[1]] == 0 and maps[puyo2[0] + serch_x][puyo2[1]] == 0:
                    serch_x = -1
                else:
                    serch_x = 0
                puyo1[0] = puyo1[0] + serch_x
                puyo2[0] = puyo2[0] + serch_x
                puyor[0] = puyor[0] + serch_x
                maps[puyo1[0]][puyo1[1]] = puyos1[i]
                maps[puyo2[0]][puyo2[1]] = puyos2[i]
                byouga(puyo1, puyo2, maps_kotei, maps, "screen")
                time.sleep(0.1)
            if key == "z" and key != before_key:
                try:
                    a = 0
                    maps[puyo1[0]][puyo1[1]] = 0
                    maps[puyo2[0]][puyo2[1]] = 0
                    puyo1_sa_x, puyo1_sa_y = puyo1[0] - puyor[0], puyo1[1] - puyor[1]
                    puyo2_sa_x, puyo2_sa_y = puyo2[0] - puyor[0], puyo2[1] - puyor[1]
                    puyo1[0], puyo1[1] = puyor[0] + puyo1_sa_y, puyor[1] - puyo1_sa_x
                    puyo2[0], puyo2[1] = puyor[0] + puyo2_sa_y, puyor[1] - puyo2_sa_x
                    if maps[puyor[0] + puyo1_sa_y][puyor[1] - puyo1_sa_x] == 0 and maps[puyor[0] + puyo2_sa_y][puyor[1] - puyo2_sa_x] == 0:
                        a = 1
                    puyo1a = puyo1.copy()
                    puyo2a = puyo2.copy()
                    puyora = puyor.copy()
                    if puyo2[0] - puyo1[0] == 1 and a == 0:
                        puyo2a[0] += -1
                        puyo1a[0] += -1
                        puyora[0] += -1
                    if puyo2[0] - puyo1[0] == -1 and a == 0:
                        puyo2a[0] += 1
                        puyo1a[0] += 1
                        puyora[0] += 1
                    if puyo2[1] - puyo1[1] == 1 and a == 0:
                        puyo2a[1] += -1
                        puyo1a[1] += -1
                        puyora[1] += -1
                    if puyo2[1] - puyo1[1] == -1 and a == 0:
                        puyo2a[1] += 1
                        puyo1a[1] += 1
                        puyora[1] += 1
                    if maps[puyo2a[0]][puyo2a[1]] != 0:
                        puyo1_sa_x, puyo1_sa_y = puyo1[0] - puyor[0], puyo1[1] - puyor[1]
                        puyo2_sa_x, puyo2_sa_y = puyo2[0] - puyor[0], puyo2[1] - puyor[1]
                        puyo1[0], puyo1[1] = puyor[0] - puyo1_sa_y, puyor[1] + puyo1_sa_x
                        puyo2[0], puyo2[1] = puyor[0] - puyo2_sa_y, puyor[1] + puyo2_sa_x
                    else:
                        puyo1, puyo2, puyor = puyo1a.copy(), puyo2a.copy(), puyora.copy()
                    maps[puyo1[0]][puyo1[1]] = puyos1[i]
                    maps[puyo2[0]][puyo2[1]] = puyos2[i]
                    byouga(puyo1, puyo2, maps_kotei, maps, "y")
                except:
                    a = 0
            if key == "x" and key != before_key:
                try:
                    a = 0
                    maps[puyo1[0]][puyo1[1]] = 0
                    maps[puyo2[0]][puyo2[1]] = 0
                    puyo1_sa_x, puyo1_sa_y = puyo1[0] - puyor[0], puyo1[1] - puyor[1]
                    puyo2_sa_x, puyo2_sa_y = puyo2[0] - puyor[0], puyo2[1] - puyor[1]
                    puyo1[0], puyo1[1] = puyor[0] - puyo1_sa_y, puyor[1] + puyo1_sa_x
                    puyo2[0], puyo2[1] = puyor[0] - puyo2_sa_y, puyor[1] + puyo2_sa_x
                    if maps[puyor[0] - puyo1_sa_y][puyor[1] + puyo1_sa_x] == 0 and maps[puyor[0] - puyo2_sa_y][puyor[1] + puyo2_sa_x] == 0:
                        a = 1
                    puyo1a = puyo1.copy()
                    puyo2a = puyo2.copy()
                    puyora = puyor.copy()
                    if puyo2[0] - puyo1[0] == 1 and a == 0:
                        puyo2a[0] += -1
                        puyo1a[0] += -1
                        puyora[0] += -1
                    if puyo2[0] - puyo1[0] == -1 and a == 0:
                        puyo2a[0] += 1
                        puyo1a[0] += 1
                        puyora[0] += 1
                    if puyo2[1] - puyo1[1] == 1 and a == 0:
                        puyo2a[1] += -1
                        puyo1a[1] += -1
                        puyora[1] += -1
                    if puyo2[1] - puyo1[1] == -1 and a == 0:
                        puyo2a[1] += 1
                        puyo1a[1] += 1
                        puyora[1] += 1
                    if maps[puyo2a[0]][puyo2a[1]] != 0:
                        puyo1_sa_x, puyo1_sa_y = puyo1[0] - puyor[0], puyo1[1] - puyor[1]
                        puyo2_sa_x, puyo2_sa_y = puyo2[0] - puyor[0], puyo2[1] - puyor[1]
                        puyo1[0], puyo1[1] = puyor[0] + puyo1_sa_y, puyor[1] - puyo1_sa_x
                        puyo2[0], puyo2[1] = puyor[0] + puyo2_sa_y, puyor[1] - puyo2_sa_x
                    else:
                        puyo1, puyo2, puyor = puyo1a.copy(), puyo2a.copy(), puyora.copy()
                    maps[puyo1[0]][puyo1[1]] = puyos1[i]
                    maps[puyo2[0]][puyo2[1]] = puyos2[i]
                    byouga(puyo1, puyo2, maps_kotei, maps, "y")
                except:
                    a = 0
            if key == "c" and key != before_key:
                break_ = 0
                hold()
                if break_ == 1:
                    break
        if puyo1[1] < 1 or puyo2[1] < 1:
            game_over = 1
byouga(puyo1, puyo2, maps_kotei, maps, "y")
print("game over")