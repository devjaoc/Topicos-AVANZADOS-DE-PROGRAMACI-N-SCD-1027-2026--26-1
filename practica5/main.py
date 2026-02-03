from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel
import sys, datetime

app = QApplication(sys.argv)
label = QLabel()
label.show()

def tick():
    label.setText(datetime.datetime.now().strftime("%H:%M:%S"))

timer = QTimer()
timer.timeout.connect(tick)
timer.start(1000)  # cada 1000 ms
sys.exit(app.exec_())