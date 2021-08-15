import sqlite3


def select_user():
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            """,
        )
    session.commit()
    for res in cursor:
        print(res)

select_user()



