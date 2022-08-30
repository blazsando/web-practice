from flask import Flask, render_template, url_for

import categories

app = Flask('web-practice')


@app.route('/')
@app.route('/home/<user>')
def index(user='world'):
    return render_template('home.html', user=user)


@app.route('/shop')
def shop_page():
    shop_data = categories.data
    return render_template('shop_page.html', shop_data=shop_data)

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
