from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('home.html'))
 
@app.route('/edit')
def edit():
    return(render_template('read.html'))

@app.route('/new')
def new():
    return(render_template('new.html'))

@app.route('/delete')
def delete():
    return(render_template('delete.html'))

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.213')