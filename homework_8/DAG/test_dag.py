import pytest
from DAG import find_cycle, topological_sort, analyze_graph


class TestFindCycle:
    def test_no_cycle_single_vertex(self):
        # одна вершина без цикла
        graph = {1: []}
        assert find_cycle(graph) is None

    def test_self_loop(self):
        # Петля (вершина ссылается на себя)
        graph = {1: [1]}
        cycle = find_cycle(graph)
        assert cycle is not None
        assert 1 in cycle

    def test_simple_cycle(self):
        # Простой цикл из трёх вершин
        graph = {1: [2], 2: [3], 3: [1]}
        cycle = find_cycle(graph)
        assert cycle is not None
        assert len(cycle) == 4  # 1 -> 2 -> 3 -> 1
        # проверяем, что цикл замкнут
        assert cycle[0] == cycle[-1]

    def test_cycle_in_larger_graph(self):
        # Цикл в большом графе
        graph = {
            1: [2],
            2: [3],
            3: [4],
            4: [2],  # цикл: 2 -> 3 -> 4 -> 2
            5: [1]
        }
        cycle = find_cycle(graph)
        assert cycle is not None
        assert cycle[0] == cycle[-1]

    def test_no_cycle_linear(self):
        # Линейный граф без цикла
        graph = {1: [2], 2: [3], 3: [4], 4: []}
        assert find_cycle(graph) is None

    def test_no_cycle_tree(self):
        #  DAG без цикла
        graph = {
            1: [2, 3],
            2: [4, 5],
            3: [6],
            4: [],
            5: [],
            6: []
        }
        assert find_cycle(graph) is None

    def test_no_cycle_diamond(self):
        # Ромбовидный DAG без цикла
        graph = {
            1: [2, 3],
            2: [4],
            3: [4],
            4: []
        }
        assert find_cycle(graph) is None

    def test_two_separate_cycles(self):
        # Две отдельные компоненты с циклами
        graph = {
            1: [2],
            2: [1],  # цикл 1
            3: [4],
            4: [3]   # цикл 2
        }
        cycle = find_cycle(graph)
        assert cycle is not None

    def test_empty_graph(self):
        # Пустой граф
        graph = {}
        assert find_cycle(graph) is None


class TestTopologicalSort:
    def test_single_vertex(self):
        # Одна вершина
        graph = {1: []}
        result = topological_sort(graph)
        assert result == [1]

    def test_linear_graph(self):
        # Линейный граф
        graph = {1: [2], 2: [3], 3: []}
        result = topological_sort(graph)
        assert result == [1, 2, 3]

    def test_diamond_dag(self):
        # Ромбовидный DAG
        graph = {
            1: [2, 3],
            2: [4],
            3: [4],
            4: []
        }
        result = topological_sort(graph)
        assert result is not None
        # Проверяем порядок: 1 до 2,3; 2,3 до 4
        assert result.index(1) < result.index(2)
        assert result.index(1) < result.index(3)
        assert result.index(2) < result.index(4)
        assert result.index(3) < result.index(4)

    def test_complex_dag(self):
        # Сложный DAG
        graph = {
            1: [2, 3],
            2: [4],
            3: [4],
            4: [5],
            5: []
        }
        result = topological_sort(graph)
        assert result is not None
        # Проверяем, что все зависимости соблюдены
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                assert result.index(node) < result.index(neighbor)

    def test_returns_none_on_cycle(self):
        # Возвращает None при наличии цикла
        graph = {1: [2], 2: [3], 3: [1]}
        assert topological_sort(graph) is None

    def test_multiple_valid_orders(self):
        # Граф с несколькими валидными порядками
        graph = {
            1: [3],
            2: [3],
            3: []
        }
        result = topological_sort(graph)
        assert result is not None
        assert result.index(1) < result.index(3)
        assert result.index(2) < result.index(3)

    def test_disconnected_dag(self):
        # Несвязный DAG
        graph = {
            1: [2],
            2: [],
            3: [4],
            4: []
        }
        result = topological_sort(graph)
        assert result is not None
        assert len(result) == 4
        assert result.index(1) < result.index(2)
        assert result.index(3) < result.index(4)

    def test_empty_graph(self):
        # Пустой граф
        graph = {}
        result = topological_sort(graph)
        assert result == []


class TestAnalyzeGraph:
    def test_graph_with_cycle(self):
        # Граф с циклом
        graph = {1: [2], 2: [3], 3: [1]}
        has_cycle, result = analyze_graph(graph)
        assert has_cycle is True
        assert result is not None
        assert result[0] == result[-1]  # цикл замкнут

    def test_dag_without_cycle(self):
        # DAG без цикла
        graph = {
            1: [2, 3],
            2: [4],
            3: [4],
            4: []
        }
        has_cycle, result = analyze_graph(graph)
        assert has_cycle is False
        assert result is not None
        # Проверяем топологический порядок
        assert result.index(1) < result.index(2)
        assert result.index(1) < result.index(3)
        assert result.index(2) < result.index(4)

    def test_single_vertex_no_cycle(self):
        """Одна вершина без цикла"""
        graph = {1: []}
        has_cycle, result = analyze_graph(graph)
        assert has_cycle is False
        assert result == [1]

    def test_self_loop_detected(self):
        """Петля обнаруживается"""
        graph = {1: [1]}
        has_cycle, result = analyze_graph(graph)
        assert has_cycle is True

    def test_complex_graph_with_cycle(self):
        """Сложный граф с циклом"""
        graph = {
            1: [2],
            2: [3],
            3: [4],
            4: [2],  # цикл
            5: [1]
        }
        has_cycle, result = analyze_graph(graph)
        assert has_cycle is True
        # Проверяем, что найден именно цикл 2->3->4->2
        assert 2 in result
        assert 3 in result
        assert 4 in result


class TestCycleValidity:
    # проверка корректности найденных циклов

    def test_cycle_is_valid_path(self):
        """Цикл является валидным путём в графе"""
        graph = {1: [2], 2: [3], 3: [4], 4: [2]}
        cycle = find_cycle(graph)
        assert cycle is not None
        # Проверяем, что каждое ребро цикла существует в графе
        for i in range(len(cycle) - 1):
            assert cycle[i + 1] in graph.get(cycle[i], [])

    def test_cycle_starts_and_ends_same(self):
        """Цикл начинается и заканчивается одной вершиной"""
        graph = {1: [2], 2: [3], 3: [1]}
        cycle = find_cycle(graph)
        assert cycle is not None
        assert cycle[0] == cycle[-1]


class TestTopologicalSortValidity:
    """Проверка корректности топологической сортировки"""

    def test_all_vertices_included(self):
        """Все вершины включены в результат"""
        graph = {1: [2, 3], 2: [4], 3: [4], 4: [5], 5: []}
        result = topological_sort(graph)
        assert set(result) == set(graph.keys())

    def test_dependencies_respected(self):
        """Все зависимости соблюдены"""
        graph = {
            'a': ['b', 'c'],
            'b': ['d'],
            'c': ['d'],
            'd': ['e'],
            'e': []
        }
        result = topological_sort(graph)
        assert result is not None
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                assert result.index(node) < result.index(neighbor)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
