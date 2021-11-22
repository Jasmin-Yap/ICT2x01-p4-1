from flask import Flask, render_template, request
from controllers import *
import models.connection as conn_mod
import requests

app = Flask(__name__)
conn = conn_mod.Connection()


@app.route('/')
def connection():
    conn_details = {
        'ip': conn.get_ip(),
        'port': conn.get_port()
    }

    return render_template('connection.html', conn=conn_details)


@app.route('/connection', methods=['GET', 'POST'])
def connection2():
    if request.method == 'POST':
        address = "http://" + request.form['ipInput'] + ":" + request.form['portInput'] + "/"
        # address = "http://192.168.4.1/"
        testDat = {'Speed': 10, 'Distance': 5}
        requests.post(address, testDat)

        return render_template('dashboard.html')
    else:
        return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
