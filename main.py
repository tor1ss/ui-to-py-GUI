import os
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QVBoxLayout, QLabel, QMessageBox
except ImportError as e:
    os.system('pip install PyQt5')
    os.system('pip install PyQt5-tools')
finally:
    light_theme_stylesheet = """
    QWidget {
        background-color: #f0f0f0;  /* Светлый фон */
        color: #000000;              /* Черный текст */
    }
    
    QPushButton {
        background-color: #e0e0e0;  /* Светлая кнопка */
        border: 1px solid #a0a0a0;  /* Серый бордер */
        padding: 5px;
        border-radius: 4px;         /* Закругленные углы */
    }
    
    QPushButton:hover {
        background-color: #d0d0d0;  /* Цвет кнопки при наведении */
    }
    
    QMenuBar {
        background-color: #f0f0f0;  /* Фон меню */
    }
    
    QMenu {
        background-color: #f0f0f0;   /* Фон выпадающего меню */
    }
    
    QMenu::item {
        background-color: transparent; /* Фон элемента меню */
    }
    
    QMenu::item:selected {
        background-color: #d0d0d0; /* Цвет элемента при наведении */
    }
    
    QLabel {
        font-size: 14px;             /* Размер шрифта для меток */
    }
    
    QLineEdit {
        background-color: #ffffff;   /* Белый фон для поля ввода */
        border: 1px solid #a0a0a0;   /* Серый бордер */
    }
    """

    dark_theme_stylesheet = """
    QWidget {
        background-color: #2c2c2c;  /* Темный фон */
        color: #ffffff;              /* Белый текст */
    }
    
    QPushButton {
        background-color: #3e3e3e;  /* Темная кнопка */
        border: 1px solid #5e5e5e;  /* Светло-серый бордер */
        padding: 5px;
        border-radius: 4px;         /* Закругленные углы */
    }
    
    QPushButton:hover {
        background-color: #4e4e4e;  /* Цвет кнопки при наведении */
    }
    
    QMenuBar {
        background-color: #2c2c2c;  /* Фон меню */
    }
    
    QMenu {
        background-color: #2c2c2c;   /* Фон выпадающего меню */
    }
    
    QMenu::item {
        background-color: transparent; /* Фон элемента меню */
    }
    
    QMenu::item:selected {
        background-color: #4e4e4e; /* Цвет элемента при наведении */
    }
    
    QLabel {
        font-size: 14px;             /* Размер шрифта для меток */
    }
    
    QLineEdit {
        background-color: #444444;   /* Темный фон для поля ввода */
        border: 1px solid #5e5e5e;   /* Светло-серый бордер */
    }
    """

    class HelpWindow(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Справка")
            self.setGeometry(100, 100, 400, 300)
            self.setWindowIcon(QtGui.QIcon('docs/logo.ico'))
            layout = QtWidgets.QVBoxLayout()

            # Добавление текста справки
            help_text = QtWidgets.QLabel(
                "Данная программа предназначена для работы с файлами формата `.ui`, созданными в Qt Designer.\n\n"
                "Она позволяет пользователю выбирать файлы, конвертировать их в Python-код и сохранять в указанной директории.\n\n"
                "Основные функции:\n"
                "1. Выбор файла: Нажмите кнопку 'Выбрать файл', чтобы открыть диалог выбора файла...\n"
                "2. Конвертация: После выбора файла, нажмите кнопку 'Конвертировать' и укажите имя и путь для файла.\n\n"
                "Темы оформления:\n"
                "Программа поддерживает две темы оформления: светлую и темную/\n\n"
                "Справка и поддержка:\n"
                "Если у вас возникли вопросы или проблемы с использованием программы напишите об этом на странице github\n\n"
                "О программе:\n"
                "Вы можете узнать больше о программе, выбрав пункт 'О программе' в меню.")
            layout.addWidget(help_text)

            self.setLayout(layout)

    class About_programm(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Справка")
            self.setGeometry(100, 100, 400, 300)
            self.setWindowIcon(QtGui.QIcon('docs/logo.ico'))

            layout = QtWidgets.QVBoxLayout()

            help_text = QtWidgets.QLabel("Название программы: Конвертер UI в Python\n\n"
                                         "Версия: 1.0.0\n\n"
                                         "Описание:\n"
                                         "Данная программа предназначена для конвертации файлов формата .ui, "
                                         "созданных в Qt Designer, в Python-код. Она предоставляет пользователю простой "
                                         "и интуитивно понятный интерфейс для выбора файлов и директории сохранения.\n\n"
                                         "Основные функции:\n"
                                         "- Выбор файла: Позволяет пользователю выбрать файл .ui для конвертации.\n"
                                         "- Конвертация: Программа выполняет конвертацию выбранного файла и сохраняет его в указанную директорию "
                                         "результат в указанной директории.\n"
                                         "- Темы оформления: Поддержка светлой и темной тем.\n\n"
                                         "Разработчик: toriss__\n\n"
                                         "Контакты: belnik422@gmail.com")
            layout.addWidget(help_text)

            self.setLayout(layout)


    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.setFixedSize(250, 170)
            MainWindow.setWindowIcon(QtGui.QIcon('docs/logo.ico'))
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.label_choice_file = QtWidgets.QLabel(self.centralwidget)
            self.label_choice_file.setGeometry(QtCore.QRect(0, 0, 250, 50))
            self.label_choice_file.setOpenExternalLinks(False)
            self.label_choice_file.setObjectName("label_choice_file")
            self.btn_converte = QtWidgets.QPushButton(self.centralwidget)
            self.btn_converte.setGeometry(QtCore.QRect(30, 100, 201, 23))
            self.btn_converte.setObjectName("btn_converte")
            self.btn_open_file = QtWidgets.QPushButton(self.centralwidget)
            self.btn_open_file.setGeometry(QtCore.QRect(30, 60, 201, 23))
            self.btn_open_file.setObjectName("btn_choice_file")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 21))
            self.menubar.setObjectName("menubar")
            self.menu_file = QtWidgets.QMenu(self.menubar)
            self.menu_file.setObjectName("menu_file")
            self.menu_view = QtWidgets.QMenu(self.menubar)
            self.menu_view.setObjectName("menu_view")
            self.menu_3 = QtWidgets.QMenu(self.menu_view)
            self.menu_3.setObjectName("menu_3")
            self.menu_FAQ = QtWidgets.QMenu(self.menubar)
            self.menu_FAQ.setObjectName("menu_FAQ")
            MainWindow.setMenuBar(self.menubar)
            self.action_open = QtWidgets.QAction(MainWindow)
            self.action_open.setObjectName("action_open")
            self.action_save = QtWidgets.QAction(MainWindow)
            self.action_save.setObjectName("action_save")
            self.action_exit = QtWidgets.QAction(MainWindow)
            self.action_exit.setObjectName("action_exit")
            self.action_dark_theme = QtWidgets.QAction(MainWindow)
            self.action_dark_theme.setObjectName("action_dark_theme")
            self.action_light_theme = QtWidgets.QAction(MainWindow)
            self.action_light_theme.setObjectName("action_light_theme")
            self.action_help = QtWidgets.QAction(MainWindow)
            self.action_help.setObjectName("action_look_FAQ")
            self.action_about_programm = QtWidgets.QAction(MainWindow)
            self.action_about_programm.setObjectName("action_about_programm")
            self.menu_file.addAction(self.action_open)
            self.menu_file.addAction(self.action_save)
            self.menu_file.addSeparator()
            self.menu_file.addAction(self.action_exit)
            self.menu_3.addAction(self.action_dark_theme)
            self.menu_3.addAction(self.action_light_theme)
            self.menu_view.addAction(self.menu_3.menuAction())
            self.menu_FAQ.addAction(self.action_help)
            self.menu_FAQ.addSeparator()
            self.menu_FAQ.addAction(self.action_about_programm)
            self.menubar.addAction(self.menu_file.menuAction())
            self.menubar.addAction(self.menu_view.menuAction())
            self.menubar.addAction(self.menu_FAQ.menuAction())

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

            self.main_logic()

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "UI to Py"))
            self.label_choice_file.setText(_translate("MainWindow", "Выберите ui файл."))
            self.btn_converte.setText(_translate("MainWindow", "Конвертировать"))
            self.btn_open_file.setText(_translate("MainWindow", "Выбрать файл"))
            self.menu_file.setTitle(_translate("MainWindow", "Файл"))
            self.menu_view.setTitle(_translate("MainWindow", "Вид"))
            self.menu_3.setTitle(_translate("MainWindow", "Тема"))
            self.menu_FAQ.setTitle(_translate("MainWindow", "Справка"))
            self.action_open.setText(_translate("MainWindow", "Открыть"))
            self.action_save.setText(_translate("MainWindow", "Сохранить"))
            self.action_exit.setText(_translate("MainWindow", "Выход"))
            self.action_dark_theme.setText(_translate("MainWindow", "Темная"))
            self.action_light_theme.setText(_translate("MainWindow", "Светлая"))
            self.action_help.setText(_translate("MainWindow", "Просмотреть справку"))
            self.action_about_programm.setText(_translate("MainWindow", "О программе"))





        def main_logic(self):
            self.file_name = ''
            self.save_directory = ''
            QtWidgets.qApp.setStyleSheet(light_theme_stylesheet)

            self.action_light_theme.triggered.connect(self.on_action_light_theme_triggered)
            self.action_dark_theme.triggered.connect(self.on_action_dark_theme_triggered)

            self.action_help.triggered.connect(self.open_help_window)
            self.action_about_programm.triggered.connect(self.open_about_programm)

            self.action_open.triggered.connect(self.open_file)
            self.btn_open_file.clicked.connect(self.open_file)


            self.action_save.triggered.connect(self.convert)
            self.btn_converte.clicked.connect(self.convert)


            self.action_exit.triggered.connect(self.exit_programm)



        def open_file(self):
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            self.file_name, _ = QFileDialog.getOpenFileName(None, 'Открыть файл', '', 'Designer UI files (*.ui)',
                                                            options=options)

            if self.file_name:
                self.label_choice_file.setText('Выбранный файл: {}'.format(self.file_name))



        def convert(self):
            options = QFileDialog.Options()
            self.save_directory = QFileDialog.getSaveFileName(None, 'Выбрать директорию', '', 'Python file (*.py)',
                                                              options=options)[0]

            if not self.file_name:
                QMessageBox.critical(self.centralwidget, "Ошибка", "Выберите файл для конвертации!")
                return

            if not self.save_directory:
                QMessageBox.critical(self.centralwidget, "Ошибка", "Выберите директорию для сохранения!")
                return

            os.system(f'python -m PyQt5.uic.pyuic -x {self.file_name} -o {self.save_directory}')

            QMessageBox.information(self.centralwidget, "Успех", "Файл успешно конвертирован!")




        def on_action_light_theme_triggered(self):
            QtWidgets.qApp.setStyleSheet(light_theme_stylesheet)

        def on_action_dark_theme_triggered(self):
            QtWidgets.qApp.setStyleSheet(dark_theme_stylesheet)



        def open_help_window(self):
            self.help_window = HelpWindow()
            self.help_window.show()

        def open_about_programm(self):
            self.about_programm_window = About_programm()
            self.about_programm_window.show()



        def exit_programm(self):
            exit(0)

    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
