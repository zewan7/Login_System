# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(271, 273)
        icon = QIcon(QIcon.fromTheme(u"contact-new"))
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 9, 12, 4)
        self.pushButton_okAccount = QPushButton(self.groupBox)
        self.pushButton_okAccount.setObjectName(u"pushButton_okAccount")
        self.pushButton_okAccount.setMinimumSize(QSize(0, 28))
        self.pushButton_okAccount.setFont(font)

        self.gridLayout.addWidget(self.pushButton_okAccount, 7, 0, 1, 2)

        self.lineEdit_name = QLineEdit(self.groupBox)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(0, 28))

        self.gridLayout.addWidget(self.lineEdit_name, 1, 1, 1, 3)

        self.lineEdit_email = QLineEdit(self.groupBox)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setMinimumSize(QSize(0, 28))

        self.gridLayout.addWidget(self.lineEdit_email, 2, 1, 1, 3)

        self.lineEdit_pwd = QLineEdit(self.groupBox)
        self.lineEdit_pwd.setObjectName(u"lineEdit_pwd")
        self.lineEdit_pwd.setMinimumSize(QSize(0, 28))
        self.lineEdit_pwd.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_pwd, 4, 1, 1, 3)

        self.label_led = QLabel(self.groupBox)
        self.label_led.setObjectName(u"label_led")
        self.label_led.setStyleSheet(u"color: rgb(255, 0, 127);")

        self.gridLayout.addWidget(self.label_led, 0, 0, 1, 4)

        self.pushButton_get_vCode = QPushButton(self.groupBox)
        self.pushButton_get_vCode.setObjectName(u"pushButton_get_vCode")
        self.pushButton_get_vCode.setMinimumSize(QSize(0, 28))

        self.gridLayout.addWidget(self.pushButton_get_vCode, 3, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.lineEdit_Vcode = QLineEdit(self.groupBox)
        self.lineEdit_Vcode.setObjectName(u"lineEdit_Vcode")
        self.lineEdit_Vcode.setMinimumSize(QSize(0, 28))

        self.gridLayout.addWidget(self.lineEdit_Vcode, 3, 1, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.pushButton_register = QPushButton(self.groupBox)
        self.pushButton_register.setObjectName(u"pushButton_register")
        self.pushButton_register.setMinimumSize(QSize(0, 28))
        self.pushButton_register.setFont(font)

        self.gridLayout.addWidget(self.pushButton_register, 7, 2, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.lineEdit_pwd_ok = QLineEdit(self.groupBox)
        self.lineEdit_pwd_ok.setObjectName(u"lineEdit_pwd_ok")
        self.lineEdit_pwd_ok.setMinimumSize(QSize(0, 28))
        self.lineEdit_pwd_ok.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_pwd_ok, 5, 1, 1, 3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7528\u6237\u6ce8\u518c", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u8d26\u53f7\u6ce8\u518c", None))
        self.pushButton_okAccount.setText(QCoreApplication.translate("Form", u"\u5df2\u6709\u8d26\u53f7", None))
        self.lineEdit_name.setText("")
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u7528\u6237\u540d", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u90ae\u7bb1", None))
        self.lineEdit_pwd.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5bc6\u7801", None))
        self.label_led.setText("")
        self.pushButton_get_vCode.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u9a8c\u8bc1\u7801", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u7528 \u6237 \u540d", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u90ae      \u7bb1", None))
        self.lineEdit_Vcode.setPlaceholderText(QCoreApplication.translate("Form", u"\u9a8c\u8bc1\u7801", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9a8c \u8bc1 \u7801", None))
        self.pushButton_register.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5bc6      \u7801", None))
        self.lineEdit_pwd_ok.setPlaceholderText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801", None))
    # retranslateUi

