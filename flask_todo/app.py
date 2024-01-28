from flask import Flask, jsonify, request

# Clasa părinte pentru gestionarea sarcinilor
class TaskManager:
    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks

    def add_task(self, task):
        self.tasks.append(task)

# Clasa pentru primul endpoint (afișare sarcini)
class TasksResource(TaskManager):
    def get(self):
        tasks = self.get_tasks()
        return jsonify({'tasks': tasks})

# Clasa pentru al doilea endpoint (adaugare sarcină)
class AddTaskResource(TaskManager):
    def post(self):
        data = request.get_json()
        task = data.get('task')

        if task:
            self.add_task(task)
            return jsonify({'message': 'Sarcină adăugată cu succes!'})
        else:
            return jsonify({'error': 'Câmpul "task" nu poate fi gol!'}), 400

app = Flask(__name__)

# Adăugarea endpoint-urilor la aplicație
app.add_url_rule('/tasks', view_func=TasksResource.as_view('tasks'))
app.add_url_rule('/add_task', view_func=AddTaskResource.as_view('add_task'))

if __name__ == '__main__':
    app.run(debug=True)
