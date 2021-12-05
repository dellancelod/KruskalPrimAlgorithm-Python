# Алгоритм Прима для знаходження остовного дерева мінімальної ваги

# Клас, що представляє граф
class GraphPrim:

    def __init__(self, vertices):
        self.V = vertices
        # Представляємо граф у вигляді матриці сміжності
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.assignment = 0
        self.comparison = 0

    # Функція, що знаходить вершину з мінімальним ребром серед тих вершин, що ще не включені в найкоротший шлях дерева
    def minKey(self, key, mstSet):

        min = 999

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
                self.comparison += 2
                self.assignment += 2

        return min_index

    # Функція, що будуємо мінімальне остовне дерево за методом Прима та повертає його вагу
    def Prim(self):

        tree = ""
        result = 0

        # Ключові значення для пошуку мінімальної ваги серед вакантних вершин
        key = [999] * self.V
        parent = [None] * self.V  # Масив, що зберігає мінімальне остовне дерево
        # Перша вершина буде та, котра занульована
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # Перший вузол це завжди корінь

        for cout in range(self.V):

            # Обираємо вершину з найменшим ребром з набору вершин
            u = self.minKey(key, mstSet)
            self.assignment += 1

            # Додаємо це ребро до мінімального остовного дерева
            mstSet[u] = True
            self.assignment += 1

            # Оновлюємо значення відстані сміжних вершин обраної вершини
            # тільки якщо дана відстань більша ніж нова відстань та вершини ще немає в дереві
            for v in range(self.V):

                # Оновлюємо ключ тільки якщо graph[u][v] менше ніж key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    self.comparison += 2
                    self.assignment += 2

        for i in range(1, self.V):
            tree += str(parent[i] + 1) + " -- " + str(i + 1) + " == " + str(self.graph[i][parent[i]]) + "\n"
            result += self.graph[i][parent[i]]

        return tree, result, self.assignment, self.comparison


