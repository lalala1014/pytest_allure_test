import yaml


def get_yaml(apiname):
    with open("../config/api_config.yml", encoding="utf-8") as fs:
        content = fs.read()
        contents = yaml.load(content, Loader=yaml.FullLoader)[apiname]
        method = contents["method"]
        url = yaml.load(content, Loader=yaml.FullLoader)["host"] + contents["url"]
        data = contents["data"]
        headers = contents["headers"]
        expected = contents["expected"]
        result = {"method": method, "url": url, "data": data, "headers": headers, "expected": expected}
    return result
