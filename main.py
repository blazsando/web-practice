from flask import Flask, render_template

import categories

app = Flask('web-practice')


@app.route('/')

def index():
    return render_template('index.html')

@app.route('/shop')
def shop():
    shop_data = categories.data
    return render_template('shop.html', shop_data=shop_data)
def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
