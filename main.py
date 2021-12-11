import numpy as np
from methods.replacing_criteria import MethodReplacingCriteria
from methods.set_pareto import SetPareto
from methods.combining_criteria import MethodWeighingCombiningCriteria
from methods.hierarchy_analysis import MethodHierarchyAnalysis

'''
ЗАДАНИЕ:

Альтернативы:
A. Береза
B. Сосна
C. Дуб
D. Лиственница

Критерии:
1. Цена за кубометр
2. Легкость обработки
3. Долговечность
4. Водостойкость
'''

# точка входа в программу
if __name__ == '__main__':
    input_file = open('input.txt', 'r')
    data = [line.replace('\n', '') for line in input_file]
    min_criteria = data[data.index('M:') + 1:][0]
    min_criteria = [None if i == '-' else float(i) for i in min_criteria.split()]
    criteria = data[data.index('C:') + 1:data.index('M:')][0]
    criteria = [int(i) for i in criteria.split()]
    A = data[data.index('A:') + 1:data.index('C:')]
    A = np.array([[float(j) for j in i.split()] for i in A])
    input_file.close()

    print(f'Входные данные:\n'
          f'Матрица А:\n'
          f'{A}\n'
          f'Вектор весов критериев:\n'
          f'{criteria}\n'
          f'Допустимые значения:\n'
          f'{min_criteria}')

    print('\n', '-' * 50, '\nРешение методом замены критериев:')
    replacing_criteria = MethodReplacingCriteria(
        matrix=A,
        criteria=min_criteria,
        index=0
    )
    if replacing_criteria.answer is None:
        print('Подходящее решение отсутствует')
    else:
        print('Подходящим решением является: ', replacing_criteria.answer)

    print('\n', '-' * 50, '\nРешение формированием и сужением множества Парето:')
    set_pareto = SetPareto(
        matrix=A,
        criteria1=0,
        criteria2=2
    )
    set_pareto.show()
    print(f'Минимальное расстояние до точки {set_pareto.answer} - решение подходит')

    print('\n', '-' * 50, '\nРешение взвешиванием и объединением критериев:')
    combining_criteria = MethodWeighingCombiningCriteria(
        matrix=A,
        criteria=np.divide(criteria, sum(criteria))
    )
    print(f'Наилучшей является альтернатива {combining_criteria.answer}')

    print('\n', '-' * 50, '\nРешение методом анализа иерархий:')
    hierarchy_analysis = MethodHierarchyAnalysis(
        matrix=A,
        vector_priorities=criteria
    )
    print(f'Наилучшей является альтернатива {hierarchy_analysis.answer}')
