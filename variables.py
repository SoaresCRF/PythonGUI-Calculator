from pathlib import Path
from typing import Final

# Diretório
rootDir: Final = Path(__file__).parent
iconDir: Final = rootDir / 'icon'
windowIconPath: Final = iconDir / 'calculator.png'

# Font sizing
bigFontSize: Final = 40
mediumFontSize: Final = 24
smallFontSize: Final = 18
textMargin: Final = 15
minimumWidth: Final = 500

# Colors
primaryColor = '#1e81b0'
darkerPrimaryColor = '#16658a'
darkestPrimaryColor = '#115270'
