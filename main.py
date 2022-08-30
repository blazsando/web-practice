from flask import Flask, render_template
import categories
# data = data.shop


app = Flask('web-practice')


@app.route('/')
@app.route('/<user>')
def index(user='world'):
    return render_template('home.html', user=user)


@app.route('/shop')
@app.route('/shop/<category>')
def shop(category=None):
    shop_data = categories.data
    brands = None
    if category:
        for item in shop_data:
            if item['category'] == category:
                brands = item['brands']
    return render_template('shop.html', shop_datas=shop_data, category=category, brands=brands)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
