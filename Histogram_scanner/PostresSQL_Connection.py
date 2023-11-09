import psycopg2
conn = None
cur = None

try:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    conn = psycopg2.connect(host="localhost",database="suppliers",user="postgres",password="12345")
    cur = conn.cursor()

    create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                            id      int PRIMARY KEY,
                            name    varchar(40) NOT NULL,
                            salary  int,
                            dept_id varchar(30))'''
    cur.execute(create_script)
    insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
    insert_value = (1, 'Jame', 12000, 'D1')
    cur.execute(insert_script, insert_value)

    conn.commit() #Yukarıdaki işlemi kaydeder


except Exception as error:
    print(error)

finally:
    cur.close()
    conn.close()