import sqlite3


con = sqlite3.connect('todo.db')
my_cursor = con.cursor()
# my_cursor.execute("SELECT * FROM tasks")
# results = my_cursor.fetchall()
# for result in results:
#     print(results)
my_cursor.execute('INSERT INTO tasks(id,title, done) VALUES(10,"play basketball",0)')
con.commit()
my_cursor.execute('UPDATE tasks SET description = "play with my friends" WHERE id = 10')
con.commit()
my_cursor.execute('DELETE FROM tasks WHERE title = "sleep"')
con.commit()