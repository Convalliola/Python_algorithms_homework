import pytest
from homework_1.prime.prime import is_prime

@pytest.mark.parametrize(
  "n, expected",
  [
    (0, 0),
    (1, 0),
    (2, 1),
    (3, 2),
    (10, 4),
    (20, 8),
    (100, 25)
  ],
)
def test_is_prime_counts_various(n, expected):
  count = is_prime(n)
  assert count == expected