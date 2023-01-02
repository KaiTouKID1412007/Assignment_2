from flask import Flask

#1.实例化flask应用对象
app = Flask(__name__)

#编写视图和路由
from flask import make_response,jsonify

@app.route(rule="/user",methods=["get","post"])
def user():
    #显示图片
    with open("2.jpg","rb") as f:
        content =f.read()
        response=make_response(content)
        response.headers["Content-Type"]="image/jpeg"
    return response

if __name__ =='__main__':
    #app.run(debug=True,host="0.0.0.0",port=8999)
    app.run(debug=True)