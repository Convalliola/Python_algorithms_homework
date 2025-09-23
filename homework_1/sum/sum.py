"На вход подается массив целых положительных чисел, разделенных пробелом."
"Нужно найти максимальную сумму элементов массива, которая делится на 2."
def max_sum(str_:str):
  stripped_str = str_.strip()
  num_list = stripped_str.split(' ')
  nums = [int(num) for num in num_list] 


  # Если сумма всех чисел делится на 2, то это и есть искомая сумма
  total_sum = sum(nums)
  if total_sum % 2 == 0:
      return total_sum

  # Если сумма нечетная, то вычитаем из неё наименьший нечетный элемент из списка
  min_odd = min((x for x in nums if x % 2 == 1))

  result_sum = total_sum - min_odd
  if result_sum == 0:
    print('Четной суммы с набором таких чисел нет')
  else:
    return result_sum

