import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import QSoundEffect

class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Surprise!")

        # Set black background color
        self.setStyleSheet("background-color: black;")

        # Create central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create a welcome label
        welcome_label = QLabel("Merry Christmas!", self)
        welcome_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)  # Align to the top and center horizontally
        welcome_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")

        # Create label for animation
        self.animation_label = QLabel(self)
        self.frame_no = 0
        self.images = [
            QPixmap("images/" + str(i + 1) + ".jpg")
            for i in range(11)
        ]
        self.animation_label.setPixmap(self.images[self.frame_no])

        # Create button for present
        present_button = QPushButton("Here's Your Present", self)
        present_button.clicked.connect(self.show_present_window)
        present_button.setStyleSheet("font-size: 18px; font-weight: bold; color: white; background-color: grey;")

        # Add widgets to layout
        layout.addWidget(welcome_label)
        layout.addWidget(self.animation_label, alignment=Qt.AlignCenter)
        layout.addWidget(present_button, alignment=Qt.AlignHCenter)

        # Set up a timer to switch frames
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(75)  # Adjust the timeout value as needed

        # Add sound effect
        self.sound_effect = QSoundEffect(self)
        self.sound_effect.setSource(QUrl.fromLocalFile("sounds/Hoho.wav"))
        self.sound_effect.setVolume(0.5)  # Adjust the volume as needed
        self.sound_effect.play()

    def update_value(self):
        self.frame_no += 1
        if self.frame_no >= 11:
            self.frame_no = 0
        self.animation_label.setPixmap(self.images[self.frame_no])

    def show_present_window(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()

        label = QLabel(self)
        present_text = "Congratulations! You got a special gift!"
        label.setText(present_text)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        layout.addWidget(label)

        close_btn = QPushButton("Close", self)
        close_btn.clicked.connect(dialog.close)
        layout.addWidget(close_btn)

        dialog.setLayout(layout)
        dialog.show()

        print("show_present_window called")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec())
