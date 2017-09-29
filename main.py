from flask import Flask, render_template, request
from back.Student import Student

app = Flask(__name__)
students = []

@app.route('/')
def index():
    return render_template('home.html', students=students, home=True)

@app.route('/add')
def add():
    return render_template('add.html', students=students)

@app.route('/edit/<int:id>')
def edit(id):
    student = [x for x in students if x.id == id]
    if len(student) == 0: return render_template('list.html', students=students)
    return render_template('edit.html', student=student[0])

@app.route('/delete/<int:id>')
def delete(id):
    student = [x for x in students if x.id == id]
    students.remove(student[0])
    return "x"

@app.route('/search/', methods=['GET'])
def search():
    name = request.args.get('name')
    students_filt = [x for x in students if name in x.name.lower() or name.lower() in x.lastname.lower()]
    return render_template('home.html', students=students_filt, home=True)

if __name__ == '__main__':
    students.append(Student("steban 1", "Barboza 1", 22, "e@mail.com"))
    students.append(Student("Esteban 2", "Barboza 2", 22, "e@mail.com"))
    students.append(Student("Esteban 3", "Barboza 3", 22, "e@mail.com"))
    students.append(Student("Esteban 4", "Barboza 4", 22, "e@mail.com"))
    students.append(Student("Esteban 5", "Barboza 5", 22, "e@mail.com"))
    app.run(debug= True, port=80)