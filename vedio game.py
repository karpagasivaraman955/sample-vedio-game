from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fake user data for demonstration (replace with a real database)
users = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'},
]


@app.route('/')
def home():
    return 'Welcome to the Login Page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username and password match a user in the database
        for user in users:
            if user['username'] == username and user['password'] == password:
                # Successful login, redirect to a dashboard or profile page
                return redirect(url_for('dashboard'))

        # If the username and password don't match, show an error message
        error_message = 'Invalid credentials. Please try again.'
        return render_template('login.html', error_message=error_message)

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return 'Welcome to the Dashboard'


if __name__ == '__main__':
    app.run(debug=True)
