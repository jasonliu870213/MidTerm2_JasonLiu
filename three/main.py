import pymysql.cursors
db_settings = {
    "host": "54.201.140.239",
    "port": 3306,
    "user": "midterm",
    "password": "midtermBatch#1",
    "db": "midterm",
    "charset": "utf8",
    "autocommit": "True",
}

conn = pymysql.connect(**db_settings)  # connect to database
with conn.cursor(pymysql.cursors.DictCursor) as cursor:
    try:
        code = "select patient_id, first_name, last_name, gender, height,weight " \
               "from patient inner join district on patient.post_code = district.post_code where district = 'Xinyi';"
        cursor.execute(code)
        result = cursor.fetchall()
        print(result)
        for i in result:
            print(f'{i["first_name"]} {i["last_name"]} (No.{i["patient_id"]}), '
                  f'{i["gender"]}, Height: {i["height"]} cm, Weight: {i["weight"]} kg')
    except Exception as e:
        print(e)