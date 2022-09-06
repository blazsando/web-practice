from flask import Flask, render_template, request
import categories

app = Flask('web-practice')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shop/<category>', methods=['POST', 'GET'])
@app.route('/shop')
def shop(category=None):
    products = None
    if request.method == 'POST':
        brand= request.form.get('brand')
        products = categories.products[brand]
    brands = None
    sports = categories.data
    if category:
        for sport in sports:
            if category == sport['category']:
                brands = sport['brands']
    return render_template('shop.html', categories=sports, brands=brands, products=products)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
