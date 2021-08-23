from flask import Flask, render_template, request, redirect, session, Markup
import random
app = Flask(__name__)
# app.secret_key = ""

# base route for home page
@app.route('/')
def index():
    return render_template("index.html")

# route for game board
@app.route('/game')
def game():
    # create attempts counter in session if its a new game
    if 'counter' not in session:
        session['counter'] = 10
    # create gold amount in session if its a new game
    if 'totalGold' not in session:
        session ['totalGold'] = 0
    # create result in session if its a new game
    if 'result' not in session:
        session['result'] = 'na'
    # create comment in session if its a new game
    if 'comment' not in session:
        session['comment'] = 'Lets get Bilbo started!!'
    return render_template("board.html", totalGold = session['totalGold'], counter = session['counter'])

# route for result page
@app.route('/result')
def result():
    return render_template("result.html")

# route for processing the stolen gold amount
@app.route('/steal', methods = ['POST'])
def steal_gold():
    if request.form['clicked'] == 'elv':
        stolenGold = random.randint(2,5)
        session['comment'] = "Bilbo went to the Elv's hut and stole "+str(stolenGold)+" gold coins! 💰💰💰"
    if request.form['clicked'] == 'fairy':
        stolenGold = random.randint(5,10)
        # print("went into the fairy den and stole this much gold coins")
        # print(stolenGold)
        session['comment'] = "Bilbo went to the Fairy's den and stole "+str(stolenGold)+" gold coins! 💰💰💰"
    if request.form['clicked'] == 'leprechaun':
        stolenGold = random.randint(10,20)
        session['comment'] = "Bilbo went to the leprechaun's castle and stole "+str(stolenGold)+" gold coins! 💰💰💰"
    if request.form['clicked'] == 'dragon':
        stolenGold = random.randint(-50,50)
        if stolenGold >=0:
            session['comment'] = "Bilbo went to the Dragon's lair and stole "+str(stolenGold)+" gold coins! 💰💰💰"
        else:
            session['comment'] = "Bilbo went to the Dragon's lair, got caught and had to cough up "+str(-stolenGold)+" gold coins! 🐲 🐲 🐲"
    # decrease the counter after each stealing attempt
    newCounter = int(session['counter']) - 1
    session['counter'] = newCounter
    gold = stolenGold + int (session['totalGold'])
    session['totalGold'] = gold
    # print('Total gold with Bilbo:')
    # print(session['totalGold'])
    if session['totalGold'] < 0:
        session['comment'] = Markup(session['comment']+'<br>Bilbo now is '+str(session['totalGold'])+' gold pieces in debt')
    else:
        session['comment'] = Markup(session['comment']+'<br>Bilbo now has a total of '+str(session['totalGold'])+' gold pieces')
    # keep playing until either Bilbo steals 200 golds or until its below 10 attempts
    # if 200 golds collected within 10 attempts; result will show success message else show failure message
    if session['counter'] <1:
        # end game since the 10 attempts are utilized
        if session['totalGold'] >= 200:
            session['result'] = 'success'
        else:
            session['result'] = 'fail'
        return redirect("/result")
    else:
        if session['totalGold'] >= 200:
            session['result'] = 'success'
            return redirect("/result")
        else:
            return redirect("/game")

# route for restarting the game
@app.route('/reset')
def reset():
    session.clear()
    # alternate way to clear individual keys from session
    # session.pop('counter')
    # session.pop('totalGold')
    return redirect('/game')

if __name__=="__main__":
    app.run(debug = True)