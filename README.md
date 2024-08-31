

# Flask Teacher Management System

This project is a simple Flask-based web application that allows users to add and view teacher records. It demonstrates basic form handling, database interaction, and static files management in a Flask application.

## Prerequisites

Before running this project, ensure that the following dependencies and setup are in place:

### 1. **Check Dependencies**

Make sure all the required Python packages are installed. You can install them by running:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install Flask and any other dependencies by running:

```bash
pip install flask
```

### 2. **Configure Database**

- Ensure you have MySQL (or your preferred database) installed and running.
- Create a new MySQL database. You can use the following SQL command in your MySQL shell:

    ```sql
    CREATE DATABASE school;
    ```

- Create the necessary tables by executing the following SQL commands:

    ```sql
    CREATE TABLE teachers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        subject VARCHAR(100) NOT NULL,
        class VARCHAR(50) NOT NULL,
        class_lab_type VARCHAR(50) NOT NULL,
        class_lab_count INT NOT NULL
    );
    ```
    ```sql
    CREATE TABLE tyb (
       id INT AUTO_INCREMENT PRIMARY KEY,
       teacher_name VARCHAR(100) NOT NULL,
       subject VARCHAR(100) NOT NULL,
       lecture_type VARCHAR(50) NOT NULL,
       lecture_count INT NOT NULL
    );

    ```

### 3. **Update Database Configuration**

Make sure to update the following fields in `app.py` to match your MySQL credentials:

```python
app.config['MYSQL_USER'] = 'your_mysql_username'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'teacher_management'
```

You can change the `'your_mysql_username'`, `'your_mysql_password'`, and `'school'` to match your database details.

### 4. **Run the Application**

Once you’ve installed the dependencies and set up the database:

1. Navigate to the project directory.
2. Run the Flask application with the following command:

    ```bash
    python app.py
    ```

The app will run by default on `http://127.0.0.1:5000/`.

### 5. **Access the Application**

Open a browser and go to `http://127.0.0.1:5000/` to access the application.

## Features

- Add teacher information such as name, subject, class, and number of classes or labs per week.
- View all teacher records in a table format.

## Project Structure

```
project-directory/
│
├── app.py                  # Main Flask application
├── templates/
│   ├── index.html          # Main page
│   ├── add_remove_teacher.html  # Add/Remove teacher page
│
├── static/
│   ├── styles.css          # CSS styles
│
├── requirements.txt        # Project dependencies
└── README.md               # Project README
```

### Notes:
- Ensure your MySQL server is running before starting the Flask application.
- Use appropriate credentials in `app.py` for connecting to the database.

---

