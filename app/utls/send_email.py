from config import config
import yagmail


def send_email_captcha(email, captcha):
    """
    发送验证码到邮箱
    """
    try:
        subject = '您的验证码'
        contents = f'您好，您的验证码是：{captcha}。有效时间5分钟。'
        yag = yagmail.SMTP(**config["email"])
        yag.send(email, subject, contents)
        yag.close()
        return True
    except Exception as e:
        print(f"验证码发送error:{e}")
        return False
