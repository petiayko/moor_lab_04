import string

import numpy as np


def compare(rating1, rating2):
    delta = rating1 - rating2
    if delta == 3:
        return 7
    elif delta == 2:
        return 5
    elif delta == 1:
        return 3
    elif delta == 0:
        return 1
    elif delta == -1:
        return 1 / 3
    elif delta == -2:
        return 1 / 5
    else:
        return 1 / 7


class MethodHierarchyAnalysis:
    def __init__(self, matrix, vector_priorities):
        self.__matrix = matrix.copy()
        self.__vector_priorities = vector_priorities

        self.matrix_criteria0 = self.__pairwise_comparison(0)
        self.matrix_criteria1 = self.__pairwise_comparison(1)
        self.matrix_criteria2 = self.__pairwise_comparison(2)
        self.matrix_criteria3 = self.__pairwise_comparison(3)
        self.matrix_criteria = np.transpose(
            np.matrix([self.matrix_criteria0, self.matrix_criteria1, self.matrix_criteria2, self.matrix_criteria3]))
        self.matrix_priorities = np.transpose(np.matrix(self.__comparison_priorities()))
        self.answer = self.__solve()

    # метод парного сравнения
    def __pairwise_comparison(self, criteria_index):
        new_matrix = np.array([[compare(self.__matrix[row_1][criteria_index], self.__matrix[row_2][criteria_index]) for
                                row_2 in range(len(self.__matrix))] for row_1 in range(len(self.__matrix))])
        sum_line = np.array([np.sum(new_matrix[i]) for i in range(len(new_matrix))])
        sum_line = np.divide(sum_line, np.sum(sum_line))
        return sum_line

    # метод сравнения критериев
    def __comparison_priorities(self):
        new_matrix = np.array([[compare(self.__vector_priorities[row_1], self.__vector_priorities[row_2]) for row_2 in
                                range(len(self.__matrix))] for row_1 in range(len(self.__matrix))])
        sum_line = np.array([np.sum(new_matrix[i]) for i in range(len(new_matrix))])
        sum_line = np.divide(sum_line, np.sum(sum_line))
        return sum_line

    # метод решения
    def __solve(self):
        solutions = self.matrix_criteria * self.matrix_priorities
        max_result = 0
        answer = None
        for i in range(len(self.__matrix)):
            if solutions[i] > max_result:
                max_result = solutions[i]
                answer = i
        if answer is not None:
            answer = string.ascii_uppercase[answer]
        return answer
