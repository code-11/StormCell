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

main_player = player.Player("Brendan")

the_game = game.Game()
the_game.add_player(main_player)


@app.route("/pauseTime")
def pause_time():
    global the_game
    new_clock = the_game.game_clock.clone()
    the_game.game_clock.stop()
    the_game.game_clock = new_clock
    return jsonify(True)


@app.route("/startTime")
def start_time():
    global the_game
    the_game.game_clock.start()
    return jsonify(True)


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
    prop_reader = PR.PropertyReader()
    countries_io = countriesIO.CountriesIO(prop_reader)
    continent_io = continentIO.ContinentIO(prop_reader)

    countries = countries.Countries()

    countries_io.init_properties()
    continent_io.init_properties()

    countries_io.load()
    continent_io.load()

    countries.construct_countries(countries_io.get_country_name_list(), continent_io.data)

    # threading.Thread(target=app.run).start()


