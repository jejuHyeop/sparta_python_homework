from flask import Flask, render_template, request, redirect, url_for
from random import randint as ri
from database import db, GameHistory
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
db.init_app(app)

@app.route('/')
def home():
    history = GameHistory.query.order_by(GameHistory.time).all()   
    win = GameHistory.query.filter_by(result="WIN").count() 
    lose = GameHistory.query.filter_by(result="LOSE").count() 
    draw = GameHistory.query.filter_by(result="DRAW").count()
    context = {
        "history" : history,
        "win" : win,
        "lose" : lose,
        "draw" : draw
    }
    return render_template('index.html', data=context)


def judge(ch):
    judge_string = "1231"
    if ch in judge_string:
        return False
    return True

@app.route('/logic', methods=['POST'])
def logic():
    rsp_list = ['two.png','zero.png','five.png']
    user_input = request.form.get('user_input')
    computer_input = ri(1,3)
    if user_input == str(computer_input):
        result = "DRAW"
    elif judge(user_input + str(computer_input)):
        result = "WIN"
    else:
        result = "LOSE"
    gh = GameHistory(user_choice=rsp_list[int(user_input)-1], computer_choice=rsp_list[computer_input-1], result=result)
    db.session.add(gh)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()