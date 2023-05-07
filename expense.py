import sqlite3
from flask import Flask, render_template, request,jsonify,redirect,url_for,flash,get_flashed_messages

app=Flask(__name__)

conn = sqlite3.connect('database.db')
c = conn.cursor()


@app.route('/addBill', methods=['GET','POST'])
def calculate_expense():
    split_type = request.form['split-type']
   
    dic=[]
    d=c.execute("SELECT Name FROM login_log")
    for x in d:
        for s in x:
            dic.append(s)
    user_name = dic[-1]

    if split_type == 'Friend':
        friend_name = request.form['friend_name']
        owed_amount = request.form['friend-cost-per-person']
        amount_you_owe_query = "SELECT owebyU FROM Info WHERE username=? AND frname = ?"
        amount_you_are_owed_query = "SELECT owebyfr FROM Info WHERE username=? AND frname = ?"
        c.execute(amount_you_owe_query, (friend_name,))
        amount_you_owe = c.fetchone()[0]
        c.execute(amount_you_are_owed_query, (friend_name,))
        amount_you_are_owed = c.fetchone()[0]
        if owed_amount >= 0:
            amount_you_owe = amount_you_owe + owed_amount
            c.execute("UPDATE Info SET owebyU = ? WHERE username=? AND frname = ?", (amount_you_owe, user_name,friend_name,))
            c.execute("UPDATE Info SET owebyfr = ? WHERE username=? AND frname = ?", (amount_you_owe, friend_name, user_name))
        elif owed_amount < 0:
            amount_you_are_owed = amount_you_are_owed - owed_amount
            c.execute("UPDATE Info SET owebyfr = ? WHERE username=? AND frname = ?", (amount_you_are_owed, user_name, friend_name))
            c.execute("UPDATE Info SET owebyU = ? WHERE username=? AND frname = ?", (amount_you_are_owed, friend_name, user_name))



    elif split_type=="Group":
        group_name = request.form['group_name']
        c.execute("SELECT username FROM Groups WHERE Gname=?", (group_name,))
        friend_names = [row[0] for row in c.fetchall()]

# Add labels for each friend to the form
        for friend_name in friend_names:
            friend_label = f"<label for='{friend_name}'>{friend_name} Paid</label>"
            friend_input = f"<input type='number' id='{friend_name}' name='{friend_name}'>"
            friend_fields = f"<div class='form-group-split-fields split-friend'>{friend_label}{friend_input}</div>"
    # Append the friend fields to the form
        form_element = driver.find_element_by_tag_name('form')
        form_element.insert_child(-2, friend_fields)


    



    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
