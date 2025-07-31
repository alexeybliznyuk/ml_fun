def round_to_2(x):
    """
    Принимает число и возвращает результат его округления
    до 2 знаков после запятой.
    
    Аргументы:
        x: Число.
        
    Возвращаемое значение:
        Результат округления числа до 2 знаков после запятой.
    """
    
    return round(x, 2)


def mean_absolute_difference_solution(real, predicted):
    error_sigma = 0
    for pos in range(len(real)):
        r = real[pos]
        p = predicted[pos]
        
        error_sigma += abs(r - p)

    return round_to_2(error_sigma / len(real))
