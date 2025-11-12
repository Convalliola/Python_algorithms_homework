"""
Реализовать декоратор, который показывает стек вызовов рекурсивных функций
На каждом шаге должен быть виден:
* вход в рекурсию (вызов функции),
* отступ, соответствующий глубине стека,
* возврат из рекурсии с результатом
"""

import functools


def tracer(func):
    """
    Декоратор для трассировки рекурсивных вызовов функции, показывает глубину стека вызовов и результаты возврата.
    """
    # атрибут функции для хранения глубины вызовов
    func.depth = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = ', '.join(repr(arg) for arg in args)
        kwargs_repr = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_repr, kwargs_repr]))

        indent = '  ' * func.depth

        print(f"{indent}→ {func.__name__}({all_args})")

        func.depth += 1

        try:
            result = func(*args, **kwargs)
            func.depth -= 1
            indent = '  ' * func.depth
            print(f"{indent}← {func.__name__}({all_args}) = {result!r}")

            return result
        except Exception as e:
            func.depth -= 1
            indent = '  ' * func.depth
            print(f"{indent}← {func.__name__}({all_args}) raised {type(e).__name__}: {e}")
            raise

    return wrapper


# Пример использования
if __name__ == "__main__":
    @tracer
    def factorial(n):
        """Вычисление факториала"""
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    @tracer
    def fibonacci(n):
        """Вычисление числа Фибоначчи"""
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    print("=== Factorial(5) ===")
    result = factorial(5)
    print(f"\nРезультат: {result}\n")

    print("=== Fibonacci(5) ===")
    result = fibonacci(5)
    print(f"\nРезультат: {result}")