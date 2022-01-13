import subprocess
from Pytest.api import app_api
import pytest
import json
import os

class TestLogin(object):
    @pytest.fixture(scope="class")
    def init_login(self):
        print("开始执行用例")
        all_login = app_api.AllApi()
        return all_login

    # @allure.story("测试test_login")
    @pytest.mark.parametrize("api_name", ["getXyhUser"])
    def test_login(self, api_name, init_login):
        res = json.loads(init_login.send_request(api_name))
        excepted = init_login.get_expect(api_name)
        # 断言1：success的值为True
        assert res['success'] == excepted, "success的值为: %s" % res['success']
        # 断言2：access_token的值为不为空
        assert res['data'] is not None, 'data的值为：%s' % res['data']



if __name__ == "__main__":
    # pytest.main(['-s', '-q', './test_login.py', '--alluredir', '../report/xml'])
    # os.system("allure generate ../report/xml -o ../report/html ")
    pytest.main(["-sq", "--alluredir", "./allure-results"])
    os.system("allure generate ./allure-results/ -o ./allure-report/ --clean")

