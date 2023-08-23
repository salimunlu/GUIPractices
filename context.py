import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu


# QMainWindow'dan türetilmiş ana pencere sınıfı
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Üst sınıfın başlatıcı metodunun çağrılması
        self.show()  # Pencerenin gösterilmesi

        # Sağ tıklama menüsü için özel bir politika belirlenmesi
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # Özel sağ tıklama menüsünün çağrılması gerektiğinde bağlantı kurulması
        self.customContextMenuRequested.connect(self.on_context_menu)

    # Sağ tıklama menüsünün oluşturulması ve gösterilmesi
    def on_context_menu(self, pos):
        context = QMenu(self)  # Yeni bir menü nesnesi oluşturma
        context.addAction(QAction("test 1", self))  # Menüye aksiyonlar eklenmesi
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        # Menünün, sağ tıklama pozisyonuna uygun bir yerde görüntülenmesi
        context.exec(self.mapToGlobal(pos))


# QApplication nesnesinin oluşturulması
app = QApplication(sys.argv)

# Özelleştirilmiş MainWindow sınıfından bir nesne oluşturulması
window = MainWindow()
window.show()  # Pencerenin gösterilmesi (zaten __init__ metodunda da gösteriliyor)

# Uygulamanın ana döngüsünün başlatılması
app.exec()
