from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit

from utils import isEmpty, isNumOrDot
from variables import bigFontSize, minimumWidth, textMargin


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {bigFontSize}px;')
        self.setMinimumHeight(bigFontSize * 2)
        self.setMinimumWidth(minimumWidth)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(textMargin, textMargin, textMargin, textMargin)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()

        # Pressionou tecla ENTER ou =
        if self.isEq(event):
            self.eqPressed.emit()
            return event.ignore()

        # Pressionou tecla BACKSPACE
        if self.isDel(event):
            self.delPressed.emit()
            return event.ignore()

        # Pressionou tecla ESC ou C
        if self.isClear(event):
            self.clearPressed.emit()
            return event.ignore()

        # Pressionou uma dessas teclas + - / * P
        if self.isOperator(event):
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        # Não passar daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()

    def isEq(self, event: QKeyEvent):
        return event.key() in [Qt.Key.Key_Enter, Qt.Key.Key_Return, Qt.Key.Key_Equal]

    def isDel(self, event: QKeyEvent):
        return event.key() in [Qt.Key.Key_Backspace, Qt.Key.Key_Delete]

    def isClear(self, event: QKeyEvent):
        return event.key() in [Qt.Key.Key_Escape, Qt.Key.Key_C]

    def isOperator(self, event: QKeyEvent):
        return event.key() in [Qt.Key.Key_Plus, Qt.Key.Key_Minus, Qt.Key.Key_Slash, Qt.Key.Key_Asterisk, Qt.Key.Key_P]
