import string

import numpy as np


def compare(criteria1, criteria2):
    if criteria1 == criteria2:
        return 0.5
    return criteria1 > criteria2


class MethodWeighingCombiningCriteria:
    def __init__(self, matrix, criteria):
        self.__matrix = matrix.copy()
        self.__vector_criteria = criteria.copy()
        self.__criteria = self.__pair_comparison()

        self.__normalize_matrix()
        self.answer = self.__solve()

    # метод парного сравнения
    def __pair_comparison(self):
        grades = np.array([[compare(criteria_1, criteria_2) for criteria_2 in self.__vector_criteria] for criteria_1 in
                           self.__vector_criteria])
        print(f'Экспертные оценки:\n {grades}')
        criteria_weights = np.array([sum(grades[i]) - 0.5 for i in range(4)])
        criteria_weights = np.divide(criteria_weights, sum(criteria_weights))
        print(f'Нормированный вектор весов критериев: {criteria_weights}')
        return criteria_weights

    # метод нормализации матрицы
    def __normalize_matrix(self):
        for col in range(len(self.__matrix)):
            self.__matrix[:, col] = np.divide(self.__matrix[:, col], np.sum(self.__matrix[:, col]))
        print(f'Нормированная матрица A:\n {self.__matrix}')

    # метод решения
    def __solve(self):
        self.__criteria = np.transpose(np.matrix(self.__vector_criteria))
        self.__matrix = np.matrix(self.__matrix)
        solutions = self.__matrix * self.__criteria
        max_result = 0
        answer = None
        for i in range(len(self.__matrix)):
            if solutions[i] > max_result:
                max_result = solutions[i]
                answer = i
        if answer is not None:
            answer = string.ascii_uppercase[answer]
        return answer
