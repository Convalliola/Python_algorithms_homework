"""
Дан ориентированный граф.

1) Нужно определить, есть ли в графе цикл
2) Если цикл есть -- вывести его (достаточно одного цикла)
3) Если цикла нет -- применяем топологическую сортировку и выводим результат

Подразумевается, что граф подается на вход в виде списка смежности (словарь со списками ребер).
"""

# цвета вершин для DFS
WHITE = 0  # не посещена
GRAY = 1   # в обработке 
BLACK = 2  # обработана


def find_cycle(graph: dict[int, list[int]]) -> list[int] | None:
    """
    Находит цикл в ориентированном графе

    На вход - словарь смежности 
    Возвращает список вершин цикла или None, если цикла нет
    Сложность: O(V + E)
    """
    color = {node: WHITE for node in graph}
    parent = {node: None for node in graph}

    def dfs(node: int) -> list[int] | None:
        color[node] = GRAY

        for neighbor in graph.get(node, []):
            if neighbor not in color:
                color[neighbor] = WHITE
                parent[neighbor] = None

            if color[neighbor] == GRAY:
                # Нашли цикл — восстанавливаем его
                cycle = [neighbor]
                current = node
                while current != neighbor:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(neighbor)
                cycle.reverse()
                return cycle

            if color[neighbor] == WHITE:
                parent[neighbor] = node
                result = dfs(neighbor)
                if result:
                    return result

        color[node] = BLACK
        return None

    for node in graph:
        if color[node] == WHITE:
            result = dfs(node)
            if result:
                return result

    return None


def topological_sort(graph: dict[int, list[int]]) -> list[int] | None:
    """
    Топологическая сортировка ориентированного графа
    Возвращает список вершин в топологическом порядке или None, если есть цикл
    """
    color = {node: WHITE for node in graph}
    result = []

    def dfs(node: int) -> bool:
        color[node] = GRAY

        for neighbor in graph.get(node, []):
            if neighbor not in color:
                color[neighbor] = WHITE

            if color[neighbor] == GRAY:
                return False  # цикл
            if color[neighbor] == WHITE:
                if not dfs(neighbor):
                    return False

        color[node] = BLACK
        result.append(node)
        return True

    for node in graph:
        if color[node] == WHITE:
            if not dfs(node):
                return None

    result.reverse()
    return result


def analyze_graph(graph: dict[int, list[int]]) -> tuple[bool, list[int] | None]:
    """
    находит цикл или выполняет топологическую сортировку
    Вовзрщает (has_cycle, result):
        - Если есть цикл: True, список вершин цикла
        - Если нет цикла: False, топологический порядок
    """
    cycle = find_cycle(graph)
    if cycle:
        return True, cycle

    topo_order = topological_sort(graph)
    return False, topo_order
