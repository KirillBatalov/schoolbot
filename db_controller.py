import pymysql


class DatabaseController:
    connection = dict(host='95.163.233.154',
                         port=3310,
                         user='kirill.b',
                         passwd='userkirill2023',
                         db='kirill_batalov')
    @staticmethod
    def get_grades():
        with pymysql.connect(**DatabaseController.connection) as connection:
            cursor = connection.cursor()
            cursor.execute('select * from grade '
                           'order by grade_value, grade_name')
            rows = cursor.fetchall()
        return dict((f'{row[1]}-{row[2]}', row[0]) for row in rows)

    # TODO: Метод, определяющий, есть ли пользователь с данным id в БД, если есть, то возвращающий класс User,
    #       в противном случае None
    @staticmethod
    def get_user(user_id):
        with pymysql.connect(**DatabaseController.connection) as connection:
            cursor = connection.cursor()
            cursor.execute('select user_id, grade, grade_value, grade_name '
                           'from user '
                           'inner join grade '
                           'on user.grade = grade.grade_id '
                           'where user_id = %s', (user_id,))
            user = cursor.fetchone()
            return user


    # TODO: Метод, добавляющий пользователя в БД (id, grade)
    @staticmethod
    def add_user(user_id,  grade_id):
        with pymysql.connect(**DatabaseController.connection) as connection:
            cursor = connection.cursor()
            cursor.execute('insert user (user_id, grade) values (%s, %s)', (user_id, grade_id))
            connection.commit()

