from flask import Flask, render_template
import categories

app = Flask('web-practice')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shop/<category>')
@app.route('/shop')
def shop(category=None):
    sports = categories.data
    return render_template('shop.html', categories=sports)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
