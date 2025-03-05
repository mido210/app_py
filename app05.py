# 웹서버 : 정적인 파일을 응답
# WAS : 파이썬을 실행해서 동적으로 만들어서 응답

# 숫자 입력 화면 

# 제곱한 결과를 출력
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/start")
def start():
	return render_template('start.html')

# 제곱한 결과를 출력
@app.route("/end")
def end():
	value=request.args.get("value")
	return render_template("end.html",result=value)


app.run(debug=True)