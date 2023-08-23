# PyQt6 kütüphanesinden gerekli modüllerin ithal edilmesi
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys


# QMainWindow sınıfından türetilen özelleştirilmiş ana pencere sınıfı
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Üst sınıfın başlatıcı metodunun çağrılması

        self.setWindowTitle("My App")  # Pencere başlığının ayarlanması
        button = QPushButton("Press Me!")  # Buton oluşturulması
        self.setMinimumSize(QSize(300, 300))  # Pencere minimum boyutunun ayarlanması

        # Pencerenin merkezi bileşeni olarak butonun ayarlanması
        self.setCentralWidget(button)


# QApplication nesnesinin oluşturulması
app = QApplication(sys.argv)

# Özelleştirilmiş MainWindow sınıfından bir nesne oluşturulması
window = MainWindow()
window.show()  # Pencerenin gösterilmesi

# Uygulamanın ana döngüsünün başlatılması
app.exec()
