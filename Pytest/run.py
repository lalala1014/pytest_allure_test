import pytest
import os
# import testcase.test_login

if __name__ == "__main__":
    # pytest.main(['-s', '-q', './test_login.py', '--alluredir', '../report/xml'])
    # os.system("allure generate ../report/xml -o ../report/html ")
    # with open('')
    pytest.main(["-sq", "--alluredir", "./allure-results"])
    # pytest.main(['-s', '-q', '../test_login.py', '--alluredir', '../report/xml'])
    os.system("allure generate ./allure-results/ -o ./allure-report/ --clean")