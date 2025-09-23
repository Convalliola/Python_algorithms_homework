from homework_1.palindrome.palindrome import is_palindrom


def test_is_palindrom_true_cases():
  assert is_palindrom(121) is True
  assert is_palindrom(0) is True
  assert is_palindrom(7) is True
  assert is_palindrom(1221) is True


def test_is_palindrom_false_cases():
  assert is_palindrom(123) is False
  assert is_palindrom(10) is False
  assert is_palindrom(-121) is False