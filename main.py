from flask import Flask, render_template

import categories

app = Flask('web-practice')


@app.route('/')
@app.route('/home/<user>')
def index(user = 'lacimaci'):
    return render_template('home.html', user=user)

@app.route('/shop')
def shop():
    shop_categories = categories.data
    return render_template('shop.html', shop_categories=shop_categories)
def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
