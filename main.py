import networkx as nx
import matplotlib.pyplot as plt


# Класс, представляющий инструмент для создания и редактирования графических диаграмм
class GraphEditor:
    def __init__(self):
        self.graph = nx.Graph()  # Используем объект графа из библиотеки networkx

    def add_node(self, node):
        # Добавляем узел в граф
        self.graph.add_node(node)

    def add_edge(self, node1, node2):
        # Добавляем ребро между двумя узлами
        self.graph.add_edge(node1, node2)

    def remove_node(self, node):
        # Удаляем узел из графа
        self.graph.remove_node(node)

    def remove_edge(self, node1, node2):
        # Удаляем ребро между двумя узлами
        self.graph.remove_edge(node1, node2)

    def plot(self, layout='spring'):
        # Визуализируем граф с использованием matplotlib
        plt.figure()
        if layout == 'spring':
            pos = nx.spring_layout(self.graph)  # Позиционирование узлов с использованием spring layout
        elif layout == 'circular':
            pos = nx.circular_layout(self.graph)  # Круговое позиционирование узлов
        elif layout == 'random':
            pos = nx.random_layout(self.graph)  # Случайное позиционирование узлов
        elif layout == 'shell':
            pos = nx.shell_layout(self.graph)  # Позиционирование в виде оболочки
        else:
            pos = nx.spring_layout(self.graph)  # Значение по умолчанию

        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=500)
        plt.title("Graph Visualization")
        plt.show()


# Пример использования GraphEditor
editor = GraphEditor()

# Добавляем узлы
editor.add_node('A')
editor.add_node('B')
editor.add_node('C')

# Добавляем ребра
editor.add_edge('A', 'B')
editor.add_edge('B', 'C')

# Визуализируем граф
editor.plot(layout='circular')

# Удаляем узел
editor.remove_node('C')

# Визуализируем после удаления узла
editor.plot(layout='spring')