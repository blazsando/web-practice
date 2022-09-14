from flask import Flask, render_template, jsonify, request
from data import queries
app = Flask('web-practice')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/display_actors')
def actors():
    actors_data = queries.actors_in_more_than_three_shows()
    return render_template('actors.html', actors_data=actors_data)


@app.route('/get_played_characters')
def get_played_characters():
    # current_actor_id = int(request.args.get('current_actor'))
    current_actor_id = (request.args.get('current_actor'))
    characters = queries.get_played_characters(current_actor_id)
    print(current_actor_id)
    return jsonify(characters)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
