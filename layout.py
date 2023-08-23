import sys

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTabWidget,
)


# Renkli bir QWidget oluşturmak için kullanılan sınıf
class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)  # Arka planın otomatik olarak doldurulmasını sağla

        palette = self.palette()  # Mevcut paleti al
        palette.setColor(QPalette.ColorRole.Window, QColor(color))  # Paletin pencere rengini ayarla
        self.setPalette(palette)  # Paleti widget'a uygula


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")  # Pencere başlığını ayarla

        tabs = QTabWidget()  # Sekmeli bir widget oluştur
        tabs.setTabPosition(QTabWidget.TabPosition.West)  # Sekmelerin pozisyonunu batıya ayarla
        tabs.setMovable(True)  # Sekmelerin taşınabilir olmasını sağla

        # Belirtilen renkler için sekmeler oluştur
        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)  # Sekmeli widget'a renkli bir sekme ekle

        self.setCentralWidget(tabs)  # Pencerenin merkezi widget'ını ayarla


# QApplication nesnesi oluştur
app = QApplication(sys.argv)

# Özelleştirilmiş MainWindow sınıfından bir nesne oluştur
window = MainWindow()
window.show()  # Pencereyi göster

# Uygulamanın ana döngüsünü başlat
app.exec()
