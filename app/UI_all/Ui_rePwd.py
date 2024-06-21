# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rePwd.ui'
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
        Form.resize(250, 253)
        icon = QIcon(QIcon.fromTheme(u"mail-message-new"))
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 20, -1)
        self.lineEdit_reNewPwd = QLineEdit(self.groupBox)
        self.lineEdit_reNewPwd.setObjectName(u"lineEdit_reNewPwd")
        self.lineEdit_reNewPwd.setMinimumSize(QSize(0, 28))
        self.lineEdit_reNewPwd.setMaxLength(32)
        self.lineEdit_reNewPwd.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_reNewPwd, 7, 1, 1, 2)

        self.lineEdit_reVcode = QLineEdit(self.groupBox)
        self.lineEdit_reVcode.setObjectName(u"lineEdit_reVcode")
        self.lineEdit_reVcode.setMinimumSize(QSize(0, 28))
        self.lineEdit_reVcode.setMaxLength(4)

        self.gridLayout.addWidget(self.lineEdit_reVcode, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.pushButton_reOk = QPushButton(self.groupBox)
        self.pushButton_reOk.setObjectName(u"pushButton_reOk")
        self.pushButton_reOk.setMinimumSize(QSize(0, 28))

        self.gridLayout.addWidget(self.pushButton_reOk, 9, 2, 1, 1)

        self.lineEdit_reEmailPath = QLineEdit(self.groupBox)
        self.lineEdit_reEmailPath.setObjectName(u"lineEdit_reEmailPath")
        self.lineEdit_reEmailPath.setMinimumSize(QSize(0, 28))

        self.gridLayout.addWidget(self.lineEdit_reEmailPath, 3, 1, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.label_reLed = QLabel(self.groupBox)
        self.label_reLed.setObjectName(u"label_reLed")
        self.label_reLed.setMinimumSize(QSize(0, 0))
        self.label_reLed.setStyleSheet(u"color: rgb(255, 0, 127);")

        self.gridLayout.addWidget(self.label_reLed, 0, 0, 1, 3)

        self.pushButton_reGetNum = QPushButton(self.groupBox)
        self.pushButton_reGetNum.setObjectName(u"pushButton_reGetNum")
        self.pushButton_reGetNum.setEnabled(True)
        self.pushButton_reGetNum.setMinimumSize(QSize(0, 28))
        font1 = QFont()
        font1.setPointSize(9)
        self.pushButton_reGetNum.setFont(font1)

        self.gridLayout.addWidget(self.pushButton_reGetNum, 5, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.pushButton_reReturn = QPushButton(self.groupBox)
        self.pushButton_reReturn.setObjectName(u"pushButton_reReturn")
        self.pushButton_reReturn.setMinimumSize(QSize(0, 28))
        self.pushButton_reReturn.setMaximumSize(QSize(68, 28))

        self.gridLayout.addWidget(self.pushButton_reReturn, 9, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4fee\u6539\u5bc6\u7801", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u91cd\u7f6e\u5bc6\u7801", None))
        self.lineEdit_reNewPwd.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u65b0\u5bc6\u7801", None))
        self.lineEdit_reVcode.setPlaceholderText(QCoreApplication.translate("Form", u"\u9a8c\u8bc1\u7801", None))
        self.pushButton_reOk.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.lineEdit_reEmailPath.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u90ae\u7bb1", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u90ae  \u7bb1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9a8c\u8bc1\u7801", None))
        self.label_reLed.setText("")
        self.pushButton_reGetNum.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u9a8c\u8bc1\u7801", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u65b0\u5bc6\u7801", None))
        self.pushButton_reReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
    # retranslateUi

