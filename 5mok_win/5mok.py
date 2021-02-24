from collections import deque

#(row)열 인덱스 : 세로
rx = [-1, 1]
ry = [0, 0]
#(column)행 인덱스 : 가로
cx = [0, 0]
cy = [-1, 1]
#(diagonal)대각선 인덱스 : 
#(왼쪽에서 시작하는대각선)
ldx = [-1, 1]
ldy = [-1, 1]
#(오른쪽에서 시작하는 대각선)
rdx = [-1, 1]
rdy = [1, -1]


d1 = [
  [-1, 1],
  [0,  0],
  [-1, 1],
  [-1, 1]
]
d2 = [
  [0, 0],
  [-1, 1],
  [-1, 1],
  [1, -1]
]

def chcekReset():
  check = [[0]* 15 for _ in range(15)]

#바둑판 출력 
def printMap(map):
  for i in map:
    print(*i)
  print()

#현재 위치를 매개변수로 받음
#current index x, current index y 
def bfs(cx, cy):
  global n, m, findcnt
  for k in range(4):
    q = deque()    
    q.append([cx, cy ])
    check[cx][cy] = 1
    cnt = 1
    print("K:",k)
    while q:
      a, b = q.popleft()
      for i in range(2):
        x = a + d1[k][i]
        y = b + d2[k][i]
        if(0 <= x < n and 0 <= y < m):
          if(exArr[x][y] == 0):
            continue
          if(check[x][y] == 0):
            check[x][y] = 1
            cnt += 1
            print("cnt:",cnt)
            q.append([x, y])
        if cnt > 4:
          return str(exArr[x][y]) + " Win"
        # chcekReset()
    print("WHILE cnt:",cnt)


#check: 바둑판 자동생성 - 방문 확인용, 
#findcnt = 오목이면 5, 삼목이면 3
check = [[0]* 15 for _ in range(15)]
findcnt = 5
#바둑판 크기 (가로, 세로)
n, m = 15, 15
# 여러 경우를 테스트 해보기위해 직접 작성함
exArr = [
  [0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0], #0
  [1, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 0, 0, 0],#1
  [1, 1, 1, 1, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0],#2
  [1, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0],#3
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#4
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7],#5
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#6
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],#7
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3],#8
  [0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0],#9
  [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0],#10
  [0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 3, 3, 0, 0, 0],#11
  [0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 3, 0, 0, 0, 0],#12
  [0, 0, 0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 0],#13
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]#14
#  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
]


#클릭된 위치는 임의로 넣어주고 테스트

print("###########################3")

#세로줄 검사
print("\"세로 검사\", 1")
res = bfs(2,0)
print(res)

#가로줄 검사
print("\"가로 검사\",9 ")
res = bfs(1, 7)
print(res)

#왼쪽 대각선 검사
print("\"왼쪽 대각선 검사\", 5")
res = bfs(12, 6)
print(res)

#오른쪽 대각선검사
print("\"오른쪽 대각선 검사\", 3")
res = bfs(11,11)
print(res)

# 승리가 아닐 때
print("\"승리가 아닐 때\", 7")
res = bfs(5, 13)
print(res)

print("###########################3")