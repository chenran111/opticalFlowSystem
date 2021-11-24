from flask import Flask


application = Flask(__name__)

@application.route('/demo')
def test():
    return '无穷鸡蛋'

application.run(debug=True)
