from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = ['Desayunar', 'Amorzar', 'Cenar']

@app.route('/')
def home():
    return render_template('index.html', titulo='ToDo', tasks = tasks)

@app.route('/add', methods = ['POST'])
def add_tasks():
    task_content = request.form['task']
    if task_content:
        tasks.append(task_content)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


