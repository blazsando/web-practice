from flask import Flask, render_template

import categories

app = Flask('web-practice')


@app.route('/')
@app.route('/home/<user>')
def index(user = 'lacimaci'):
    return render_template('home.html', user=user)

@app.route('/shop')
@app.route('/shop/<category>')
def shop(category = None):
    shop_data = categories.data
    brands = None
    if category:
        for item in shop_data:
           if item['category'] == category:
               brands = item['brands']
    return render_template('shop.html', shop_categories=shop_data, brands=brands)
def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
