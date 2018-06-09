from flask import Flask, render_template, request
import json
from data import NavModel

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/baidu')
def baidu():
    return render_template('baidu.html')

@app.route('/index')
def nav_html():
    conn = NavModel.NavModel()
    nav_data = conn.select_all()
    return render_template('nav.html', nav=nav_data)

@app.route('/nav', methods=['GET', 'POST'])
def nav():
    conn = NavModel.NavModel()
    res = ''
    res_data = {
        'success': 0,
        'data': ''
    }

    if request.method == 'GET':
        result = conn.select_all()
        res_data['data'] = result

    elif request.method == 'POST':
        Obj = json.loads(request.get_data())
        conn.insert_item(Obj['item'])
        
    res = app.make_response(json.dumps(res_data))
    res.headers['Access-Control-Allow-Origin'] = '*'

    conn.close()
    
    return res



if __name__ == '__main__':
    app.run(debug=True)
