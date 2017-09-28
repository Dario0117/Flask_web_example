from flask import Flask, render_template
from back.Student import Student

app = Flask(__name__)
students = []

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/list')
def lst():
    return render_template('list.html', students=students)

@app.route('/search')
def search():
    return render_template('search.html', students=students)

@app.route('/add')
def add():
    return render_template('add.html', students=students)

@app.route('/edit')
def edit():
    return render_template('edit.html', students=students)

@app.route('/delete')
def delete():
    return render_template('delete.html', students=students)


if __name__ == '__main__':
    students.append(Student("Esteban 1", "Barboza 1", 22, "e@mail.com"))
    students.append(Student("Esteban 2", "Barboza 2", 22, "e@mail.com"))
    students.append(Student("Esteban 3", "Barboza 3", 22, "e@mail.com"))
    students.append(Student("Esteban 4", "Barboza 4", 22, "e@mail.com"))
    students.append(Student("Esteban 5", "Barboza 5", 22, "e@mail.com"))
    app.run(debug= True, port=80)