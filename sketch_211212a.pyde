import random

x = 1
zerop = []
squares2 =  [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
#squares2 =  [[2, 8, 3], [1, 0, 4], [7, 6, 5]]
goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
#goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
results = []
check = [10 for i in range(1000)]

"""n = 0
for i in range(3) : 
    for j in range(3) :
        if i!=1 or j!=1 :
           squares[i][j] = arr[n]
           n = n + 1
        else :
            squares[i][j] = 0"""

def afficher(arr) :
    for i in range(3) :
        for j in range(3) :
            print(arr[i][j],)
        print()
class Puzz :
    def __init__(self, g, dirc, h, pth, result) :
        self.g = g
        self.dirc = dirc
        self.h = h
        self.pth = pth
        self.result = result
def copy(arr1, arr2) :
    for i in range(3) :
        for j in range(3) :
            arr1[i][j] = arr2[i][j]
def CalculeH(squares, goal) :
    h = 0
    for i in range(3) :
        for j in range(3) :
            if (squares[i][j] != goal[i][j] and squares[i][j] != 0) :
                h = h + 1
    return h
def zero(squares) :
    for i in range(3) :
        for j in range(3) :
            if squares[i][j] == 0 :
                break
        else : 
            continue
        break
    del zerop[:]
    zerop.append(i)
    zerop.append(j)
def MovingDir (Puz) :
    dir = []
    for i in range(3) :
        for j in range(3) :
            if Puz.result[i][j] == 0 :
                break
        else : 
            continue
        break 
    if i == 0 :
        dir.append('D')
    elif i == 2 :
        dir.append('U')
    else :
        dir.append('D')
        dir.append('U')
    
    if j == 0 :
        dir.append('R')
    elif j == 2 :
        dir.append('L')
    else :
        dir.append('R')
        dir.append('L')
    for d in dir[:] :
        if (Puz.dirc == 'L') and d=='R':
            dir.remove(d)
        elif (Puz.dirc == 'R') and d=='L':
            dir.remove(d)
        elif (Puz.dirc == 'U') and d=='D':
            dir.remove(d)
        elif (Puz.dirc == 'D') and d=='U':
            dir.remove(d)


    return dir
def Move(c,squares) :
    temp = [[0 for x in range(3)] for y in range(3)]
    copy(temp, squares)
    i = 0
    zero(squares)
    if c == 'D' :
        i = temp[zerop[0]][zerop[1]]
        temp[zerop[0]][zerop[1]] = temp[zerop[0]+1][zerop[1]]
        temp[zerop[0]+1][zerop[1]] = i
    elif c == 'U' :
        i = temp[zerop[0]][zerop[1]]
        temp[zerop[0]][zerop[1]] = temp[zerop[0]-1][zerop[1]]
        temp[zerop[0]-1][zerop[1]] = i
    elif c == 'R' :
        i = temp[zerop[0]][zerop[1]]
        temp[zerop[0]][zerop[1]] = temp[zerop[0]][zerop[1]+1]
        temp[zerop[0]][zerop[1]+1] = i
    else : 
        i = temp[zerop[0]][zerop[1]]
        temp[zerop[0]][zerop[1]] = temp[zerop[0]][zerop[1]-1]
        temp[zerop[0]][zerop[1]-1] = i
    return temp
def PathCalc(Puz) :
    h = 10
    path = ""
    squares = Puz.result
    pth = Puz.pth
    g = int(len(pth)/2)
    for Dir in MovingDir(Puz) :
        th = CalculeH(Move(Dir,squares),goal)
        if h >= th :
           h = th
           path = pth + Dir
           results.append(Puzz(g, Dir, h, path, Move(Dir,squares)))

    if check[g] > h :
       check[g] = h
    for res in results[:] :
        if res.h > check[g] and res.g == g:
            results.remove(res)
    return h


    for res in results[:] :
        if res.h < Puzz.h and res.g == Puzz.g:
            results.remove(Puzz)
            return 0
    return 1
    
results.append(Puzz(0,"",0,"",squares2))
h=1
while h :
   h = PathCalc(results.pop(0))

fpath = list(results.pop(0).pth)
result = []
result.append(squares2)
for fp in fpath :
      squares2 = Move(fp, squares2)
      result.append(squares2)

def setup() :
    background(255,255,255)
    size(303,303)

def draw() :    
    if len(result) :
       rs = result.pop(0)
    else :
       rs = goal
    for i in range(3) :
        for j in range(3) :
            fill(255,255,255)
            square(i*101,j*101,100)
            if rs[j][i]!=0 :
               fill(0,0,0)
               textSize(50);
               if len(result):
                  text(rs[j][i], i*101+35, 101*j+65)
               else :
                  text(goal[j][i], i*101+35, 101*j+65)
    delay(1000)
