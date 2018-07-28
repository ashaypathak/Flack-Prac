import sqlite3 as sql
import _mysql

def insert_values(name, enro_no, bran, sp):
    con = sql.connect("flask_prac")
    cur = con.cursor()
    cur.execute("INSERT INTO per_details VALUES (?,?,?,?)", (name, enro_no, bran, sp))
    con.commit()
    con.close()

def retreive_values():
    db = _mysql.connect(host='127.0.0.1',
                        user='root',
                        passwd='',
                        db='flask_prac')
    final_name='s'
    sql = 'select location from Book_Location where Code like "%' + final_name + '%"'
    db.query(sql)
    data = db.store_result()
    data = data.fetch_row(maxrows=0, how=1)
    print(data)
    # Location of Book
    # b = int((data[0]['location']))
    # print(b)

    return data


if __name__ == '__main__':
    data1 = retreive_values()


