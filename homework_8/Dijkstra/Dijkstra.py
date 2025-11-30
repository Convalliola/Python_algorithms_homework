"""
Реализовать алгоритм Дейкстры для взвешенного графа.
"""

import heapq


def dijkstra(graph: dict[int, list[tuple[int, int]]], start: int) -> dict[int, int]:
    """
    Алгоритм Дейкстры для поиска кратчайших путей от начальной вершины.

    На вход:
        graph: Взвешенный граф в виде словаря смежности
        start: Начальная вершина
    Возвращает словарь кратчайших расстояний {вершина: расстояние}
    или float('inf') если вершина недостижима

    Алгоритм корректен только при неотрицательных весах
    Предплогается, что все вершины есть ключами словаря
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # приоритетная очередь (расстояние, вершина)
    heap = [(0, start)]

    while heap:
        current_dist, current = heapq.heappop(heap)

        # пропускаем если уже нашли более короткий путь
        if current_dist > distances[current]:
            continue

        for neighbor, weight in graph.get(current, []):
            distance = current_dist + weight

            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def dijkstra_with_path(
    graph: dict[int, list[tuple[int, int]]], start: int, end: int
) -> tuple[int, list[int]]:
    """
    Алгоритм Дейкстры с восстановлением пути.

    На вход:
        graph: Взвешенный граф 
        start: Начальная вершина
        end: Конечная вершина

    Возвращает кратчайшее расстояние и список вершин пути
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {start: None}

    heap = [(0, start)]

    while heap:
        current_dist, current = heapq.heappop(heap)

        if current == end:
            break

        if current_dist > distances[current]:
            continue

        for neighbor, weight in graph.get(current, []):
            distance = current_dist + weight

            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                predecessors[neighbor] = current
                heapq.heappush(heap, (distance, neighbor))

    # восстановление пути
    if distances.get(end, float('inf')) == float('inf'):
        return float('inf'), []

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors.get(current)
    path.reverse()

    return distances[end], path
