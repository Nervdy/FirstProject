from flask import Flask, render_template

app = Flask(__name__)

# for 遍历字典


# @app.route('/')
# def index():
#     user = {
#         'username': u'黄宙',
#         'age': 18
#     }
#     websites = ['baidu.com','googe.com']
#     return render_template('index.html', user=user , websites=websites)
@app.route('/')
def index():
    books = [
        {
            'name': u'西游记',
            'author': u'吴承恩',
            'price': 109
        },
        {
            'name': u'红楼梦',
            'author': u'曹雪芹',
            'price': 110
        },
        {
            'name': u'三国演义',
            'author': u'罗贯中',
            'price': 111
        },
        {
            'name': u'水浒传',
            'author': u'施耐庵',
            'price': 130
        }
    ]
    return render_template('index.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)
