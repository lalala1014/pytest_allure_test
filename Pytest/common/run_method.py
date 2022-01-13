import requests


class runMethod(object):
    def post_main(self, url, headers, data):
        response = requests.post(url=url, headers=headers, json=data)    # verify用来验证网站的ca证书，为false时为不验证
        return response.text

    def get_main(self, url, headers, data):
        response = requests.get(url=url, headers=headers, params=data)
        return response.text

    def run_main(self, method, url, headers, data):
        if method == 'get':
            res = self.get_main(url, headers, data)
        elif method == 'post':
            res = self.post_main(url, headers, data)
        return res
