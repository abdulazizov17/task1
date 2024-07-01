import psycopg2
conn = psycopg2.connect(database = 'n48',
                        user = 'posgres',
                        host = 'localhost',
                        password = 'qazwsx',
                        port = 5432
                        )
cursor = conn.cursor()
select_all_employes_query = '''
select * from employe;
'''
cursor.execute(select_all_employes_query)
rows = cursor.fetchall()
for employe in rows:
    print(employe)