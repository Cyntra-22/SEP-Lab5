import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import QSoundEffect

class Language_Animation(QWidget):
    def __init__(self, name, frame):
        super().__init__()
        self.name = name
        self.animation_frames = []
        self.frame = frame
        for i in range(self.frame):
            self.animation_frames.append(QPixmap(f"images/{name}{str(i + 1)}.png"))
        self.frame_index = 0
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.update_animation)
        self.animation_timer.start(75)

    def update_animation(self):
        self.frame_index += 1
        if self.frame_index >= self.frame:
            self.frame_index = 0
        self.update()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.animation_frames[self.frame_index])

class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coding Game Homepage")
        self.setGeometry(100, 100, 800, 400)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.language_label = QLabel()
        self.language_label.setText("Select a Course:")
        self.layout.addWidget(self.language_label)
        self.language_label.setAlignment(Qt.AlignTop)
        self.language_label.setFont(QFont("Arial", 20))

        self.python_button = QPushButton('Python')
        self.python_button.clicked.connect(self.python)
        self.layout.addWidget(self.python_button)

        self.java_button = QPushButton('Java')
        self.java_button.clicked.connect(self.java)
        self.layout.addWidget(self.java_button)
        self.setLayout(self.layout)

    def python(self):
        if hasattr(self, "java_animation"):
            self.layout.removeWidget(self.java_animation)
            self.layout.removeWidget(self.confirm_bt)
        self.python_animation = Language_Animation("python", 70)
        self.layout.addWidget(self.python_animation)
        self.confirm_bt = QPushButton('Confirm')
        self.confirm_bt.clicked.connect(self.confirm)
        self.layout.addWidget(self.confirm_bt)

    def java(self):
        if hasattr(self, "python_animation"):
            self.layout.removeWidget(self.python_animation)
            self.layout.removeWidget(self.confirm_bt)
        self.java_animation = Language_Animation("java", 1)
        self.layout.addWidget(self.java_animation)
        self.confirm_bt = QPushButton('Confirm')
        self.confirm_bt.clicked.connect(self.confirm)
        self.layout.addWidget(self.confirm_bt)
    
    def confirm(self):
        self.click = QSoundEffect()
        self.click.setSource(QUrl.fromLocalFile("sounds/press.wav")) 
        self.click.play()
            
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText("Starting Game...")
        layout.addWidget(label)
        close_button = QPushButton("Close window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show() 


def main():
    app = QApplication(sys.argv)
    window = HomePage()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
