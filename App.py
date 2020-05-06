from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/execute')
def execute():
    return render_template('execute.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1",port="5000",debug=True)
