from flask import Flask

app = Flask('web-practice')


@app.route('/')
def index():
    return 'Hello world'


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
