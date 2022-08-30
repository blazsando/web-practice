from flask import Flask, render_template
import categories_data

app = Flask('web-practice')


@app.route('/')
@app.route('/home/<user>')
def index(user='roli'):
    return render_template('home.html', user=user)


@app.route('/shop')
def shop_page():
    data = categories_data.data
    return render_template('shop.html', data=data)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
