from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'super secret key :P'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_form', methods=['POST'])
def handle_form():
    session['fav_color'] = request.form['fav_color']
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)