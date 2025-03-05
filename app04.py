from flask import Flask, request

app = Flask(__name__)

# test1 주소로 value라는 숫자를 받아오시오(문자열)
# value*value 출력
@app.route("/test1")
def test1():
	value = int(request.args.get("value","10"))
	value = value*value
	return f"{value}"  # 리턴값이 숫자인 경우 타입에 신경써서 작업!(그냥 f문자열 사용!)
app.run(debug=True)