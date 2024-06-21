# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zh.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(356, 300)
        widget.setMinimumSize(QSize(356, 300))
        widget.setMaximumSize(QSize(356, 300))
        icon = QIcon(QIcon.fromTheme(u"emblem-shared"))
        widget.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_img = QLabel(widget)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setPixmap(QPixmap(u"app/images/16pic_8707727_b.jpg"))
        self.label_img.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_img)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 10, 14, 4)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_account = QLineEdit(widget)
        self.lineEdit_account.setObjectName(u"lineEdit_account")
        self.lineEdit_account.setMinimumSize(QSize(0, 28))
        self.lineEdit_account.setEchoMode(QLineEdit.EchoMode.Normal)

        self.horizontalLayout.addWidget(self.lineEdit_account)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_password = QLineEdit(widget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(0, 28))
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_password)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(36, -1, 76, -1)
        self.checkBox_aoto_login = QCheckBox(widget)
        self.checkBox_aoto_login.setObjectName(u"checkBox_aoto_login")
        self.checkBox_aoto_login.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(8)
        self.checkBox_aoto_login.setFont(font1)

        self.horizontalLayout_4.addWidget(self.checkBox_aoto_login)

        self.checkBox_remember = QCheckBox(widget)
        self.checkBox_remember.setObjectName(u"checkBox_remember")
        self.checkBox_remember.setFont(font1)

        self.horizontalLayout_4.addWidget(self.checkBox_remember)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_register = QPushButton(widget)
        self.pushButton_register.setObjectName(u"pushButton_register")
        self.pushButton_register.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_3.addWidget(self.pushButton_register)

        self.pushButton_login = QPushButton(widget)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_3.addWidget(self.pushButton_login)

        self.pushButton_fpwd = QPushButton(widget)
        self.pushButton_fpwd.setObjectName(u"pushButton_fpwd")
        self.pushButton_fpwd.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_3.addWidget(self.pushButton_fpwd)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u7528\u6237\u767b\u9646", None))
        self.label_img.setText("")
        self.label_2.setText(QCoreApplication.translate("widget", u"\u8d26\u53f7", None))
        self.lineEdit_account.setPlaceholderText(QCoreApplication.translate("widget", u"\u8f93\u5165Email", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"\u5bc6\u7801", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("widget", u"\u8f93\u5165\u5bc6\u7801", None))
        self.checkBox_aoto_login.setText(QCoreApplication.translate("widget", u"\u81ea\u52a8\u767b\u9646", None))
        self.checkBox_remember.setText(QCoreApplication.translate("widget", u"\u8bb0\u4f4f\u6211", None))
        self.pushButton_register.setText(QCoreApplication.translate("widget", u"\u6ce8\u518c", None))
        self.pushButton_login.setText(QCoreApplication.translate("widget", u"\u767b\u9646", None))
        self.pushButton_fpwd.setText(QCoreApplication.translate("widget", u"\u5fd8\u8bb0\u5bc6\u7801?", None))
    # retranslateUi

