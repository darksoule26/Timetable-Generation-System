from flask import Flask, request, jsonify, render_template
import mysql.connector


app = Flask(__name__)


# Function to connect to the MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='root',  # Replace with your MySQL password
        database='school'
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

# Route for Add/Remove Teacher page
@app.route('/add_remove_teacher')
def add_remove_teacher():
    return render_template('add_remove_teacher.html')



@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    data = request.get_json()
    name = data.get('name')
    subject = data.get('subject')
    teacher_class = data.get('class')
    class_lab_type = data.get('class_lab_type')
    class_lab_count = data.get('class_lab_count')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO teachers (name, subject, class, type, class_lab_count)
            VALUES (%s, %s, %s, %s, %s)
        ''', (name, subject, teacher_class, class_lab_type, class_lab_count))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({'status': 'success'}), 200
    except mysql.connector.Error as err:
        return jsonify({'status': 'failure', 'reason': str(err)}), 500

@app.route('/get_teachers', methods=['GET'])
def get_teachers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM teachers")
    teachers = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(teachers)

@app.route('/tyb_teachers')
def tyb_teachers():
    return render_template('tyb_teachers.html')

@app.route('/add_teacher_to_tyb', methods=['POST'])
def add_teacher_to_tyb():
    data = request.json
    name = data.get('name')
    subject = data.get('subject')
    lecture_type = data.get('lecture_type')
    lecture_count = data.get('lecture_count')
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO tyb (teacher_name, subject, lecture_type, lecture_count) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, subject, lecture_type, lecture_count))
        conn.commit()
        cursor.close()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'fail', 'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
