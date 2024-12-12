import sys
from pathlib import Path

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.load()
        self.ui.studentLW.itemClicked.connect(self.student_change)
        self.ui.auStudentLW.itemClicked.connect(self.second_change)
        self.ui.acceptButton.clicked.connect(self.file)
        self.ui.addButton.clicked.connect(self.add_student)
        self.show()

    def load(self):
        if Path('./students.txt').exists() and Path('./august_students.txt').exists():
            with open('students.txt', 'r') as f:
                students = f.read().splitlines()
            with open('august_students.txt', 'r') as f:
                august_students = f.read().splitlines()

            self.ui.studentLW.clear()
            self.ui.studentLW.addItems(students)
            self.ui.auStudentLW.clear()
            self.ui.auStudentLW.addItems(august_students)

            for item in students:
                self.ui.deleteBox.addItem(item)
    def update_students(self):
        august_students = [self.ui.auStudentLW.item(i).text() for i in range(self.ui.auStudentLW.count())]
        students = [self.ui.studentLW.item(i).text() for i in range(self.ui.studentLW.count())]

        self.ui.studentLW.clear()
        for student in students + august_students:
            self.ui.deleteBox.addItem(student)

    def student_change(self):
        #students = self.ui.studentLW.selectedItems()
        #for student in students:
         #   self.ui.auStudentLW.addItem(student.text())
        student = self.ui.studentLW.takeItem(self.ui.studentLW.currentRow()) #zwraca aktualnie wybrany wiersz
        self.ui.auStudentLW.addItem(student.text())

    def second_change(self):
        student = self.ui.auStudentLW.takeItem(self.ui.auStudentLW.currentRow())  # zwraca aktualnie wybrany wiersz
        self.ui.studentLW.addItem(student.text())

    def file(self):
        # lista = []
        # for element in range(self.ui.auStudentLW.count()):
        #     lista.append(self.ui.auStudentLW.item(element).text())
        # plik = open('wynik.txt', "w")
        # plik.write('\n'.join(lista))
        # plik.close()

        # WERSJA Z LEKCJI
        august_students = [self.ui.auStudentLW.item(i).text() for i in range(self.ui.auStudentLW.count())]
        with open('august_students.txt', "w") as f:
            for s in august_students:
                f.write(s + '\n')

        students = [self.ui.studentLW.item(i).text() for i in range(self.ui.studentLW.count())]
        with open('students.txt', "w") as f:
            for s in students:
                f.write(s + '\n')
    def add_student(self):
        uczen = self.ui.formEdit.text()
        self.ui.studentLW.addItem(uczen)
        self.update_students() #musi to byc ostatnia linijka

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())