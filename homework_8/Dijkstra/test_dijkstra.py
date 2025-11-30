import pytest
from Dijkstra import dijkstra, dijkstra_with_path


class TestDijkstra:
    def test_single_vertex(self):
        """граф с одной вершиной """
        graph = {1: []}
        result = dijkstra(graph, start=1)
        assert result[1] == 0

    def test_two_connected_vertices(self):
        """две связанные вершины """
        graph = {1: [(2, 5)], 2: [(1, 5)]}
        result = dijkstra(graph, start=1)
        assert result[1] == 0
        assert result[2] == 5

    def test_linear_graph(self):
        """линейный граф """
        graph = {
            1: [(2, 1)],
            2: [(1, 1), (3, 2)],
            3: [(2, 2), (4, 3)],
            4: [(3, 3)]
        }
        result = dijkstra(graph, start=1)
        assert result[1] == 0
        assert result[2] == 1
        assert result[3] == 3
        assert result[4] == 6

    def test_shortest_path_not_direct(self):
        """кратчайший путь не прямой"""
        # 1 -> 2 напрямую = 10, через 3 = 2 + 3 = 5
        graph = {
            1: [(2, 10), (3, 2)],
            2: [(1, 10), (3, 3)],
            3: [(1, 2), (2, 3)]
        }
        result = dijkstra(graph, start=1)
        assert result[2] == 5  # через вершину 3

    def test_unreachable_vertex(self):
        """недостижимая вершина """
        graph = {
            1: [(2, 1)],
            2: [(1, 1)],
            3: []  # изолированная вершина
        }
        result = dijkstra(graph, start=1)
        assert result[1] == 0
        assert result[2] == 1
        assert result[3] == float('inf')

    def test_directed_graph(self):
        """ориентированный граф (односторонние рёбра) """
        graph = {
            1: [(2, 1)],
            2: [(3, 1)],
            3: []
        }
        result = dijkstra(graph, start=1)
        assert result[1] == 0
        assert result[2] == 1
        assert result[3] == 2

    def test_multiple_paths_same_weight(self):
        """Несколько путей одинакового веса."""
        graph = {
            1: [(2, 1), (3, 1)],
            2: [(1, 1), (4, 1)],
            3: [(1, 1), (4, 1)],
            4: [(2, 1), (3, 1)]
        }
        result = dijkstra(graph, start=1)
        assert result[4] == 2  # любой путь через 2 или 3

    def test_zero_weight_edge(self):
        """ребро с нулевым весом"""
        graph = {
            1: [(2, 0)],
            2: [(1, 0), (3, 5)],
            3: [(2, 5)]
        }
        result = dijkstra(graph, start=1)
        assert result[2] == 0
        assert result[3] == 5

    def test_large_weights(self):
        """большие веса рёбер"""
        graph = {
            1: [(2, 1000000)],
            2: [(1, 1000000), (3, 1000000)],
            3: [(2, 1000000)]
        }
        result = dijkstra(graph, start=1)
        assert result[3] == 2000000

    def test_complex_graph(self):
        """сложный граф с несколькми путями """
        #     1 --2-- 2
        #     |       |
        #     4       1
        #     |       |
        #     3 --1-- 4
        graph = {
            1: [(2, 2), (3, 4)],
            2: [(1, 2), (4, 1)],
            3: [(1, 4), (4, 1)],
            4: [(2, 1), (3, 1)]
        }
        result = dijkstra(graph, start=1)
        assert result[1] == 0
        assert result[2] == 2
        assert result[3] == 4  # напрямую или через 2->4->3
        assert result[4] == 3  # через 2


class TestDijkstraWithPath:
    def test_direct_path(self):
        """прямой путь между вершинами"""
        graph = {1: [(2, 5)], 2: [(1, 5)]}
        dist, path = dijkstra_with_path(graph, start=1, end=2)
        assert dist == 5
        assert path == [1, 2]

    def test_path_through_intermediate(self):
        """путь через промежуточную вершину"""
        graph = {
            1: [(2, 1)],
            2: [(1, 1), (3, 1)],
            3: [(2, 1)]
        }
        dist, path = dijkstra_with_path(graph, start=1, end=3)
        assert dist == 2
        assert path == [1, 2, 3]

    def test_shortest_path_not_direct(self):
        """кратчайший путь не прямой"""
        graph = {
            1: [(2, 10), (3, 2)],
            2: [(1, 10), (3, 3)],
            3: [(1, 2), (2, 3)]
        }
        dist, path = dijkstra_with_path(graph, start=1, end=2)
        assert dist == 5
        assert path == [1, 3, 2]

    def test_unreachable_destination(self):
        """недостижимая конечная вершина"""
        graph = {
            1: [(2, 1)],
            2: [(1, 1)],
            3: []
        }
        dist, path = dijkstra_with_path(graph, start=1, end=3)
        assert dist == float('inf')
        assert path == []

    def test_start_equals_end(self):
        """начальная и конечная вершина совпадают"""
        graph = {1: [(2, 5)], 2: [(1, 5)]}
        dist, path = dijkstra_with_path(graph, start=1, end=1)
        assert dist == 0
        assert path == [1]

    def test_complex_path(self):
        """сложный путь в графе"""
        graph = {
            1: [(2, 2), (3, 4)],
            2: [(1, 2), (4, 1)],
            3: [(1, 4), (4, 1)],
            4: [(2, 1), (3, 1)]
        }
        dist, path = dijkstra_with_path(graph, start=1, end=4)
        assert dist == 3
        assert path == [1, 2, 4]

    def test_long_path(self):
        """длинный путь через много вершин"""
        graph = {
            1: [(2, 1)],
            2: [(1, 1), (3, 1)],
            3: [(2, 1), (4, 1)],
            4: [(3, 1), (5, 1)],
            5: [(4, 1)]
        }
        dist, path = dijkstra_with_path(graph, start=1, end=5)
        assert dist == 4
        assert path == [1, 2, 3, 4, 5]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
