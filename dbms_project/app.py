from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('school.db')
    conn.row_factory = sqlite3.Row
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
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO teachers (name, subject, class, type, class_lab_count)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, subject, teacher_class, class_lab_type, class_lab_count))
        
        conn.commit()
        conn.close()
        
        return jsonify({'status': 'success'}), 200
    except sqlite3.IntegrityError as e:
        return jsonify({'status': 'failure', 'reason': str(e)}), 500

@app.route('/get_teachers', methods=['GET'])
def get_teachers():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM teachers")
    teachers = cursor.fetchall()
    conn.close()

    teachers_list = [dict(row) for row in teachers]
    
    return jsonify(teachers_list)

if __name__ == '__main__':
    app.run(debug=True)
