# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(595, 481)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(76, 5, 76, 5)
        self.pushButton_re_login = QPushButton(Form)
        self.pushButton_re_login.setObjectName(u"pushButton_re_login")

        self.horizontalLayout.addWidget(self.pushButton_re_login)

        self.pushButton_break = QPushButton(Form)
        self.pushButton_break.setObjectName(u"pushButton_break")

        self.horizontalLayout.addWidget(self.pushButton_break)

        self.pushButton_random = QPushButton(Form)
        self.pushButton_random.setObjectName(u"pushButton_random")

        self.horizontalLayout.addWidget(self.pushButton_random)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 800)

        self.retranslateUi(Form)
        self.pushButton_break.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.pushButton_re_login.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u767b\u9646", None))
        self.pushButton_break.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.pushButton_random.setText(QCoreApplication.translate("Form", u"\u968f\u673a\u56fe\u7247", None))
    # retranslateUi

