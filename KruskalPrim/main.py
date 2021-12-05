from kruskal import *
from prim import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QFont, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem

winWidth1, winHeight1 = 1000, 600
winWidth2, winHeight2 = 1000, 700
winX, winY = 200, 200

# додаємо граф Graph(vert, res), де vert - кількість вершин
gKruskal = GraphKruskal(10)
gKruskal.addEdge(0, 1, 4)
gKruskal.addEdge(0, 4, 5)
gKruskal.addEdge(0, 5, 7)
gKruskal.addEdge(1, 2, 10)
gKruskal.addEdge(1, 3, 9)
gKruskal.addEdge(1, 4, 7)
gKruskal.addEdge(2, 6, 11)
gKruskal.addEdge(2, 3, 2)
gKruskal.addEdge(3, 4, 10)
gKruskal.addEdge(3, 6, 12)
gKruskal.addEdge(4, 7, 3)
gKruskal.addEdge(4, 8, 4)
gKruskal.addEdge(5, 8, 9)
gKruskal.addEdge(6, 7, 8)
gKruskal.addEdge(7, 9, 7)
gKruskal.addEdge(8, 9, 5)

gPrim = GraphPrim(10)
gPrim.graph = [[0, 4, 0, 0, 5, 7, 0, 0, 0, 0],
               [4, 0, 10, 9, 7, 0, 0, 0, 0, 0],
               [0, 10, 0, 2, 0, 0, 11, 0, 0, 0],
               [0, 9, 2, 0, 10, 0, 12, 0, 0, 0],
               [5, 7, 0, 10, 0, 0, 0, 3, 4, 0],
               [7, 0, 0, 0, 5, 7, 0, 0, 9, 0],
               [0, 0, 11, 12, 0, 0, 0, 8, 0, 0],
               [0, 0, 0, 0, 3, 0, 8, 0, 0, 7],
               [0, 0, 0, 0, 4, 9, 0, 0, 0, 5],
               [0, 0, 0, 0, 0, 0, 0, 7, 5, 0]]

gPrim.Prim()

# текстові константи:
txtTitle = 'Знаходження остовного дерева мінімальної ваги'
txtHello = 'Світайло Даніл ІН-01. Варіант 14. Програма для демонстрації роботи алгоритмів Крускала та Прима.'
txtInstruction = ('\nДана програма створена щоб продемонструвати роботу алгоритмів Крускала та Прима '
                  'для знаходження остовного дерева мінімальної ваги на прикладі наступного графу:' )
txtKruskal1 = '1. Спочатку необхідно відсортувати вагу ребер за зростанням'
txtKruskal2 = '2. Беремо першу вершину з відсортованих і йдемо до кінця масиву, в процесі перевіряючи на зациклювання'
txtResult = '3. Результат: '

txtPrim1 = '1. На вхід подається зв\'язний неорієнтований граф і для кожного ребра задається вага'
txtPrim2 = '2. Беремо довільну вершину і знаходимо ребро, що інцидентне їй та має найменшу вагу'
txtPrim3 = '3. Потім розглядаються ребра графа, один кінець яких — вершина, що вже належить дереву, а інший — ні; \n' \
           'з цих ребер вибирається ребро найменшої вартості. Ребро, що вибирається на кожному кроці, приєднується до дерева. \n' \
           'Зростання дерева відбувається доти, доки вичерпані всі вершини вихідного графа. \n' \
           'Результатом роботи алгоритму є остовне дерево мінімальної вартості.'


class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.btnKruskal = QPushButton('Вирішення за методом Крускала', self)
        self.btnPrim = QPushButton('Вирішення за методом Прима', self)
        self.helloText = QLabel(txtHello)
        self.instruction = QLabel(txtInstruction)
        self.pic = QLabel()

        self.initUI()
        self.connects()
        self.setAppear()
        self.show()



    def initUI(self):
        self.helloText.setFont(QFont('Times New Roman', weight=QFont.Bold))
        self.pic.setPixmap(QPixmap("graph.PNG"))

        layoutLine = QVBoxLayout()
        layoutLine.addWidget(self.helloText, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.instruction, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.pic, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.btnKruskal, alignment=Qt.AlignCenter)
        layoutLine.addWidget(self.btnPrim, alignment=Qt.AlignCenter)
        self.setLayout(layoutLine)

    def setAppear(self):
        self.setWindowTitle(txtTitle)
        self.resize(winWidth1, winHeight1)
        self.move(winX, winY)

    def connects(self):
        self.btnKruskal.clicked.connect(self.kruskalClick)
        self.btnPrim.clicked.connect(self.primClick)

    def kruskalClick(self):
        global tw
        tw = KruskalWindow()

    def primClick(self):
        global tw
        tw = PrimWindow()


class KruskalWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.text1 = QLabel(txtKruskal1)
        self.text2 = QLabel(txtKruskal2)

        string, result, assignments, comparisons = gKruskal.Kruskal()
        self.textMST = QLabel(string)
        self.text3 = QLabel(txtResult)
        self.result = QLabel("Вага мінімального остовного дерева: " + str(result) +
                             ". Кількість присвоювань: " + str(assignments) +
                             ". Кількість порівнянь: " + str(comparisons) + ".")
        self.table = QTableWidget()

        self.initUI()
        self.setAppear()

        self.show()

    def initUI(self):
        layoutLine = QVBoxLayout()
        layoutLine.addWidget(self.text1, alignment=Qt.AlignHCenter)
        self.table.setColumnCount(len(gKruskal.graph))
        self.table.setRowCount(2)
        self.table.setVerticalHeaderLabels(["Ребро", "Вага"])
        self.table.horizontalHeader().hide()

        i = 0
        for u, v, w in gKruskal.graph:
            self.table.setItem(0, i, QTableWidgetItem(str(u) + "-" + str(v)))
            self.table.setItem(1, i, QTableWidgetItem(str(w)))

            i += 1
        self.table.setMinimumWidth(winWidth2 - 50)
        self.table.setMaximumHeight(90)
        layoutLine.addWidget(self.table, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.text2, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.textMST, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.text3, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.result, alignment=Qt.AlignHCenter)
        self.setLayout(layoutLine)

    def setAppear(self):
        self.setWindowTitle(txtTitle)
        self.resize(winWidth2, winHeight2)
        self.move(winX, winY)


class PrimWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.text1 = QLabel(txtPrim1)
        self.text2 = QLabel(txtPrim2)

        string, result, assignments, comparisons = gPrim.Prim()

        self.text3 = QLabel(txtPrim3)
        self.text3.setAlignment(Qt.AlignHCenter)
        self.textMST = QLabel(string)
        self.text4 = QLabel(txtResult)
        self.result = QLabel("Вага мінімального остовного дерева: " + str(result) +
                             ". Кількість присвоювань: " + str(assignments) +
                             ". Кількість порівнянь: " + str(comparisons) + ".")
        self.initUI()
        self.setAppear()
        self.show()

    def initUI(self):
        layoutLine = QVBoxLayout()
        layoutLine.addWidget(self.text1, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.text2, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.text3, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.textMST, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.text4, alignment=Qt.AlignHCenter)
        layoutLine.addWidget(self.result, alignment=Qt.AlignHCenter)
        self.setLayout(layoutLine)

    def setAppear(self):
        self.setWindowTitle(txtTitle)
        self.resize(winWidth2, winHeight2)
        self.move(winX, winY)


def main():
    app = QApplication([])
    app.setFont(QFont('Times New Roman', 12), className='MainWindow')
    app.setFont(QFont('Times New Roman', 12), className='KruskalWindow')
    app.setFont(QFont('Times New Roman', 12), className='PrimWindow')

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor('white'))
    palette.setColor(QPalette.Text, QColor('red'))
    app.setPalette(palette)

    mw = MainWindow()
    mw.show()
    app.exec_()


if __name__ == "__main__":
    main()