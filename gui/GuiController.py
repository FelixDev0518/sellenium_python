import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("WebAutoClickertest.ui")[0]

url = "https://doc.qt.io/qt-5/designer-layouts.html"

class MyWindow(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.go.clicked.connect(lambda: self.goClicked())
        self.webEngineView.load(QUrl(url))
        self.webEngineView.urlChanged.connect(lambda: self.urlChanedFunction())
        self.RunJavascript_btn.clicked.connect(lambda: self.inputText())
        self.AutoButton.clicked.connect(lambda: self.autoTest())

    def inputText(self):
        self.webEngineView.page().runJavaScript('document.getElementById("gsc-i-id1").value = "Hi";')
        self.webEngineView.page().runJavaScript('window.location.reload();')

    def autoTest(self):
        # self.webEngineView.page().runJavaScript('''document.getElementById("gsc-i-id1").value = "Novak";''')
        self.webEngineView.page().runJavaScript('window.location.reload();')
        self.webEngineView.page().runJavaScript('''
                                                var linkHref = document.getElementsByClassName("mm-link")[1];
                                                var event = document.createEvent("MouseEvents");
                                                event.initEvent("click",true,false);
                                                linkHref.dispatchEvent(event);''')

    def urlChanedFunction(self):
        self.lineEdit.setText(self.webEngineView.url().toString())
    def goClicked(self):
        self.webEngineView.load(QUrl(self.lineEdit.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
