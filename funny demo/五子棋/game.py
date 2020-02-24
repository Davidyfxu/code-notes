class Gomoku:
    def __init__(self):
        self.g_map = [[0 for y in range(15)] for x in range(15)]  # 游戏棋盘
        self.cur_step = 0  # 步数

    def move_lstep(self):
        '''玩家落子'''
        while True:
            try:
                pos_x = int(input("x: "))
                pos_y = int(input("y: "))
                if 0 <= pos_x <= 14 and 0 <= pos_y <= 14:
                    if self.g_map[pos_x][pos_y] == 0:
                        self.g_map[pos_x][pos_y] = 1
                        self.cur_step += 1
                        return
            except ValueError:  # 玩家输入错误后的情况
                continue

    def game_result(self):
        '''判断游戏的结局：0为正在进行中，1为玩家获胜，2为电脑获胜，3为平局'''
        # 1.判断是否横向连续五子
        for x in range(11):
            for y in range(15):
                if self.g_map[x][y] == 1 and self.g_map[x+1][y] == 1 and self.g_map[x+2][y] == 1 and self.g_map[x+3][y] == 1 and self.g_map[x+4][y] == 1:
                    return 1
                if self.g_map[x][y] == 2 and self.g_map[x+1][y] == 2 and self.g_map[x+2][y] == 2 and self.g_map[x+3][y] == 2 and self.g_map[x+4][y] == 2:
                    return 2
        # 2.判断是否纵向连续五子
        for x in range(15):
            for y in range(11):
                if self.g_map[x][y] == 1 and self.g_map[x][y+1] == 1 and self.g_map[x][y+2] == 1 and self.g_map[x][y+3] == 1 and self.g_map[x][y+4] == 1:
                    return 1
                if self.g_map[x][y] == 2 and self.g_map[x][y+1] == 2 and self.g_map[x][y+2] == 2 and self.g_map[x][y+3] == 2 and self.g_map[x][y+4] == 2:
                    return 2
        # 3.判断是否左上-右下连续五子
        for x in range(11):
            for y in range(11):
                if self.g_map[x][y] == 1 and self.g_map[x+1][y+1] == 1 and self.g_map[x+2][y+2] == 1 and self.g_map[x+3][y+3] == 1 and self.g_map[x+4][y+4] == 1:
                    return 1
                if self.g_map[x][y] == 2 and self.g_map[x+1][y+2] == 2 and self.g_map[x+2][y+2] == 2 and self.g_map[x+3][y+3] == 2 and self.g_map[x+4][y+4] == 2:
                    return 2

        # 4.判断是否右上-左下连续五子
        for x in range(11):
            for y in range(11):
                if self.g_map[x+4][y] == 1 and self.g_map[x+3][y+1] == 1 and self.g_map[x+2][y+2] == 1 and self.g_map[x+1][y+3] == 1 and self.g_map[x][y+4] == 1:
                    return 1
                if self.g_map[x+4][y] == 2 and self.g_map[x+3][y+1] == 2 and self.g_map[x+2][y+2] == 2 and self.g_map[x+1][y+3] == 2 and self.g_map[x][y+4] == 2:
                    return 2
        # 5.判断是否为平局
        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:  # 棋盘中还有剩余的格子，不能判断为平局
                    return 0
        return 3

    def ai_move_lstep(self):
        '''电脑落子'''
        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:
                    self.g_map[x][y] = 2
                    self.cur_step += 1
                    return

    def show(self, res):
        '''显示游戏内容'''
        for y in range(15):
            for x in range(15):
                if self.g_map[x][y] == 0:
                    print(" ", end='')
                elif self.g_map[x][y] == 1:
                    print("()", end='')
                elif self.g_map[x][y] == 2:
                    print("x", end='')

                if x != 14:
                    print('-', end='')
            print('\n', end='')
            for x in range(15):
                print("| ", end='')
            print('\n', end='')
        if res == 1:
            print('玩家获胜！')
        elif res == 2:
            print('电脑获胜！')
        elif res == 3:
            print('平局！')

    def play(self):
        while True:
            self.move_lstep()  # 玩家下一步
            res = self.game_result()  # 判断游戏结果
            if res != 0:  # 若游戏结果为“已结束”，则显示游戏内容，退出主循环
                self.show(res)
                return

            self.ai_move_lstep()  # 电脑下一步
            res = self.game_result()  # 判断游戏结果
            if res != 0:  # 若游戏结果为“已结束”，则显示游戏内容，退出主循环
                self.show(res)
                return

            self.show(0)
