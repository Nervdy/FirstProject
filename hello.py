from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/baidu')
def baidu():
    return render_template('baidu.html')

if __name__ == '__main__':
    app.run(debug=True)
