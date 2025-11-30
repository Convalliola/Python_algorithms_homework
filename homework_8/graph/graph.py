"""
Дан неориентированный граф.

Необходимо, найти все компоненты связности графа и вывести их.

Подразумевается, что граф подается на вход в виде списка смежности (словарь со списками ребер).

"""

# версия с рекурсией
def find_connected_components(graph: dict[int, list[int]]) -> list[list[int]]:
    """
    Находит все компоненты связности в неориентированном графе
    """
    visited = set()
    components = []

    def dfs(node: int, component: list[int]):
        visited.add(node)
        component.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components

# итератинвая версия
def find_connected_components_dfs_iter(graph: dict[int, list[int]]) -> list[list[int]]:
    """
    итеративный DFS со стеком
    """
    visited = set()
    components = []

    for start in graph:  # предполагаем, что все вершины есть ключами словаря
        if start in visited:
            continue

        stack = [start]
        visited.add(start)
        component = []

        while stack:
            node = stack.pop()
            component.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        components.append(component)

    return components