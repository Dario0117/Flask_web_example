from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/list')
def lst():
    return render_template('list.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug= True, port=80)