from datetime import datetime
from flask import Blueprint, request, render_template, redirect
import app.controllers.task_db_service as db

task_api = Blueprint('task_api', __name__)

@task_api.route('/api/tasks', methods=['GET','POST']) # GET ALL
def get_all_tasks():
    rv = db.read_all_tasks_in_db()
    return render_template('tasks.html', tasks=rv)

@task_api.route('/api/tasks/update/<id>', methods=['POST']) # GET ONE
def get_task(id):
    result = db.read_task_in_db(id)
    return render_template('task_update.html', task=result) 

@task_api.route('/api/tasks/create', methods=['POST']) # CREATE
def post_task():
    content = request.form['content']
    dt = datetime.utcnow()
    db.create_task_in_db(content, dt)
    return redirect('/api/tasks')
    #rv = db.read_all_tasks_in_db()
    #return render_template('tasks.html', tasks=rv)

@task_api.route('/api/tasks/update/submit/<id>', methods=['POST']) # PUT
def put_task(id):
    content = request.form['content']
    db.update_task_in_db(content, id)
    return redirect('/api/tasks')

@task_api.route('/api/tasks/delete/<id>', methods=['POST']) # DELETE
def delete_task(id):
    db.delete_task_in_db(id)
    return redirect('/api/tasks')
