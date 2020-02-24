from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from game import Gomoku


class GomokuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ai()  # 初始化游戏界面
        self.g = Gomoku()  # 初始化游戏内容

    def init_ai(self):
        '''初始化游戏界面'''
        # 1.确定游戏界面的标题、大小和背景颜色
        self.setObjectName('MainWindow')
        self.setWindowTile('五子棋')
        self.setFixedSize(650, 650)
        self.setStyleSheet("#MainWindow{background-color:green}")

        # 2.显示初始化的游戏界面
        self.show()

    def pointEvent(self, e):
        '''绘制游戏内容'''

        def draw_map(self):
            '''绘制棋盘'''
            qp.setPen(QPen(QColor(0, 0, 0), 2, Qt.SolidLine))  # 棋盘的颜色为黑色

            # 绘制横线
            for x in range(15):
                qp.drawLine(40*(x+1), 40, 40*(x+1), 600)
            # 绘制竖线
            for y in range(15):
                qp.drawLine(40, 40*(y+1), 600, 40*(y+1))

        def draw_pieces():
            '''绘制棋子'''
            # 绘制黑棋子
            qp.setPen(QPen(QColor(0, 0, 0), 1, Qt.SolidLine))
            qp.setBrush(QColor(0, 0, 0))
            for x in range(15):
                for y in range(15):
                    if self.g.g_map[x][y] == 1:
                        qp.drawEllipse(QPoint(40*(x+1), 40*(y+1), 15, 15))
            # 绘制白棋子
            qp.setPen(QPen(QColor(255, 255, 255), 1, Qt.SolidLine))
            qp.setBrush(QColor(255, 255, 255))
            for x in range(15):
                for y in range(15):
                    if self.g.g_map[x][y] == 2:
                        qp.drawEllipse(QPoint(40*(x+1), 40*(y+1), 15, 15))
        qp = QPainter()
        qp.begin(self)
        draw_map()  # 绘制棋盘
        draw_pieces()  # 绘制棋子
        qp.end()

    def mousePressEvent(self, e):
        '''根据鼠标的动作，确定落子位置'''
        pass
