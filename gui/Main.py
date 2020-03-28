# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WebAutoClickertest.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl

url = "https://doc.qt.io/qt-5/designer-layouts.html"

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1006, 827)
        Dialog.setMinimumSize(QtCore.QSize(30, 0))
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RunJavascript_btn = QtWidgets.QPushButton(Dialog)
        self.RunJavascript_btn.setMaximumSize(QtCore.QSize(800, 16777215))
        self.RunJavascript_btn.setObjectName("RunJavascript_btn")
        self.horizontalLayout_2.addWidget(self.RunJavascript_btn)
        self.AutoButton = QtWidgets.QPushButton(Dialog)
        self.AutoButton.setObjectName("AutoButton")
        self.horizontalLayout_2.addWidget(self.AutoButton)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(859, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.go = QtWidgets.QPushButton(Dialog)
        self.go.setObjectName("go")
        self.horizontalLayout.addWidget(self.go)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout.addWidget(self.webEngineView, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.go.clicked.connect(lambda: self.goClicked())
        self.webEngineView.load(QUrl(url))
        self.webEngineView.urlChanged.connect(lambda: self.urlChanedFunction())
        self.RunJavascript_btn.clicked.connect(lambda: self.inputText())
        self.AutoButton.clicked.connect(lambda: self.autoTest())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.RunJavascript_btn.setText(_translate("Dialog", "RunJavaScript"))
        self.AutoButton.setText(_translate("Dialog", "Auto"))
        self.go.setText(_translate("Dialog", "Go"))

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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
