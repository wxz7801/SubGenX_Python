from flask import Flask, Response
import base64

app = Flask(__name__)


@app.route('/api/<uuid>', methods=['GET'])
def get_base64(uuid):
    try:
        # 根据UUID读取文件
        with open(f'./data/config.txt', 'r') as f:
            data = f.read()

        # 替换默认的UUID
        default_uuid = '620436f3-3104-48c4-a41d-3d19e72b9605'
        data = data.replace(default_uuid, uuid)

        # 转换为base64
        encoded_data = base64.b64encode(data.encode()).decode()

        # 返回base64编码的数据
        return Response(encoded_data, mimetype='text/plain')

    except FileNotFoundError:
        return Response('404 not found.', status=404)

    except Exception as e:
        return Response(f"An error occurred.", status=500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
