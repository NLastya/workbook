#FILE in progress
#1. ...
#Solution
#1. Think that this is useful for big array of data. Difficult: O(N).

def sub_arr(a: [], b: []):
    b_set = set(b)
    res = []
    for i in range(len(a)): #len of array is O(1).
          if a[i] not in b: #this action is O(1).
              res += [a[i]]
    return res
  
#2: Pythonic style, Time complimitiv: O(N).
def sub_arr(a: [], b: []):
    b_set = set(b)
    res = []
    res = [s for s in a if s not in set(b)]
    return res



#3: Задача вывести номер телефона в нужном формате, числа заданы в массиве. Предполагается, что данные уже проверены, то есть чисел в массиве достоверно 10.
def create_phone_number(n):
    #Проверка на ненулове значение(не сломанное значение)
    if not n:
        return ""
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)



