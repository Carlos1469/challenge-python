from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/igs')
def igs():
    kata="CODING IGS"
    data=[1,2,3,4]
    return render_template("igs.html",kata=kata,data=data)

if __name__ == "__main__":
    app.run(debug=True)