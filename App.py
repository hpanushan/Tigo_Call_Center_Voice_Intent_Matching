from flask import Flask, render_template, url_for, request

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

@app.route('/new_submit', methods=['POST'])
def new_submit():
    intent_name = request.form['intentname']
    keywords = request.form['keywords']

    # Convert the keywords string into a list of keywords
    keywords = keywords.split(',')
    print(intent_name,keywords)

    return render_template('new.html')

@app.route('/update_submit', methods=['POST'])
def update_submit():
    intent_name = request.form['intentname']
    keywords = request.form['keywords']
    
    # Convert the keywords string into a list of keywords
    keywords = keywords.split(',')
    print(intent_name,keywords)

    return render_template('update.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1",port="5000",debug=True)
