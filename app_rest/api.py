from flask import Flask
import jsonsempai #json-sempai
import json
from flask_restful import reqparse, abort, Api, Resource
from app_blog.models import Workers, Dept, Post

app = Flask(__name__)
api = Api(app)





#TODOS = {
#    post_item[0].title:  {'task': post_item[0].body},
#    post_item[0].title:  {'task': post_item[1].body},
#    post_item[0].title:  {'task': post_item[2].body},
#}

post_item = Post.query.all()
TODOS = []
for number in range(3):
    TODOS.append(post_item[number].title)
    for number2 in range(3):
        TODOS[number] = [post_item[0].body,post_item[1].body,post_item[2].body]

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

#WorkList = {}
WorkersListQuery = Workers.query.all()


WorkersList = {a: {} for a in range(len(WorkersListQuery))}
for number in range(len(WorkersListQuery)):
    WorkersList[number] = {'id': WorkersListQuery[number].id, 'deptname' : WorkersListQuery[number].deptname, 'name': WorkersListQuery[number].fullname, 'salary' : WorkersListQuery[number].salary}


# WorkList
# return list workers
class Workers(Resource):
    def get(self):
        return WorkersList

dept_names={}
Dept_id = []
DeptListQ = Dept.query.all()

for i in range(len(DeptListQ)):
    dept_names[DeptListQ[i].id] = DeptListQ[i].name
    Dept_id.append(DeptListQ[i].id)


DeptList = {a: {} for a in dept_names.values()}

for id in Dept_id:
    for number in range(len(DeptListQ)):
        if id == int(WorkersListQuery[number].deptname):
            DeptList[dept_names[id]][WorkersListQuery[number].fullname] = {'id': WorkersListQuery[number].id, 'deptname' : dept_names[int(WorkersListQuery[number].deptname)], 'name': WorkersListQuery[number].fullname, 'salary' : WorkersListQuery[number].salary}



class Dept(Resource):
    def get(self):
        return DeptList


##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(Workers, '/workers')
api.add_resource(Dept, '/dept')


if __name__ == '__main__':
    app.run( debug = True)
    app.run( FLASK_DEBUG = True)
