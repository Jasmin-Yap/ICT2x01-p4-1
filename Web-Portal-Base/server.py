from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/maze')
def maze():
    return render_template('maze.html')

@app.route('/ref')
def extra():
    return render_template('extra.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 