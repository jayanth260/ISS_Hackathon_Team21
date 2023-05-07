import sqlite3
from flask import Flask, render_template, request,jsonify,redirect,url_for,flash,get_flashed_messages

app=Flask(__name__)

conn = sqlite3.connect('database.db')
c = conn.cursor()

@app.route('/settleBill', methods=['GET','POST'])
def settle_expense():
    friend_name = request.form['user-name']
     
    dic=[]
    d=c.execute("SELECT Name FROM login_log")
    for x in d:
        for s in x:
            dic.append(s)
    user_name = dic[-1]

    amount_to_be_paid = request.form['payment']

    query1="SELECT owebyU FROM Info WHERE username=? AND frname=?"
    query2="SELECT owebyfr FROM Info WHERE username=? AND frname=?"
    c.execute(query1,(user_name,friend_name,))
    amount_you_owe = c.fetchone()[0]
    c.execute(query2,(user_name, friend_name,))
    amount_fr_is_owed = c.fetchone()[0]

    amount_you_owe = amount_you_owe - amount_to_be_paid
    amount_fr_is_owed = amount_fr_is_owed - amount_to_be_paid

    c.execute("UPDATE Info SET owebyU = ? WHERE username=? AND frname= ?",(amount_you_owe, user_name,friend_name))
    c.execute("UPDATE Info SET owebyfr = ? WHERE username=? AND frname= ?",(amount_fr_is_owed, friend_name, user_name))    

if __name__ == '__main__':
    app.run(debug=True)