from flask import Flask, render_template, request, redirect

app = Flask(__name__)

names = [
    "Alex", "Veronica", "Heather", "JD"
]

#localhost:5000
@app.route('/')
def index():
    return render_template("landing.html", people=names, player=None)

@app.route('/leave')
def leave():
    return render_template("outside.html")

#listen for localhost:5000/choose_name (POST request)
@app.route('/choose_name', methods=['POST'])
def choose_name():
    print(request.form) #shows whole dictionary
    print(request.form["alias"])
    return render_template("landing.html", people=names, player=request.form['alias'])

if __name__=="__main__":
    app.run(debug=True)