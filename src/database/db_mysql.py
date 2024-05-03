import pymysql

def get_connection():
    try:
        return pymysql.connect(
            host='localhost',
            database='castro_db',
            user='root',
            password=''
        )
    except Exception as ex:
        print(ex)