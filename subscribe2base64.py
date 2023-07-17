import base64


def config2base64(path):
    # 读取文件
    with open('/data/config.txt', 'rb') as f:
        data = f.read()

    # 转换为base64
    data = base64.b64encode(data)

    return data
