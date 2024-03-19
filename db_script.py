# db_script.py
import psycopg2

with psycopg2.connect(
    host="172.17.0.3",
    port="5432",  # the port on your host machine that will forward requests to 5432 in the container
    database="books",
    user="postgres",
    password="password") as conn:
    with conn.cursor() as cursor:
        cursor.execute("select * from Author")
        data = cursor.fetchall()
        for d in data:
            if d[0] > 40:
                first_name = d[1].split(" ")[0]
                print(first_name)
# Del
# Raychel
# Millicent
# Inglebert
# Gram
# Andie
# Sibylle
# Cornie
# Brandtr
# Roseline