from flask import Flask, render_template, redirect, request, session
import random, collections
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super secret key :3'

@app.route('/')
def landing():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('landing.html', activities = session['activities'])

@app.route('/gold', methods=['POST'])
def gold():
    location = request.form['location']
    user_gold = session['gold']
    activities = session['activities']

    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now()
    myTime = date.strftime(date_format)

    if(location == 'farm'):
        thisTurnGold = round(random.random() * 3 + 2)
        myString = "You rummaged through a Farm and gained " + str(thisTurnGold) + " Gold. " + str(myTime)

    elif(location == 'cave'):
        thisTurnGold = round(random.random() * 6 + 10)
        myString = "You spelunked a Cave and discovered " + str(thisTurnGold) + " Gold. " + str(myTime)

    elif(location == 'keep'):
        thisTurnGold = round(random.random() * 20 + 20)
        myString = "You raided a Keep and plundered " + str(thisTurnGold) + " Gold. " + str(myTime)

    elif(location == 'thieves_den'):
        thisTurnGold = round(random.random() * 60 + 15)
        gainOrLoss = round(random.random() + 1)
        #Gain: 1 means loss of $$. 2 means Gain of $$
        if(gainOrLoss == 1):
            myString = "You infiltrated a Thieves' Den and were mugged. Lost " + str(thisTurnGold) + " Gold. " + str(myTime)
            thisTurnGold *= -1
        else:
            myString = "You infiltrated a Thieves' Den and snuck successfully. Stole " + str(thisTurnGold) + " Gold! " + str(myTime)

    user_gold += thisTurnGold
    session['gold'] = user_gold
    session['activities'].insert(0, myString)
    return redirect('/')

@app.route('/reset_gold')
def reset_gold():
    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now()
    myTime = date.strftime(date_format)

    myString = f"You give all your gold to charity and continue on your journey {myTime}"
    session['activities'].insert(0, myString)
    session.pop('gold')
    return redirect('/')

@app.route('/reset_all')
def reset_all():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)