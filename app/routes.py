from flask import Flask, request, render_template
from app import app, db
from app.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        # Secure query using parameterized queries
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return f"User {username} added successfully!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
