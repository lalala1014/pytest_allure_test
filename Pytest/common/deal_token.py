import os
import sys

import pytest
import yaml
import json
from get_log import get_log
from run_method import runMethod
import requests

# logger = get_log()


#
# curPath = os.path.abspath(os.path.dirname(__file__))  # 返回绝对路径
# rootPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + ".")
# sys.path.append(rootPath)


def write_token(res):
    curPath = os.path.abspath(os.path.dirname(__file__))
    yamlPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "config/access_token.yml")
    tokenValue = {
        'access_token': res["data"]
    }
    with open(yamlPath, 'w', encoding='utf-8') as f:
        yaml.dump(tokenValue, f)    # 将python 数据类型转换为yaml数据类型
    print(tokenValue)
    # logger.info("\n token值已保存至配置文件中")


def read_token():
    curPath = os.path.abspath(os.path.dirname(__file__))
    path = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "config/access_token.yml")
    # path = os.path.dirname(os.path.abspath('.'))+'/data/access_token.yml'
    file = open(path)
    read = file.read()
    load = yaml.load(read, Loader=yaml.FullLoader)
    file.close()
    return load['access_token']


# @pytest.fixture(scope='function', autouse=True)
def login_token():
    url = ''
    headers = {
        "Content-Type": "application/json"
    }
    data = {
         "account": "",
         "password": ""
    }
    res = runMethod()
    r = json.loads(res.run_main("post", url, headers, data))
    print(r)
    return '=' + r['data']


if __name__ == "__main__":
    a = login_token()
    print(a)
    # run = runMethod()
    # url = "http://aly-test.api.xiaoyuanhao.com/nbugs-auth-center-test/xyhauth/getXyhUser"
    # data = {
    #
    #     "schoolId":"440101-S000011"
    # }
    # headers = {
    #     "Content-Type": "application/json",
    #     "Cookie": read_token()
    # }
    # # token = read_token()
    # res = run.run_main("get", url, headers, data)
    # print(res.content)
    # response = json.loads(res.text)
    # write_token(response)
