from app import mysql

def read_all_tasks_in_db():
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM task")
   return cur.fetchall()

def read_task_in_db(id):
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM task WHERE id = " + id)
   return cur.fetchone()

def create_task_in_db(title, dt):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO task (task, date_created) VALUES ('" + str(title) + "','" + str(dt) + "')")
    mysql.connection.commit()
    return {'title': title}

def update_task_in_db(title, id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE task SET task = '" + str(title) + "' WHERE id = " + id)
    mysql.connection.commit()
    return {'title': title}

def delete_task_in_db(id):
   cur = mysql.connection.cursor()
   response = cur.execute("DELETE FROM task WHERE id = " + id)
   mysql.connection.commit()
   if response > 0:
       return {'message': 'record deleted'}
   else: 
       return {'message': 'no record found'}
