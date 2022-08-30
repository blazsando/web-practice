from flask import Flask, render_template

app = Flask('web-practice')


@app.route('/')
def index():
    return render_template('home.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
