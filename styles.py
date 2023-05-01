# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
import qdarktheme

from variables import darkerPrimaryColor, darkestPrimaryColor, primaryColor

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {primaryColor};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {darkerPrimaryColor};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {darkestPrimaryColor};
    }}
"""


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{primaryColor}",
            },
        },
        additional_qss=qss
    )
