import sys
sys.path.append(r"C:\Users\Administrator\PycharmProjects\ImoocAPI")
import logging.config
import logging


# 读取日志配置文件
def get_log():
    con_log = "../config/log.conf"
    logging.config.fileConfig(con_log)  # 从一个.conf 格式文件中读取日志记录配置
    log = logging.getLogger()
    return log