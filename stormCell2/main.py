import os
import game
import player
import threading
import countries
import countriesIO
import continentIO
import propertyReader as PR
from flask import jsonify

from flask import Flask, send_from_directory
app = Flask(__name__, static_folder='static')


def start_game():
    main_player = player.Player("Brendan")

    a_game = game.Game()
    a_game.add_player(main_player)
    return a_game


def load_data():
    prop_reader = PR.PropertyReader()
    countries_io = countriesIO.CountriesIO(prop_reader)
    continent_io = continentIO.ContinentIO(prop_reader)

    all_countries = countries.Countries()

    countries_io.init_properties()
    continent_io.init_properties()

    countries_io.load()
    continent_io.load()

    all_countries.construct_countries(countries_io.get_country_name_list(), continent_io.data)
    return countries_io.data


the_game = start_game()
shapes = load_data()


@app.route("/getCountryShapes")
def get_country_shapes():
    global shapes
    return jsonify(shapes)


@app.route("/pauseTime")
def pause_time():
    global the_game
    new_clock = the_game.game_clock.clone()
    the_game.game_clock.stop()
    the_game.game_clock = new_clock
    return jsonify({"response": True})


@app.route("/startTime")
def start_time():
    global the_game
    the_game.game_clock.start()
    return jsonify({"response": True})


@app.route("/time")
def time():
    return jsonify(the_game.game_clock.game_time_dic())

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


@app.route('/bundle.js')
def bundle():
    return app.send_static_file('./bundle.js')


@app.route('/')
def root():
    return app.send_static_file('./index.html')


if __name__ == '__main__':
    threading.Thread(target=app.run).start()


