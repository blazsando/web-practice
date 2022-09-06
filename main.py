from flask import Flask, render_template, url_for, request

import categories
from data import queries

app = Flask('web-practice')


@app.route('/')

def index():
    return render_template('index.html')


@app.route('/shop',methods=['GET','POST'])
@app.route('/shop/<sport>',methods=['GET','POST'])
def shop(sport=None):
    chosen_product = None
    if request.method == 'POST':
        brand = request.form.get('choose-brand')
        chosen_product = categories.products[brand]
        # print(chosen_product)
    brands = None
    shop_data = categories.data
    if sport:
        for category in shop_data:
            if category['name'] == sport:
                brands = category['brands']
    return render_template('shop.html', shop_data=shop_data, brands=brands, sport=sport, chosen_product=chosen_product)


@app.route('/shows',methods=['GET','POST'])
def shows():
    shows = queries.get_shows()
    return render_template('shows.html', shows=shows)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
