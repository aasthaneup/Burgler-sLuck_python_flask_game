from flask import Flask, render_template, request, redirect, session, Markup
import random
app = Flask(__name__)
# app secret key here

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
    # create attempts counter in session if its a new game
    if 'counter' not in session:
        session['counter'] = 10
    # create gold amount in session if its a new game
    if 'totalGold' not in session:
        session ['totalGold'] = 0
    if 'result' not in session:
        session['result'] = 'na'
    if 'comment' not in session:
        session['comment'] = 'Lets get Bilbo started!!'
    return render_template("board.html", totalGold = session['totalGold'], counter = session['counter'])

@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/steal', methods = ['POST'])
def steal_gold():
    # process here
    if request.form['clicked'] == 'elv':
        stolenGold = random.randint(2,6)
        print("went into the elv hut and stole this much gold coins")
        print(stolenGold)
        session['comment'] = "Bilbo went to the Elv's hut and stole "+str(stolenGold)+" gold coins! 💰💰💰"
    if request.form['clicked'] == 'fairy':
        stolenGold = random.randint(5,11)
        print("went into the fairy den and stole this much gold coins")
        print(stolenGold)
        session['comment'] = "Bilbo went to the Fairy's den and stole "+str(stolenGold)+" gold coins! 💰💰💰"
    if request.form['clicked'] == 'leprechaun':
        stolenGold = random.randint(10,21)
        print("went into the leprechaun castle and stole this much gold coins:")
        print(stolenGold)
        session['comment'] = "Bilbo went to the leprechaun's castle and stole "+str(stolenGold)+" gold coins! 💰💰💰"
    if request.form['clicked'] == 'dragon':
        stolenGold = random.randint(-50,51)
        if stolenGold >=0:
            print("went into the dragon lair and stole this much gold coins:")
            print(stolenGold)
            session['comment'] = "Bilbo went to the Dragon's lair and stole "+str(stolenGold)+" gold coins! 💰💰💰"
        else:
            print("went into the dragon got caught and had to cough up this much gold coins:")
            print(stolenGold)
            session['comment'] = "Bilbo went to the Dragon's lair, got caught and had to cough up "+str(-stolenGold)+" gold coins! 🐲 🐲 🐲"
    # decrement counter
    newCounter = int(session['counter']) - 1
    session['counter'] = newCounter
    gold = stolenGold + int (session['totalGold'])
    session['totalGold'] = gold
    print('Total gold with Bilbo:')
    print(session['totalGold'])
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
            # session['result'] = 'na'
            return redirect("/game")

@app.route('/reset')
def reset():
    session.clear()
    # alternate way to clear individual keys from session
    # session.pop('counter')
    # session.pop('totalGold')
    return redirect('/game')


if __name__=="__main__":
    app.run(debug = True)