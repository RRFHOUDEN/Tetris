import tkinter
import itertools
import numpy as np
for i in range(1):
    print(1)
class Boad:
    #盤の設定，処理

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.num_boad     = [[0 for _ in range(self.width)] for _ in range(self.height)]

    #blockは駒，配列で入力
    #駒をy行x列に配置
    def input_block(self, block, y, x):
        for i in range(len(block)):
            for j in range(len(block[i])):
                self.num_boad[y + i][x + j] += 1

    #lineより上の列を下におろす
    def down_boad(self, line):
        for i in range(line - 1, -1, -1):
            for j in range(self.width):
                if self.num_boad[i][j] == 1:
                    self.num_boad[i + 1][j] = 1

    #行がそろってるかを判定したうえで更新
    def update_boad(self):
        for i in range(self.height):
            if sum(self.num_boad[i]) == self.width:
                self.down_boad(i)

class block:
    #blockに関する処理
    square = [[1, 1], [1, 1]]
