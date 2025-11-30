import pytest
from graph import find_connected_components, find_connected_components_dfs_iter


class TestFindConnectedComponents:
    def test_empty_graph(self):
        """пустой граф (нет компонент)"""
        graph = {}
        result1 = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert result1 == []
        assert result2 == []

    def test_single_vertex_no_edges(self):
        """1 вершина без рёбер"""
        graph = {1: []}
        result1 = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result1) == 1
        assert result1[0] == [1]
        assert len(result2) == 1
        assert result2[0] == [1]

    def test_single_vertex_with_self_loop(self):
        """одна вершина с петлёй """
        graph = {1: [1]}
        result1 = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result2) == 1
        assert result2[0] == [1]
        assert len(result1) == 1
        assert result1[0] == [1]

    def test_two_connected_vertices(self):
        """Две связанные вершины"""
        graph = {1: [2], 2: [1]}
        result = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result) == 1
        assert set(result[0]) == {1, 2}

        assert len(result2) == 1
        assert set(result2[0]) == {1, 2}

    def test_two_isolated_vertices(self):
        """две изолированные вершины"""
        graph = {1: [], 2: []}
        result = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result) == 2
        assert len(result2) == 2

    def test_fully_connected_graph(self):
        """Полносвязный граф, одна компонента"""
        graph = {
            1: [2, 3, 4],
            2: [1, 3, 4],
            3: [1, 2, 4],
            4: [1, 2, 3]
        }
        result = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result) == 1
        assert set(result[0]) == {1, 2, 3, 4}
        assert len(result2) == 1
        assert set(result2[0]) == {1, 2, 3, 4}

    def test_all_isolated_vertices(self):
        """Все вершины изолированы """
        graph = {1: [], 2: [], 3: [], 4: [], 5: []}
        result = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result) == 5
        assert len(result2) == 5

    def test_multiple_components(self):
        """Несколько компонент связности """
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2],
            4: [5],
            5: [4],
            6: []
        }
        result = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result) == 3
        components_as_sets = [set(c) for c in result]
        assert {1, 2, 3} in components_as_sets
        assert {4, 5} in components_as_sets
        assert {6} in components_as_sets

        assert len(result2) == 3
        components_as_sets2 = [set(c) for c in result2]
        assert {1, 2, 3} in components_as_sets2
        assert {4, 5} in components_as_sets2
        assert {6} in components_as_sets2

    def test_linear_graph(self):
        """Линейный граф """
        graph = {
            1: [2],
            2: [1, 3],
            3: [2, 4],
            4: [3, 5],
            5: [4]
        }
        result = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result) == 1
        assert set(result[0]) == {1, 2, 3, 4, 5}

        assert len(result2) == 1
        assert set(result2[0]) == {1, 2, 3, 4, 5}

    def test_cycle_graph(self):
        """граф-цикл"""
        graph = {
            1: [2, 4],
            2: [1, 3],
            3: [2, 4],
            4: [3, 1]
        }
        result = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result) == 1
        assert set(result[0]) == {1, 2, 3, 4}

        assert len(result2) == 1
        assert set(result2[0]) == {1, 2, 3, 4}

    def test_star_graph(self):
        """Граф-звезда с одной центральной вершиной)"""
        graph = {
            1: [2, 3, 4, 5],
            2: [1],
            3: [1],
            4: [1],
            5: [1]
        }
        result = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result) == 1
        assert set(result[0]) == {1, 2, 3, 4, 5}
        assert len(result2) == 1
        assert set(result2[0]) == {1, 2, 3, 4, 5}

    def test_two_triangles(self):
        """Два отдельных треугольника"""
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2],
            4: [5, 6],
            5: [4, 6],
            6: [4, 5]
        }
        result = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result) == 2
        components_as_sets = [set(c) for c in result]
        assert {1, 2, 3} in components_as_sets
        assert {4, 5, 6} in components_as_sets

        assert len(result2) == 2
        components_as_sets2 = [set(c) for c in result2]
        assert {1, 2, 3} in components_as_sets2
        assert {4, 5, 6} in components_as_sets2

    def test_string_vertices(self):
        """Граф с вершинами-строками """
        graph = {
            "a": ["b"],
            "b": ["a", "c"],
            "c": ["b"],
            "x": ["y"],
            "y": ["x"]
        }
        result = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result) == 2
        assert len(result2) == 2

        components_as_sets = [set(c) for c in result]
        assert {"a", "b", "c"} in components_as_sets
        assert {"x", "y"} in components_as_sets

        components_as_sets2 = [set(c) for c in result2]
        assert {"a", "b", "c"} in components_as_sets2
        assert {"x", "y"} in components_as_sets2

    def test_large_single_component(self):
        """Большой граф с одной компонентой"""
        n = 100
        graph = {i: [i - 1, i + 1] for i in range(1, n)}
        graph[0] = [1]
        graph[n - 1] = [n - 2]
        result = find_connected_components(graph)
        result2 = find_connected_components_dfs_iter(graph)
        assert len(result) == 1
        assert len(result[0]) == n
        assert len(result2) == 1
        assert len(result2[0]) == n

if __name__ == "__main__":
    pytest.main([__file__, "-v"])