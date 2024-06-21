import string
import random


def get_captcha():
    """
    随机验证码
    """
    source = string.digits * 4
    captcha = "".join(random.sample(source, 4))
    print("发送邮箱验证码:", captcha)
    return captcha
