# 숫자 2개를 입력받아 덧셈을 해서 출력
from flask import Flask, render_template, request
app= Flask(__name__)

@app.route("/start")
def start():
	return render_template("start2.html")

@app.route("/end")
def end():
	value1 = int(request.args.get(value2))
	value2 = int(request.args.get(value1))
	result = value1 + value2
	return render_template("end2.html", result=result)

app.run(debug=True)