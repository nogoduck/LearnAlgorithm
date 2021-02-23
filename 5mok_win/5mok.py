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

#바둑판 출력 
def printMap(map):
  for i in map:
    print(*i)
  print()

#현재 위치를 매개변수로 받음
#current index x, current index y 
def bfs(cx, cy):
  global n, m, findcnt
  q = deque() 
  q.append([cx, cy])
  check[cx][cy] = 1
  cnt = 1
  while q:
    a, b = q.popleft()
    for i in range(2):
      x = a + rx[i]
      y = b + ry[i]
      if(0 <= x < n and 0 <= y < m):
        if(exArr[x][y] == 0):
          continue
        if(check[x][y] == 0):
          check[x][y] = 1
          cnt += 1
          q.append([x, y])
  return cnt


#check: 바둑판 자동생성 - 방문 확인용, 
#findcnt = 오목이면 5, 삼목이면 3
check = [[0]* 15 for _ in range(15)]
findcnt = 5
#바둑판 크기 (가로, 세로)
n, m = 15, 15
# 여러 경우를 테스트 해보기위해 직접 작성함
exArr = [
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
  [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3],
  [0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0],
  [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0],
  [0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 3, 3, 0, 0, 0],
  [0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 3, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0]
]


#클릭된 위치는 임의로 넣어주고 테스트


#세로줄 검사
res = bfs(2,0)
print(res)
#가로줄 검사
res = bfs(1, 7)
print(res)
#왼쪽 대각선 검사
res = bfs(11, 6)
print(res)
#오른쪽 대각선검사
res = bfs(12,12)
print(res)


