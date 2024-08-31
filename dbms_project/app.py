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

if __name__ == '__main__':
    app.run(debug=True)
