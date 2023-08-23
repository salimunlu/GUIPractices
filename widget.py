import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


# QMainWindow sınıfını özelleştirerek uygulamanın ana penceresini oluşturun
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Üst sınıfın başlatıcısını çağır

        self.setWindowTitle("Widgets App")  # Pencere başlığını ayarla

        layout = QVBoxLayout()  # Dikey düzen oluştur

        # Eklemek istediğimiz widget'ları bir liste içinde sırala
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:  # Her bir widget'ı düzen içine ekle
            layout.addWidget(w())

        widget = QWidget()  # Ana pencere widget'ını oluştur
        widget.setLayout(layout)  # Düzeni widget'a uygula

        # Pencerenin merkezi widget'ını ayarla. Varsayılan olarak widget,
        # pencerenin tüm alanını kaplayacaktır.
        self.setCentralWidget(widget)


# QApplication nesnesi oluştur
app = QApplication(sys.argv)

# Özelleştirilmiş MainWindow sınıfından bir nesne oluştur
window = MainWindow()
window.show()  # Pencereyi göster

# Uygulamanın ana döngüsünü başlat
app.exec()
