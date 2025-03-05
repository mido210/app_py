from flask import Flask, request

app = Flask(__name__)
# 루트 패이지
@app.route("/")
def index():
	return "<html><body><p>Hello <b>Flask</b></p></body></html>"
# 사용자가 127.0.0.1:5000/test1?username=spring으로 요청을 보내면 
# spring이라는 username을 꺼내서 출력
@app.route("/test1")
def test1():
	username =request.args.get('username')
	return username

# 127.0.0.1:5000/test2?value=11
@app.route("/test2")
def test2():
	value = request.args.get("value")
	return value+value
app.run(debug=True)