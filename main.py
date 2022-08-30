from flask import Flask, render_template

app = Flask('web-practice')


@app.route('/')
@app.route('/home/<user>')
def index(user='roli'):
    return render_template('home.html', user=user)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
