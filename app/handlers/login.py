from PySide6.QtCore import Signal, QTimer, QSettings, QUrl
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from ..UI_all.Ui_zh import Ui_widget as ui_loging
from ..models.create_tables import session, UserTable
from ..utls.api_hash import PasswordHasher
from threading import Thread
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config import IMGS_TIME

hash_pwd = PasswordHasher()
script_dir = os.path.dirname(os.path.abspath(__file__))
IMGS_PATH = os.path.join(script_dir, "", "..", "images")


class LoginHander(QWidget):
    login_signal = Signal(str)
    longin_ok = Signal(bool, dict)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.settings = QSettings("MyApp", "LoginApp")
        self.login_ui = ui_loging()
        self.login_ui.setupUi(self)
        self.login_ui.label_img.setPixmap(QPixmap(f"{IMGS_PATH}/16pic_8707727_b.jpg"))
        self.login_func()
        self.login_signal.connect(self.on_login_result)
        self.current_img_index = 0
        try:
            self.imgs_list = os.listdir(IMGS_PATH)
        except FileNotFoundError:
            print("图片列表未配置")
            self.imgs_list = []

        self.update_button_timer = QTimer(self)
        self.update_button_timer.timeout.connect(self.imgs)

        self.update_button_timer.start(IMGS_TIME)

        # 初始化视频播放
        self.video_widget = QVideoWidget(self)
        self.video_widget.hide()
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)

        # 记住我和自动登陆
        self.load_settings()

    def load_settings(self):
        # 记住我
        if self.settings.value("remember_me", type=bool):
            self.login_ui.lineEdit_account.setText(self.settings.value("email", ""))
            self.login_ui.checkBox_remember.setChecked(True)
        # 自动登陆
        if self.settings.value("auto_login", type=bool):
            self.login_ui.lineEdit_account.setText(self.settings.value("email", ""))
            self.login_ui.lineEdit_password.setText(self.settings.value("password", ""))
            self.login_ui.checkBox_aoto_login.setChecked(True)
            self.login()

    # 更新登陆界面的图片
    def imgs(self):
        # 未配置图片列表时
        if not self.imgs_list:
            self.update_button_timer.stop()
            return

        # 配置了图片
        self.current_img_index = (self.current_img_index + 1) % len(self.imgs_list)
        img_path = os.path.join(IMGS_PATH, self.imgs_list[self.current_img_index])
        img_end = img_path.rsplit('.', maxsplit=1)[-1]
        if not self.login_ui.label_img.isVisible():
            self.login_ui.label_img.show()

        # 动态图和视频
        if img_end.lower() in ["gif", "mng"]:
            self.movie = QMovie(img_path)
            self.login_ui.label_img.setMovie(self.movie)
            self.login_ui.label_img.setScaledContents(True)
            self.movie.start()

        # 视频显示
        elif img_end.lower() in ["mp4", "wmv", "avi"]:
            # 隐藏label_img标签
            self.login_ui.label_img.hide()

            # 替换成视频播放
            self.login_ui.verticalLayout_2.insertWidget(0, self.video_widget)
            self.video_widget.show()
            video_url = QUrl.fromLocalFile(img_path)
            self.media_player.setSource(video_url)
            self.media_player.play()

        # 图片显示
        else:
            try:
                pixmap = QPixmap(img_path)
                if not pixmap.isNull():
                    self.login_ui.label_img.setPixmap(pixmap)
                    self.login_ui.label_img.setScaledContents(True)
            except Exception:
                pass

    def on_login_result(self, message):
        QMessageBox.warning(self, 'Error', message)

    def login_func(self):
        # 登陆
        self.login_ui.pushButton_login.clicked.connect(self.login)
        # 注册按钮切换页面  
        self.login_ui.pushButton_register.clicked.connect(self.goto_register)
        # 忘记密码
        self.login_ui.pushButton_fpwd.clicked.connect(self.goto_repwd)

    def login(self):
        def thread_login():
            email = self.login_ui.lineEdit_account.text()
            pwd = self.login_ui.lineEdit_password.text()
            if not email or not pwd:
                self.login_signal.emit("请输入用户名或密码")
                return
            user = session.query(UserTable).filter_by(email=email).first()
            if user:
                db_pwd = user.password
                check_password = hash_pwd.verify_password(pwd, db_pwd)
                if check_password:
                    # 保存账号和密码
                    self.settings.setValue("email", email)
                    self.settings.setValue("password", pwd)
                    # 记住我
                    self.settings.setValue("remember_me", self.login_ui.checkBox_remember.isChecked())
                    # 自动登陆
                    self.settings.setValue("auto_login", self.login_ui.checkBox_aoto_login.isChecked())
                    user_info = {
                        "user_id": user.id,
                        "user_name": user.name,
                        "user_email": user.email,
                        "user_create_time": user.create_time,
                        "user_update_time": user.update_time
                    }
                    self.longin_ok.emit(True, user_info)

                else:
                    self.login_signal.emit("用户名或密码不正确")
            else:
                self.login_signal.emit("该邮箱未注册")

        thread = Thread(target=thread_login)
        thread.start()

    def goto_register(self):
        self.parent.stacked_layout.setCurrentIndex(1)
        self.parent.setWindowTitle("注册")

    def goto_repwd(self):
        self.parent.stacked_layout.setCurrentIndex(2)
        self.parent.setWindowTitle("重置密码")
