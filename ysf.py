def move(players,step):
    # 移动step前的元素到列表末尾
        num =step - 1
        while num > 0:
            tmp =players.pop(0)
            players.append(tmp)
            num = num - 1
    
       return players





def play(x,y,z):
    players = x
    alive = z
    step = y
    
    list1 = [i for i in range(1,players+1)]
   # 进入游戏的循环，每次数到step淘汰，step之前的元素移动的列表末尾
   # 游戏结束的条件；列表人数小于alive
    while len(list1) > alive:
    # 移动step前的元素到列表末尾
        list1 = move(list1,step)
        
        list1.pop(0)    # 此时的step的元素在列表第一个位置，使用pop(0)从列表中删除
    return list1
players_num = int(input("请输入参加的人数"))
step_num = int(input("请输入淘汰的数字"))
slive_num = int(input("请输入幸存的人数"))

alive_list = play(players_num,step_num,slive_num)
print(alive_list)