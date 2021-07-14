from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'I would be a landing file if that were setup'

@app.route('/dashboard')
def dashboard():
    return 'This is the dashboard'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}. Welcome to Flask'

@app.route('/multiply/<x>/<y>')
def multiply(x,y):
    result = int(x) * int(y)
    return render_template('multiply.html', template_x = x, y = y, result = result)

@app.route('/multiplication_table/<number>/<start>/<end>')
def multiplication_table(number, start, end):
    return render_template('table.html', number = int(number), start = int(start), end = int(end))

@app.route('/multiplication_table2/<int:number>/<int:start>/<int:end>')
def multiplication_table2(number, start, end):
    results = []
    for i in range(int(start), int(end+1)):
        results.append({
            'number' : number,
            'operation' : f'{number} * {i}',
            'output' : number * i,
            })
    return render_template('table2.html', results = results, number = int(number), start = int(start), end = int(end))

@app.route('/new')
def new_user():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create_user():
    print(request.form['first_name'])
    return render_template('create_result.html', 
        first_name = request.form['first_name'], 
        last_name = request.form['last_name'], 
        email = request.form['email'])

@app.route('/even_or_odd/<num>')
def even_or_odd(num):
    num = int(num)
    if num % 2 == 0:
        return f'{num} is even'
    else:
        return f'{num} is odd'

#Makes Flask File Run
if __name__ == "__main__":
    app.run(debug=True)