from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
    # create attempts counter in session
    # create gold amount in session
    return render_template("board.html")

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

if __name__=="__main__":
    app.run(debug = True)