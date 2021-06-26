maze=[
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,0,0,1,1,1,1],
    [1,0,1,1,0,1,1,1,1,1],
    [1,0,0,1,0,1,1,1,1,1],
    [1,1,0,0,0,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,1,1,1,1],
    [1,1,1,1,0,0,0,1,1,1],
    [1,1,1,1,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]
#設定起、終點
start=(1,1)
end=(8,8)
#放走的每一步(r,c)
lst=[start]
while lst:#有路走
    now=lst[-1]#目前走的列表最後一點
    if now == end:
        print(lst)#結果
        break
    row ,col = now 
    maze[row][col]=2 #將走過的地方標記
    #上
    if maze[row-1][col]==0:
        lst.append((row-1,col))
    #右
    elif maze[row][col+1]==0:
        lst.append((row,col+1))
    #下
    elif maze[row+1][col]==0:
        lst.append((row+1,col))
    #左
    elif maze[row][col-1]==0:
        lst.append((row,col-1))
    else:
        lst.pop()#走到死路就回到上一點

else:
    print("無路走")