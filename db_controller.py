import pymysql


class DatabaseController:
    @staticmethod
    def get_grades():
        connection = pymysql.connect(host='95.163.233.154',
                                     port=3310,
                                     user='kirill.b',
                                     passwd='userkirill2023',
                                     db='kirill_batalov')
        with connection:
            cursor = connection.cursor()
            query = 'select * from grade ' +\
                    'order by grade_value, grade_name'
            cursor.execute(query)
            rows = cursor.fetchall()
        return dict((f'{row[1]}-{row[2]}', row[0]) for row in rows)


print(DatabaseController.get_grades())
