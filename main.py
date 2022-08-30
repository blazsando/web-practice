from flask import Flask, render_template
import categories
# data = data.shop


app = Flask('web-practice')


@app.route('/')
@app.route('/<user>')
def index(user='world'):
    return render_template('home.html', user=user)


@app.route('/shop')
def shop():
    shop_data = categories.data
    return render_template('shop.html', shop_datas=shop_data)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
