# Алгоритм Крускала для знаходження остовного дерева мінімальної ваги

# Клас, що представляє граф
class GraphKruskal:

    def __init__(self, vertices):
        self.V = vertices  # Кількість вершин
        self.graph = []  # Словник для значень графу

        self.assignments = 0  # Лічильник для кількості присвоювань
        self.comparisons = 0  # Лічильник для кількості порівнянь

    # Функція для додавання ребра графу
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # Рекурсивна функція, яка викликається щоб попередити зациклювання
    # (використовує метод стискання шляху)
    def find(self, parent, i):
        if parent[i] == i:
            self.comparisons += 1
            return i
        return self.find(parent, parent[i])

    # Функція, яка об'єднує корені х та у за рангом
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        self.assignments += 2

        # Додаємо дерево меншого рангу під корінь дерева більшого рангу
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
            self.comparisons += 1
            self.assignments += 1

        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
            self.comparisons += 1
            self.assignments += 1

        # Якщо ранги однакові, вершини відносяться до одного кореня, збільшуємо ранг на 1
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
            self.comparisons += 1
            self.assignments += 1

    # Головна функція, що будує мінімальне остовне дерево за Крускалом і повпртає його вагу
    def Kruskal(self):
        result = []  # Тут буде зберігатися результат мінімального дерева

        # Індекс для відсортованих ребер
        i = 0

        # Індекс для result[]
        e = 0

        parent = []
        rank = []

        # Крок 1: сортуємо граф за зростанням
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        # Створюємо набір вершин
        for node in range(self.V):
            parent.append(node)
            self.assignments += 1
            rank.append(0)

        # Алгоритм завершує роботу коли кількість вершин підграфа співпадає з кількістю вершин початкового графа
        while e < self.V - 1:
            self.comparisons += 1

            # Крок 2: беремо найменшу вершину з відсортованих і йдемо до кінця масиву
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            self.assignments += 3

            # Якщо додавання вершини не викликає зациклювання, то додаємо її до результату і продовжуємо
            if x != y:
                self.comparisons += 1
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # В іншому випадку вершину не додаємо

        minimumCost = 0
        string = ""
        for u, v, weight in result:
            minimumCost += weight
            string += str(u + 1) + " -- " + str(v + 1) + " == " + str(weight) + "\n"
        return string, minimumCost, self.assignments, self.comparisons

