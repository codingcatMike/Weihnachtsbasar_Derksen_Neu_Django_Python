import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout

class WebsiteWindow(QWidget):
    def __init__(self, url):
        super().__init__()
        self.initUI(url)

    def initUI(self, url):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Test Website")
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebsiteWindow("0.0.0.0:8000")
    window.show()
    sys.exit(app.exec_())