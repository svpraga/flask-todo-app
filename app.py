from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list (we'll upgrade to a DB later)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({'id': len(tasks)+1, 'text': task, 'done': False})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

