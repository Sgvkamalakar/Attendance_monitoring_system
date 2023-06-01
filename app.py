from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = '' #Add your secret key here  
db = mysql.connector.connect(
    host='localhost',
    user='', #add your username here
    password='',#add your password here
    database='' # add your db name here
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        cur = db.cursor()
        if role == 'teacher':
            cur.execute("SELECT * FROM teachers WHERE username = %s AND password = %s", (username, password))
            user = cur.fetchone()
            if user:
                session['loggedin'] = True
                session['username'] = user[0]
                session['role'] = 'teacher'
                return redirect('/teacher/dashboard')
            else:
                error = 'Invalid login credentials.'
                return render_template('login.html', error=error)
        elif role == 'admin':
            cur.execute("SELECT * FROM admins WHERE username = %s AND password = %s", (username, password))
            user = cur.fetchone()
            if user:
                session['loggedin'] = True
                session['username'] = user[0]
                session['role'] = 'admin'
                return redirect('/admin/admin_dashboard')
            else:
                error='Invalid login credentials'
                return render_template('login.html',error=error)
        cur.close()
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        cursor = db.cursor()
        query = "SELECT username FROM teachers WHERE username = %s"
        cursor.execute(query, (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            error_message = "Username already exists. Please choose a different one."
            return render_template('teacher_registration.html', error=error_message)
        insert_query = "INSERT INTO teachers (teacher_name, username, password, email, phone) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (name, username, password, email, phone))
        db.commit()
        return render_template('teacher_registration.html', message="Teacher successfully registered.")
    return render_template('teacher_registration.html')

@app.route('/student_register', methods=['GET', 'POST'])
def student_register():
    if request.method == "POST":
        student_id = request.form['student_id']
        name = request.form['name']
        class_sec = request.form['class_sec']
        email = request.form['email']
        phone = request.form['phone']
        cursor = db.cursor()
        query = "SELECT student_id FROM students WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        existing_user = cursor.fetchone()
        if existing_user:
            error_message = "Invalid student_id"
            return render_template('student_registration.html', error=error_message)
        insert_query = "INSERT INTO students (student_id, student_name, class_sec, email, phone) VALUES ( %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (student_id, name, class_sec, email, phone))
        db.commit()
        return render_template('student_registration.html', message="Student successfully registered.")
    return render_template('student_registration.html')

@app.route('/get_student',methods=['POST','GET'])
def get_student():
    if request.method=='POST':
        student_id=request.form['student_id']
        cur = db.cursor()
        cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
        student = cur.fetchone()
        if student:
            message="Fetched student details"
            return render_template('update_student.html', student=student, msg=message)
        else:
            error = "Invalid Student ID"
            return render_template('update_student.html', err=error)
    return render_template('update_student.html') 

@app.route('/update_student', methods=['GET', 'POST'])
def update_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        new_name = request.form['new_name']
        new_email = request.form['new_email']
        new_phone = request.form['new_phone']
        cur = db.cursor()
        cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
        student = cur.fetchone()
        if student:
            cur.execute("UPDATE students SET student_name = %s, email = %s, phone = %s WHERE student_id = %s",(new_name, new_email, new_phone, student_id))
            db.commit()
            message = "Student ID " +str(student_id)+" details have been successfully updated."
            return render_template('update_student.html', student=student, message=message)
        else:
            error = "Invalid Student ID"
            return render_template('update_student.html', error=error)
    return render_template('update_student.html')

@app.route('/teacher/dashboard')
def teacher_dashboard():
    if 'loggedin' in session and session['role'] == 'teacher':
        cur = db.cursor()
        cur.execute("SELECT * FROM classes WHERE teacher_username = %s", (session['username'],))
        classes = cur.fetchall()
        cur.close()
        return render_template('teacher_dashboard.html', classes=classes)
    else:
        return redirect('/')
    
@app.route('/teacher/teacher_profile')
def teacher_profile():
    cur = db.cursor()
    cur.execute("SELECT teacher_name, email, phone FROM teachers WHERE username = %s", (session['username'],))
    profile_data = cur.fetchone()
    cur.close()
    return render_template('teacher_profile.html', profile_data=profile_data)

@app.route('/teacher/update_profile', methods=['POST'])
def update_profile():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    cur = db.cursor()
    cur.execute("UPDATE teachers SET teacher_name = %s, email = %s, phone = %s WHERE username = %s",(name, email, phone, session['username']))
    db.commit()
    cur.close()
    return redirect('/teacher/teacher_profile')

@app.route('/teacher/add_class', methods=['GET', 'POST'])
def add_class():
    if 'loggedin' in session and session['role'] == 'teacher':
        cur = db.cursor()
        if request.method == 'POST':
            class_name = request.form['class_name']
            class_section = request.form['class_section']
            attendance_date = request.form['attendance_date']
            cur.execute("INSERT INTO classes (class_sec, class_name,class_date, teacher_username) VALUES (%s,%s, %s, %s)",(class_section,class_name,attendance_date, session['username']))
            db.commit()
            cur.close()
            return redirect('/teacher/dashboard')
        cur.execute('SELECT DISTINCT class_sec from classes')
        class_sections = cur.fetchall()
        cur.close()
        return render_template('add_class.html', class_sections=class_sections)
    else:
        return redirect('/')
    
@app.route("/teacher/mark_attendance/<class_id>", methods=['GET'])
def display_attendance_form(class_id):
    if 'loggedin' in session and session['role'] == 'teacher':
        cur = db.cursor()
        cur.execute("SELECT * FROM classes WHERE class_id = %s", (class_id,))
        classes = cur.fetchone()
        cur.execute("SELECT * FROM students WHERE class_sec = %s", (classes[3],))
        students = cur.fetchall()
        cur.close()
        return render_template('mark_attendance.html', students=students, class_date=classes[4], class_name=classes[1], class_sec=classes[3], class_id=classes[0])
    else:
        return redirect('/teacher/mark_attendance/<class_id>')


@app.route("/teacher/mark_attendance/<class_id>", methods=['POST'])
def update_attendance(class_id):
    if 'loggedin' in session and session['role'] == 'teacher':
        attendance_data = request.form.getlist('attendance')
        cur = db.cursor()
        cur.execute("SELECT class_name FROM classes WHERE class_id=%s",(class_id,))
        class_name=cur.fetchone()
        cur.execute("DELETE FROM attendance WHERE class_id = %s", (class_id,))
        db.commit()
        cur.execute("SELECT class_date FROM classes WHERE class_id = %s", (class_id,))
        class_date = cur.fetchone()
        cur.execute("SELECT class_sec FROM classes WHERE class_id = %s", (class_id,))
        class_sec = cur.fetchone()
        cur.execute("SELECT student_id FROM students WHERE class_sec=%s", (class_sec[0],))
        students = [student[0] for student in cur.fetchall()]
        student_ids = []
        for student_id in students:
            if str(student_id) in attendance_data:
                student_ids.append(student_id)
        present_students = []
        absent_students = []
        for student_id in students:
            if student_id in student_ids:
                cur.execute("INSERT INTO attendance (class_id, student_id, class_date, status) VALUES (%s, %s, %s, %s)",
                            (class_id, student_id, class_date[0], 'present'))
            else:
                cur.execute("INSERT INTO attendance (class_id, student_id, class_date, status) VALUES (%s, %s, %s, %s)",
                            (class_id, student_id, class_date[0], 'absent'))
        db.commit()        
        cur.execute("SELECT student_id FROM attendance WHERE status='present' and class_id=%s",(class_id,)) 
        present_std=cur.fetchall()
        for i in present_std:
            cur.execute("SELECT student_name,phone FROM students WHERE student_id=%s",(i[0],)) 
            student_det=cur.fetchone()
            present_students.append((i[0],student_det[0],student_det[1]))   
        cur.execute("SELECT student_id FROM attendance WHERE status='absent' and class_id=%s",(class_id,)) 
        absent_std=cur.fetchall()
        for i in absent_std:
            cur.execute("SELECT student_name,phone FROM students WHERE student_id=%s",(i[0],)) 
            student_det=cur.fetchone()
            absent_students.append((i[0],student_det[0],student_det[1]))       
        cur.close()
        return render_template('get_attendance.html', class_name=class_name,class_sec=class_sec,class_date=class_date,present_students=present_students, absent_students=absent_students)
    else:
        return redirect('/teacher/mark_attendance/<class_id>')


@app.route('/admin/admin_dashboard')
def admin_dashboard():
    if 'loggedin' in session and session['role'] == 'admin':
        return render_template('admin_dashboard.html')
    else:
        return redirect('/')



@app.route("/admin/get_attendance_report", methods=['GET', 'POST'])
def get_attendance_report():
    if 'loggedin' in session and session['role'] == 'admin':
        if request.method == 'POST':
            class_sec = request.form.get('class_sec')
            class_date = request.form.get('class_date')
            class_name = request.form.get('class_name')
            
            cur = db.cursor()
            cur.execute("SELECT student_id, student_name FROM students WHERE class_sec = %s", (class_sec,))
            students = cur.fetchall()
            
            cur.execute("SELECT student_id, status FROM attendance WHERE class_id IN (SELECT class_id FROM classes WHERE class_sec = %s AND class_date = %s AND class_name = %s)", (class_sec, class_date, class_name))
            attendance = cur.fetchall()
            
            cur.close()
            
            return render_template('attendance_report.html', class_sec=class_sec, class_date=class_date, class_name=class_name, students=students, attendance=attendance)
        else:
            cur = db.cursor()
            cur.execute("SELECT DISTINCT class_sec FROM classes")
            secs = cur.fetchall()
            cur.execute("SELECT DISTINCT class_name FROM classes")
            class_names = cur.fetchall()
            cur.close()
            
            return render_template('attendance_report.html', class_secs=secs, class_names=class_names)
    else:
        return redirect('/admin/login')


    
@app.route('/admin/admin_profile')
def admin_profile():
    cur = db.cursor()
    cur.execute("SELECT admin_name, email, phone FROM admins WHERE username = %s", (session['username'],))
    profile_data = cur.fetchone()
    cur.close()
    return render_template('admin_profile.html', profile_data=profile_data)

@app.route('/admin/update_admin_profile', methods=['POST'])
def update_admin_profile():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    cur = db.cursor()
    cur.execute("UPDATE admins SET admin_name = %s, email = %s, phone = %s WHERE username = %s",(name, email, phone, session['username']))
    db.commit()
    cur.close()
    return redirect('/admin/admin_profile')
    
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('role', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
