from flask import Flask, render_template, url_for

import categories

app = Flask('web-practice')


@app.route('/')
@app.route('/home/<user>')
def index(user='world'):
    return render_template('home.html', user=user)


@app.route('/shop')
@app.route('/shop/<category>')
def shop_page(category = None):
    shop_data = categories.data
    brands = None
    if category:
        for item in shop_data:
            if item['category'] == category:
                brands = item['brands']

    return render_template('shop_page.html', shop_data=shop_data, brands=brands)



def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
