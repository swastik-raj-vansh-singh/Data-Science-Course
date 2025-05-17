import sqlite3
connection = sqlite3.connect('example.db')
connection

currsor = connection.cursor()

# # creating a table
# currsor.execute('''

#     create table student(
#         id integer Primary key,
#         name varchar not null,
#         age int                        
#     )             
# ''')

# connection.commit()


# INSERTING INTO TABLE
# currsor.execute('''
#     insert into student (id,name, age) values (1,"swastik",22)
    
# ''')

# currsor.execute('''
#     insert into student (id,name, age) values (4,"lovely",55)
    
# ''')
# currsor.execute('''
#     insert into student (id,name, age) values (2,"shruti",26)
    
# ''')

# currsor.execute('''
#     insert into student (id,name, age) values (3,"surinder",60)
    
# ''')

# connection.commit()


currsor.execute('select * from student')
rows = currsor.fetchall()

for i in rows:
    print(i)