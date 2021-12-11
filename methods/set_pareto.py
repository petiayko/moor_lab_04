import string

import matplotlib.pyplot as plt
import numpy as np


class SetPareto:
    def __init__(self, matrix, criteria1, criteria2):
        self.__matrix = matrix
        self.__x = self.__matrix[:, criteria1][:]
        self.__y = self.__matrix[:, criteria2][:]

        self.__max_x = np.max(self.__x)
        self.__max_y = np.max(self.__y)
        self.answer = self.__solve()

    # метод отображения графика
    def show(self):
        plt.title('Графическое решение')
        plt.plot(self.__x, self.__y, 'o')
        plt.grid()
        plt.show()

    # метод получения манхеттенского расстояния
    def __get_distance(self, x, y):
        return np.max([np.abs(x - self.__max_x), np.abs(y - self.__max_y)])

    # метод решения
    def __solve(self):
        min_distance = self.__get_distance(0., 0.)
        answer = None
        for i in range(len(self.__matrix)):
            dis = self.__get_distance(self.__x[i], self.__y[i])
            if dis < min_distance:
                min_distance = dis
                answer = i
        if answer is not None:
            answer = string.ascii_uppercase[answer]
        return answer
