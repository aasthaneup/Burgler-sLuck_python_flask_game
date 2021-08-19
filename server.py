from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# add the app secret key here

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
    return render_template("board.html", totalGold = session['totalGold'], counter = session['counter'])

@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/steal', methods = ['POST'])
def steal_gold():
    # process here
    # decrement/increment counter
    # keep playing until either Bilbo steals 200 golds or until its below 10 attempts
    # return redirect("/game")
    # if 200 golds collected within 10 attempts; result will show success message else show failure message
    return redirect('/result')

@app.route('/reset')
def reset():
    session.clear()
    # alternate way to clear individual keys from session
    # session.pop('counter')
    # session.pop('totalGold')
    return redirect('/game')


if __name__=="__main__":
    app.run(debug = True)