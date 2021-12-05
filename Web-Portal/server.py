from flask import Flask, render_template
from controllers import blockly_controller

app = Flask(__name__)

@app.route('/')
def connection():
    return render_template('dashboard.html')

@app.route('/blockly')
def blockly():
    return render_template('blockly.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
