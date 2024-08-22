import psycopg2
# conn_params = {
#     'dbname': 'payment_details',
#     'user': 'postgres',
#     'password': 'lAtarUsDfykfJQyTPxMfKaZvBzRNbJrd',
#     'host': 'postgres.railway.internal',
#     'port': 'your_port'
# }
connection = psycopg2.connect("postgresql://postgres:lAtarUsDfykfJQyTPxMfKaZvBzRNbJrd@junction.proxy.rlwy.net:26909/railway")

def response_insert(data):
    sql = "INSERT INTO payment_details(message) VALUES(%s)"
    # sql2 = "SELECT * FROM payment_details"
    values = (data,)
    cursor = connection.cursor()
    try:
        cursor.execute(sql,values)
        connection.commit()
        # print("done")
        return 1
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()

        
def get_access_token():
    sql = "SELECT * FROM access_tokens ORDER BY created_at DESC LIMIT 1"
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        # print(result[0][1])
        return result[0][1]
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()

get_access_token()