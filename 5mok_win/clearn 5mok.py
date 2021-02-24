from collections import deque

dx = [[-1, 1], [0, 0], [-1, 1], [-1, 1]]
dy = [[0, 0], [-1, 1], [-1, 1], [1, -1]]

def isWin(curX, curY):
  global sizeN, sizeM, stoneNum
  stoneNum -= 1
  stoneColor = Map[curX][curY]
  for k in range(4):
    q = deque()    
    q.append([curX, curY])
    check[curX][curY] = 1
    cnt = 1
    while q:
      a, b = q.popleft()
      for i in range(2):
        x = a + dx[k][i]
        y = b + dy[k][i]
        if 0 <= x < sizeN and 0 <= y < sizeM:
          if Map[x][y] != stoneColor:
            continue
          if check[x][y] == 0:
            check[x][y] = 1
            cnt += 1
            q.append([x, y])
        if cnt > stoneNum:
          return str(Map[x][y]) + " Win"

# stoneNum:최소 몇개부터 승리 판정을 할지 정함 ex) 3목 = 3, 5목 = 5, 7목 = 7
# sizeN - M : 바둑판의 가로. 세로 사이즈 
check = [[0]* 15 for _ in range(15)]
stoneNum = 5
sizeN, sizeM = 15, 15
Map = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0
  [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],#1
  [0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],#2
  [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],#3
  [0, 0, 0, 0, 7, 4, 0, 0, 4, 4, 0, 0, 0, 0, 0],#4
  [0, 0, 0, 7, 4, 4, 7, 0, 7, 4, 0, 0, 0, 0, 0],#5
  [0, 0, 4, 0, 4, 4, 4, 7, 7, 4, 0, 0, 0, 0, 0],#6
  [0, 0, 0, 0, 0, 4, 7, 4, 7, 4, 0, 0, 0, 0, 0],#7
  [0, 0, 0, 0, 0, 7, 0, 0, 7, 7, 0, 0, 0, 0, 0],#8
  [0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 7, 0, 0, 0, 0],#9
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#10
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#11
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#12
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#13
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]#14
  #0 #1 #2 #3 #4 #5 #6 #7 #8 #9 #10#11#12#13#14
]
print(isWin(8, 9))
