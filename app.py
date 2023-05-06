import sqlite3
from flask import Flask, render_template, request,jsonify,redirect,url_for,flash,get_flashed_messages

app = Flask(__name__,static_url_path='/static')
app.config['SECRET_KEY'] = 'your_secret_key_here'


@app.route('/',  methods=['POST','GET'])
def Home():
    return render_template('Home.html')



@app.route('/Signup', methods=['POST','GET'])
def Signup():
    if request.method=='POST':
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
# Create playlist table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS profiles
             (Username TEXT, 
             Email TEXT,
             Phone TEXT,
             Password TEXT,
             Owed INTEGER,
             Owes INTEGER)''')
        username=request.form['username']
        email=request.form['email']
        phone=request.form['mobile']
        password=request.form['password']

        d=c.execute("SELECT Username FROM profiles")
        for x in d:
            for i in x:
                if username==i:
                    flash('username exits!Try different')
                    messages = get_flashed_messages()
                    return render_template('Signup.html', messages=messages)
        sql = "INSERT INTO profiles VALUES ('%s', '%s','%s','%s',%d,%d)" % (username, email,phone,password,0,0)
        c.execute(sql)
        c.execute('''CREATE TABLE IF NOT EXISTS login_log
        (Name TEXT,
        Password TEXT)''')
        sql = "INSERT INTO login_log (name, password) VALUES ('%s', '%s')" % (username, password)
        c.execute(sql)
       
        print(username)
# Construct the CREATE TABLE statement using the variable name
        sql1 = f"CREATE TABLE {username} (id INTEGER PRIMARY KEY, name TEXT,owebyU INTEGER, owebyfr INTEGER)"

        c.execute(sql1)
        conn.commit()
        
        conn.close()
        flash('Login successful!Welcome to splitwise')
        messages = get_flashed_messages()
        return render_template('Dashboard.html',messages=messages )





       
        
    

@app.route('/Login' ,methods=['POST','GET'])
def Login():
      if request.method=='POST':

        # Process the form data here
        name = request.form['name']
        # email = request.form['email']
        password = request.form['password']
        

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS login_log
        (Name TEXT,
        Password TEXT)''')
        # Append the user data to the file
        # user = {'name': name, 'email': email, 'password': password}
        y=0
        d=c.execute('SELECT Password FROM profiles WHERE Username=? ', (name,))
        for i in d:
            for x in i:
                y=x
        
        if y!=password or y==0:
            
            
            flash('Login Unsuccesful! Try again')
            messages = get_flashed_messages()
            return render_template('login.html', messages=messages)

        else :
            flash('Login successful!Welcome to splitwise')
            sql = "INSERT INTO login_log (name, password) VALUES ('%s', '%s')" % (name, password)
            c.execute(sql)

            conn.commit()
            c.close()
            conn.close()
            messages = get_flashed_messages()
            return render_template('Dashboard.html',messages=messages )
        # Return a success message
@app.route('/Profile')
def freinds():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    dic=[]
    d=c.execute("SELECT Name FROM login_log")
    for x in d:
        for s in x:
            dic.append(s)
    name=dic[-1]
    # print(req)
    d=c.execute("SELECT Owed,Owes FROM profiles WHERE Username=?",(name,))
    for i in d:
        Owed=i[0]
        Owes=i[1]
    dic1=[]
    sql = f"SELECT name FROM {name}"
    D=c.execute(sql)
    for i in D:
        for x in i:
            dic1.append(x)
    print(dic1)
        

    
    return render_template('profile.html',Owed=Owed,Owes=Owes,dic1=dic1)

@app.route('/Dashboard')
def freind():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    dic=[]
    d=c.execute("SELECT Name FROM login_log")
    for x in d:
        for s in x:
            dic.append(s)
    name=dic[-1]
    # print(req)
    d=c.execute("SELECT Owed,Owes FROM profiles WHERE Username=?",(name,))
    for i in d:
        Owed=i[0]
        Owes=i[1]
    
        

    
    return render_template('Dashboard.html',Owed=Owed,Owes=Owes)





@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/signup')
def signup():
    return render_template('Signup.html')
@app.route('/Profile')
def Profile():
    return render_template('profile.html')
@app.route('/Dashboard')
def Dashboard():
    return render_template('Dashboard.html')
@app.route('/Freinds')
def Freinds():
    return render_template('freinds.html')

if __name__=='__main__':
    app.run(debug=True)