import pymysql


class DatabaseController:
    connection = pymysql.connect(host='95.163.233.154',
                                 port=3310,
                                 user='kirill.b',
                                 passwd='userkirill2023',
                                 db='kirill_batalov')
    @staticmethod
    def get_grades():
        with DatabaseController.connection as connection:
            cursor = connection.cursor()
            cursor.execute('select * from grade '
                           'order by grade_value, grade_name')
            rows = cursor.fetchall()
        return dict((f'{row[1]}-{row[2]}', row[0]) for row in rows)

    # TODO: Метод, определяющий, есть ли пользователь с данным id в БД, если есть, то возвращающий класс User,
    #       в противном случае None

    # TODO: Метод, добавляющий пользователя в БД (id, grade)


print(DatabaseController.get_grades())
