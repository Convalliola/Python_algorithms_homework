from homework_1.sum.sum import max_sum

def test_max_sum_even_total():
  assert max_sum("1 2 3 4") == 10
  assert max_sum("1 2 4") == 6
  assert max_sum("2 4 6") == 12
  assert max_sum("13 300 54 21") == 388
  assert max_sum("8") == 8


def test_max_sum_single_odd_prints_message(capsys):
  result = max_sum("7")
  output = capsys.readouterr().out.strip()
  assert result is None
  assert "Четной суммы с набором таких чисел нет" in output