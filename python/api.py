from bottle import route, run
import json
@route('/staging/a')
def hello():
    return json.dumps({"message": "mail a"})


@route('/staging/b')
def hello():
    return json.dumps({"message": "mail b"})


run(host='0.0.0.0', port=5000)

