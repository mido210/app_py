# 플라스크 모듈로 부터 Flask 클래스를 읽어온다 
from flask import Flask
app= Flask(__name__)

# 사용자가 웹브라우저로 요청하면 실행되는 함수 
# decorator로 주소를 지정 웹서버 주소 + 데코레이터 주소
# 127.0.0.1:5000/test1
@app.route("/test1")
def test1():
	return "Hello Flask"
@app.route("/request")
def request():
	return "요청을 접수했습니다"
# 플라스크앱(파이썬 서버)실행
# debug옵션은 코드가 변경되면 서버 재시작
app.run(debug=True)
