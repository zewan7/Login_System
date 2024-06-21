import redis

# 登陆界面图片更换时间间隔(ms)
IMGS_TIME = 5000

config = {
    "db_params": {    # mysql数据库配置
        "user": "root",
        "port": 3306,
        "host": "47.xxx.xxx.xxx",
        "password": "xxxxxx",
        "db": "xxx",
    },

    "redis": {      # redis
        "host": '47.xxx.xxx.xxx',
        "port": 6379,
        "password": 'xxxxxx',
        "db": 1,
        "decode_responses": True
    },

    "email": {
        "host": "smtp.qq.com",  # QQ邮箱，其他邮箱自行更换
        "smtp_ssl": True,
        "port": 465,
        "user": "xxxxxx@qq.com",# 替换你的邮箱
        "password": "xxxxxx" # 替换你的邮箱授权码
    },
}

config["redis_url"] = "redis://:{password}@{host}:{port}/1".format(**config["redis"])
config["db_url"] = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(**config["db_params"])

redis_conn = redis.Redis(**config["redis"])
