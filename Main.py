import flask
from flask import Flask, request, render_template,redirect
import DBMS
import _mysql

app = Flask(__name__, static_path='')

@app.route('/')
def index():
    return render_template('details.html')

@app.route('/data_entry',methods=['POST'])
def data_entry():
    if request.method == 'POST':
        name=request.form['Name']
        erno=request.form['Enrollment_No']
        bran=request.form['Branch']
        list=[]
        list.append(name)
        list.append(erno)
        list.append(bran)
        db = _mysql.connect(host='127.0.0.1',
                            user='root',
                            passwd='',
                            db='flask_prac')
        db.query("select * from Student")
        data = db.store_result()
        data = data.fetch_row(maxrows=0, how=1)
        for i in data:
            a=(i['Name']).decode("utf-8")
            b= (i['Enrollment_No']).decode("utf-8")
            c= (i['Branch']).decode("utf-8")
            list1=[a,b,c]
            if(set(list)==set(list1)):
                return render_template('books_data.html')
        db.close()
        return index()
    else:
        return 'Not a valid call'

@app.route('/issue_book')
def issue_Book():
    return  render_template('Issue_Book.html')


@app.route('/student_data')
def Student_data():
    return render_template('enter_data.html')

@app.route('/librarian_data')
def librarian_data():
    return render_template('Enter_book_detail.html')


@app.route('/Enter_book',methods=['POST'])
def Enter_book():
    if request.method == 'POST':
        book_name=request.form['Name']
        book_code=request.form['Code']
        book_author=request.form['Author']
        book_department=request.form['Department']

        db = _mysql.connect(host='127.0.0.1',
                            user='root',
                            passwd='',
                            db='flask_prac')

        sql = """INSERT INTO
             Book (Code,Name,Author,Department) 
             VALUES ('%s', '%s', '%s', '%s')""" % (
        book_code,book_name,book_author,book_department)
        db.query(sql)
        db.close()
        return render_template('Enter_book_detail.html')
    else:
        return 'not a valid call'

@app.route('/list_all')
def list_all():
    db = _mysql.connect(host='127.0.0.1',
                        user='root',
                        passwd='',
                        db='flask_prac')
    sql = "SELECT * FROM Book"
    db.query(sql)
    list_of_all = db.store_result()
    list_of_all = list_of_all.fetch_row(maxrows=0, how=1)
    db.close()
    return render_template('list_all.html', list_of_all=list_of_all)

@app.route('/Book',methods=['POST'])
def book():
    if request.method == 'POST':
        final_name=request.form['Name']
        db = _mysql.connect(host='127.0.0.1',
                            user='root',
                            passwd='',
                            db='flask_prac')
        sql='select location from Book_Location where Code like "%' + final_name + '%"'
        db.query(sql)
        data = db.store_result()
        data = data.fetch_row(maxrows=0, how=1)
        print(data)
        # Location of Book
        b = int((data[0]['location']))
        print(b)
        db.close()

        db = _mysql.connect(host='127.0.0.1',
                            user='root',
                            passwd='',
                            db='flask_prac')
        sql='delete from Book where Code like "%' + final_name + '%"'
        db.query(sql)
        db.close()
        return index()
    else:
        return 'not a valid call'

if __name__ == '__main__':
    app.run(debug=True)

