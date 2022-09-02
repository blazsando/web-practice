from flask import Flask, render_template, url_for

import categories

app = Flask('web-practice')


@app.route('/')

def index():
    return render_template('index.html')


@app.route('/shop')
@app.route('/shop/<sport>')
def shop(sport=None):
    brands = None
    shop_data = categories.data
    if sport:
        for category in shop_data:
            if category['name'] == sport:
                brands = category['brands']
    return render_template('shop.html', shop_data=shop_data, brands=brands)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
