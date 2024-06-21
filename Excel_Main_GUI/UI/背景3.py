# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '背景3.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(821, 701)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(821, 701))
        MainWindow.setStyleSheet(u"QPushButton { \n"
"    background-image: url(gg03.png);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setWeight(QFont.ExtraBold)
        font1.setItalic(False)
        self.groupBox.setFont(font1)
        self.groupBox.setMouseTracking(False)
        self.groupBox.setStyleSheet(u"QPushButton{\n"
"	font-size:15px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover { \n"
"    color:red;\n"
"	font-size:18px;\n"
"	\n"
"}\n"
"\n"
"\n"
"#groupBox{\n"
"	font-weight:900;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout.setContentsMargins(11, 11, 11, -1)
        self.pushButton1 = QPushButton(self.groupBox)
        self.pushButton1.setObjectName(u"pushButton1")
        sizePolicy2.setHeightForWidth(self.pushButton1.sizePolicy().hasHeightForWidth())
        self.pushButton1.setSizePolicy(sizePolicy2)
        self.pushButton1.setBaseSize(QSize(0, 0))
        self.pushButton1.setIconSize(QSize(30, 30))
        self.pushButton1.setAutoRepeatDelay(300)
        self.pushButton1.setAutoRepeatInterval(100)

        self.verticalLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton(self.groupBox)
        self.pushButton2.setObjectName(u"pushButton2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton2.sizePolicy().hasHeightForWidth())
        self.pushButton2.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.pushButton2)

        self.pushButton4 = QPushButton(self.groupBox)
        self.pushButton4.setObjectName(u"pushButton4")
        sizePolicy3.setHeightForWidth(self.pushButton4.sizePolicy().hasHeightForWidth())
        self.pushButton4.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.pushButton4)

        self.pushButton3 = QPushButton(self.groupBox)
        self.pushButton3.setObjectName(u"pushButton3")
        sizePolicy3.setHeightForWidth(self.pushButton3.sizePolicy().hasHeightForWidth())
        self.pushButton3.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.pushButton3)

        self.pushButton5 = QPushButton(self.groupBox)
        self.pushButton5.setObjectName(u"pushButton5")
        sizePolicy3.setHeightForWidth(self.pushButton5.sizePolicy().hasHeightForWidth())
        self.pushButton5.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.pushButton5)

        self.pushButton_re_login = QPushButton(self.groupBox)
        self.pushButton_re_login.setObjectName(u"pushButton_re_login")

        self.verticalLayout.addWidget(self.pushButton_re_login)


        self.horizontalLayout.addWidget(self.groupBox)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(2, 6)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textEdit = QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_4.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(4, 12)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Excel\u6587\u4ef6\u5904\u7406", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u793a\uff1a\u8f93\u51fa\u6587\u4ef6\u5747\u5728\u684c\u9762\u3010\u8f93\u51fa\u6587\u4ef6\u5939\u3011\u4e2d", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879\u5361", None))
        self.pushButton1.setText(QCoreApplication.translate("MainWindow", u"\u2606  \u5408\u5e76Excel\u6570\u636e           ", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"\u2606  \u5408\u5e76csv\u6570\u636e             ", None))
        self.pushButton4.setText(QCoreApplication.translate("MainWindow", u"\u2606  \u5408\u5e76\u591a\u4e2aSheet\u6570\u636e        ", None))
        self.pushButton3.setText(QCoreApplication.translate("MainWindow", u"\u2606  \u6279\u91cf\u5408\u5e76Excel\u6570\u636e        ", None))
        self.pushButton5.setText(QCoreApplication.translate("MainWindow", u"\u2606  \u610f\u89c1\u5efa\u8bae[\u9700\u8981\u7f51\u7edc]       ", None))
        self.pushButton_re_login.setText(QCoreApplication.translate("MainWindow", u"\u2606  \u9000\u5230\u767b\u5f55", None))
        self.pushButton_6.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u9762\u677f", None))
    # retranslateUi

