import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from buttons import ButtonsGrid
from display import Display
from info import Info
from mainWindow import MainWindow
from styles import setupTheme
from variables import windowIconPath

if __name__ == '__main__':
    # Cria aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define icon
    app.setWindowIcon(QIcon(str(windowIconPath)))
    window.setWindowIcon(QIcon(str(windowIconPath)))

    # Info
    info = Info('My equation')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('Type here...')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
