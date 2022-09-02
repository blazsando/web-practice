from flask import Flask, render_template
import categories

app = Flask('web-practice')


@app.route('/')
@app.route('/<user>')
def index(user='world'):
    return render_template('home.html', user=user)

@app.route('/shop')
def shop():
    categories_data = categories.data
    return render_template('shop.html', categories=categories_data)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
