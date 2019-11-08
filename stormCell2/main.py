import os
import clock
import threading
from flask import jsonify

from flask import Flask, send_from_directory
app = Flask(__name__, static_folder='static')
the_clock = clock.Clock()


@app.route("/time")
def time():
    return jsonify(the_clock.cur_game_time_dic)


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
    the_clock.start()
    threading.Thread(target=app.run).start()
    # app.run()

