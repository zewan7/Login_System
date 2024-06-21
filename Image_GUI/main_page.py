from PySide6.QtWidgets import QWidget
from PySide6_Login_System.Image_GUI.UI.Ui_mainwindow import Ui_Form as ui_mainwindow
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtCore import QUrl, QSize, QThread, Signal
from PySide6.QtGui import QPixmap, QImage
import requests

image_url = "https://img.8845.top/random.php"

class MyMainpage(QWidget):

    def __init__(self, parent=None, user_inof=dict):
        super().__init__()
        self.parent = parent
        self.user_inof = user_inof
        self.mainwindow = ui_mainwindow()
        self.mainwindow.setupUi(self)
        self.setMinimumSize(QSize(560, 490))
        self.setMaximumSize(QSize(560, 490))

        # 返回登陆
        self.mainwindow.pushButton_re_login.clicked.connect(self.re_login)

        self.mainwindow.pushButton_random.clicked.connect(self.random_image)
        self.random_image()

    def random_image(self):
        self.getimage = GetImage()
        self.getimage.signal_image.connect(self.network_access)
        self.getimage.start()

    def network_access(self, url):
        # 使用QNetworkAccessManager来请求图片
        self.manager = QNetworkAccessManager(self)
        self.reply = self.manager.get(QNetworkRequest(QUrl(url)))
        self.reply.finished.connect(self.on_image_ready)
        self.show()
        

    def on_image_ready(self):
        # 图片请求完成后，将图片数据转换为QPixmap并设置到QLabel上
        bytes = self.reply.readAll()
        image = QImage.fromData(bytes)
        pixmap = QPixmap.fromImage(image)
        self.mainwindow.label.setPixmap(pixmap)
        self.mainwindow.label.setScaledContents(True)


    def re_login(self):
        self.close()
        self.parent.show()



class GetImage(QThread):

    signal_image = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        result = self.get_image(image_url)
        if result:
            self.signal_image.emit(result)

    def get_image(self, image_url):
        res = requests.get(image_url).json()
        if res["Image_status"] == "ok":
            print(f'URL获取成功, 延迟：{res["delay"]}, url:{res["image_links"]}')
            return res["image_links"]
        else:
            print("获取失败")
            return ""


