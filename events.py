import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

# QMainWindow'dan türetilmiş özelleştirilmiş ana pencere sınıfı
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # Üst sınıfın başlatıcı metodunun çağrılması
        self.label = QLabel("Click in this window") # Etiket oluşturma
        self.setCentralWidget(self.label) # Pencerenin merkezi bileşeni olarak etiketi ayarlama

    # Fare hareket olayını yakalayan metot
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    # Fare basma olayını yakalayan metot
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent RIGHT")

    # Fare bırakma olayını yakalayan metot
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    # Fare çift tıklama olayını yakalayan metot
    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

# QApplication nesnesinin oluşturulması
app = QApplication(sys.argv)

# Özelleştirilmiş MainWindow sınıfından bir nesne oluşturulması
window = MainWindow()
window.show() # Pencerenin gösterilmesi

# Uygulamanın ana döngüsünün başlatılması
app.exec()
