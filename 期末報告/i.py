# -*- coding: utf-8 -*-




from random import randint

def mark(maze,y = pos[1]

 

  maze[pos[0]][pos[1]] = 2 # 將走過的位置標記為 2

def move(maze,y = pos[1]

  :return: bool 型別

  return maze[pos[0]][pos[1]] == 0

move_path = [] # 記錄能成功到達出口的移動路徑座標

path_direction = [] # 記錄能成功到達出口的移動路徑方向

def find_path(maze,end):

        # 這裡之所以仍然新增起始點座標是因為當查詢到下一個位置就是終點或者可到達終點時記錄此時位置

        move_path.append(start)

        path_direction.append(direction[i]) # 記錄路徑方向

        return True

  return False # 遍歷遞迴了 4 種可能方向後仍不能到達終點則說明無法走出迷宮

 

 

def gen_maze(m,n):

  

  生成隨機迷宮陣列

  :param m: int 型別

  :param n: int 型別

  :return: maze

  

  m += 2

  n += 2 # m 和 n 均 +2 是為了構造最外層的 1

  maze = [[1 for i in range(n)] for j in range(m)] # 初始化大小為 m * n，值全為 1 的二維矩陣

  for x in range(1,n-1):

      

      這裡 x,y 取值範圍為 x ∈ [1,m-1)，y ∈ [1,n-1) 是因為我們令此迷宮的最外層（四周）均為 1，如：

      考察 3 * 3 矩陣，一種可能的陣列為：

      [

       _ |←--- n:y ---→|

       ↑ [1,1,1],| [1,m:x [1,↓ [1,1]

      ]

      

      if (x == 1 and y == 1) or (x == m - 2 and y == n - 2):

        maze[x][y] = 0 # 起始點和終點必為 0

      else:

        maze[x][y] = randint(0,1) # 在最外層均為 1 的情況下內部隨機取 0，1

  return maze

 

 

def print_maze(maze,end=end1)

    print(end=end2)

 

 

def path_maze(maze,j = directions_position

      i = 2 * i

      j = 2 * j

      if direction == "↑":

        maze[i - 1][j] = "↑"

      if direction == "↓":

        maze[i + 1][j] = "↓"

      if direction == "←":

        maze[i][j] = " ← "

      if direction == "→":

        maze[i][j + 1] = " → "

  return maze

def main():

  # maze = gen_maze(m=10,n=12)

  maze = \

    [

      [1,[1,1]

    ] # 輸入樣式矩陣，這裡最外層用 1 環包圍住，目的是方便後續的處理，可以用 gen_maze() 函式自生成

  print_maze(maze)

  if find_path(maze,start=(1,1),end=(10,12)):

    mp = move_path[::-1]
    pd = path_direction[::-1]

    # 這裡 pos[0] 和 pos[1] 都要 -1 是因為原來的遞迴計算中存在最外層的 1 環

    print('座標移動順序為:',[(pos[0]-1,pos[1]-1) for pos in mp])

    path_direction_map = {

      '↑': [],'↓': [],'←': [],'→': []

    } # 路徑方向的對映表

    for i in range(len(pd)):

      path_direction_map[pd[i]].append(mp[i])

    maze = path_maze(maze,path_direction_map)

    print_maze(maze,text='迷宮移動路徑為：',end1='',end2='\n',xs=1,xe=1,ys=1,ye=1)

  else:

    print('此迷宮無解')


if __name__ == '__main__':

  main()

