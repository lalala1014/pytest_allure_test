import json
import pytest
import os
from Pytest.common import get_yaml
from Pytest.common import run_method
from Pytest.common.deal_token import login_token


class AllApi(object):
    def __init__(self):
        self.run = run_method.runMethod()

    def send_request(self, api_name):
        try:
            # 获取接口请求参数
            result = get_yaml.get_yaml(api_name)
            method = result["method"]
            url = result["url"]
            data = result["data"]
            headers = result["headers"]
            headers['Cookie'] = login_token()
            response = self.run.run_main(method, url, headers, data)
            return response
        except Exception as e:
            print(e)

    # 获取预期结果，方便断言时直接使用
    def get_expect(self, api_name):
        # 获取配置文件中的预期结果
        expect = get_yaml.get_yaml(api_name)["expected"]["success"]
        return expect


if __name__ == '__main__':
    all_login = AllApi()
    all_login.send_request("getXyhUser")