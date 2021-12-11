import string

import numpy as np


class MethodReplacingCriteria:
    def __init__(self, matrix, criteria, index):
        # входная матрица А
        self.__matrix = matrix.copy()
        # входные критерии
        self.__criteria = criteria.copy()
        # индекс
        self.__index = index

        self.__normalize_matrix()
        self.answer = self.__solve()

    # метод нормализации матрицы А
    def __normalize_matrix(self):
        min_ = np.min(self.__matrix, axis=0)
        max_ = np.max(self.__matrix, axis=0)
        for i in range(len(self.__matrix)):
            if i != self.__index:
                for j in range(len(self.__matrix)):
                    self.__matrix[j][i] = (self.__matrix[j][i] - min_[i]) / (max_[i] - min_[i])
        print(f'Нормированная матрица A:\n {self.__matrix}')

    # метод сравнения значений с ограничениями
    def __check_lower(self, row):
        for col in range(len(self.__matrix)):
            if col != self.__index:
                if row[col] < self.__criteria[col]:
                    return False
        return True

    # метод решения
    def __solve(self):
        answer = None
        for row in range(len(self.__matrix)):
            if self.__check_lower(self.__matrix[row]):
                if answer is None or self.__matrix[answer][self.__index] < self.__matrix[row][self.__index]:
                    answer = row
        if answer is not None:
            answer = string.ascii_uppercase[answer]
        return answer
