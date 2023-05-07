import sqlite3
from flask import Flask, render_template, request,jsonify,redirect,url_for,flash,get_flashed_messages

app = Flask(__name__,static_url_path='/static')
app.config['SECRET_KEY'] = 'your_secret_key_here'


@app.route('/',  methods=['POST','GET'])
def Home():
    return render_template('Home.html')

conn = sqlite3.connect('database.db')
c = conn.cursor()
sql1 = f"CREATE TABLE IF NOT EXISTS Info ( Username TEXT,frname TEXT,owebyU INTEGER, owebyfr INTEGER)"


c.execute(sql1)
sql1=f"CREATE TABLE IF NOT EXISTS Groups(Gname TEXT,username TEXT, Tbepaid INTEGER )"
c.execute(sql1)
conn.commit()
        
conn.close()

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
                    # flash('username exits!Try different')
                    # messages = get_flashed_messages()
                    return render_template('Signup.html')
        sql = "INSERT INTO profiles VALUES ('%s', '%s','%s','%s',%d,%d)" % (username, email,phone,password,0,0)
        c.execute(sql)
        c.execute('''CREATE TABLE IF NOT EXISTS login_log
        (Name TEXT,
        Password TEXT)''')
        sql = "INSERT INTO login_log (name, password) VALUES ('%s', '%s')" % (username, password)
        c.execute(sql)
       
        print(username)
# Construct the CREATE TABLE statement using the variable name
        sql1 = f"CREATE TABLE IF NOT EXISTS Info ( Username TEXT,frname TEXT,owebyU INTEGER, owebyfr INTEGER)"

        c.execute(sql1)
        conn.commit()
        
        conn.close()
      
        return redirect(url_for('Dashboard'))





        
    

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
            conn.commit()
            c.close()
            conn.close()

            
            
            # flash('Login Unsuccesful! Try again')
            # messages = get_flashed_messages()
            return render_template('Login.html')

        else :
            sql = "INSERT INTO login_log (name, password) VALUES ('%s', '%s')" % (name, password)
            c.execute(sql)

            conn.commit()
            c.close()
            conn.close()
            
            return redirect(url_for('Dashboard'))
        # Return a success message
@app.route('/Profile')
def Profile():
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
    sql = f"SELECT frname FROM Info Where Username=?"
    D=c.execute(sql,(name,))
    for i in D:
        for x in i:
            dic1.append(x)
    print(dic1)
        

    
    return render_template('profile.html',Owed=Owed,Owes=Owes,dic1=dic1,name=name)

@app.route('/Dashboard')
def Dashboard():
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






@app.route('/Friends', methods=['POST','GET'])
def Friends():
        conn=sqlite3.connect('database.db')
        c=conn.cursor()
        dic=[]
        d=c.execute("SELECT Name FROM login_log")
        for x in d:
            for s in x:
                dic.append(s)
        name=dic[-1]
        # print(req)
       
        dic1={}
        sql = f"SELECT frname,owebyU,owebyfr FROM Info WHERE Username=?"
    
        D=c.execute(sql,(name,))
        for i in D:
            dic1[i[0]]=[i[1]]
            dic1[i[0]]+=[i[2]]
        # print(dic1)
        d=len(dic1)
        

# Fetch the result and print it
      
        return render_template('friends.html',dic1=dic1,d=d)

@app.route('/friends', methods=['POST','GET'])
def add_Friends():
    # if request.method=='POST':
        frname=request.form['friend-name']
        # print(frname)
        conn=sqlite3.connect('database.db')
        c=conn.cursor()
        
        dic=[]
        d=c.execute("SELECT Name FROM login_log")
        for x in d:
            for s in x:
                dic.append(s)
        name=dic[-1]
        sql = f"SELECT EXISTS(SELECT 1 FROM profiles WHERE Username = ?)"

    # Execute the SQL query with the value to check as a parameter
        c.execute(sql, (frname,))
        


    # Fetch the result and print it
        result = c.fetchone()
        sql = f"SELECT EXISTS(SELECT 1 FROM Info WHERE frname = ? AND Username=?)"

    
        c.execute(sql, (frname,name))


    # Fetch the result and print it
        result1 = c.fetchone()

        if result1[0]==1:
            # flash('Already a friend!')
            # messages = get_flashed_messages()
            return redirect(url_for('Friends'))

        else:
            if result[0]==1:
                sql = f"INSERT INTO Info (Username,frname,owebyU,owebyfr) VALUES ('%s', '%s',%d,%d)" % (name,frname, 0,0)

                c.execute(sql)
                sql = f"INSERT INTO Info (Username,frname,owebyU,owebyfr ) VALUES ('%s','%s',%d,%d)"% (frname,name,0,0)
                c.execute(sql)
                conn.commit()
                c.close()
                conn.close()
                return redirect(url_for('Friends'))
        
            else:
                conn.commit()
                c.close()
                conn.close()
                # flash('No User')
                # messages = get_flashed_messages()
                return redirect(url_for('Friends'))
@app.route('/ffriends',methods=['POST','GET'])
def remove_Friend():
    
    frname=request.form['friend-name']
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    dic=[]
    d=c.execute("SELECT Name FROM login_log")
    for x in d:
        for s in x:
            dic.append(s)
    name=dic[-1]
    c.execute("DELETE FROM Info WHERE Username=? AND frname=?", (name,frname,))
    c.execute("DELETE FROM Info WHERE Username=? AND frname=?", (frname,name,))
    conn.commit()
    c.close()
    conn.close()

    return redirect(url_for('Friends'))



@app.route('/add-group', methods=['POST'])
def add_group():
    group_name = request.form['num-people2']
    num_people = int(request.form['num-people'])
    people = []
    for i in range(1, num_people+1):
        print(i)
        person_name = request.form.get(f'person{i}')
        people.append(person_name)

    print(group_name,num_people)
    print(people)
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    dic=[]
    d=c.execute("SELECT Name FROM login_log")
    for x in d:
        for s in x:
            dic.append(s)
        name=dic[-1]

    dic1=[]
    sql = f"SELECT frname FROM Info Where Username=?"
    D=c.execute(sql,(name,))
    for i in D:
        for x in i:
            dic1.append(x)
    dic1.append(name)
    # print(dic1)
    people[num_people-1]=name
    print(dic1,people)
    for i in range(0,num_people):
        if people[i] in dic1:
            sql=f"INSERT INTO Groups Values('%s','%s',%d)"%(group_name,people[i],0)
            c.execute(sql)
            print(people[i])
    

    conn.commit()
    c.close()
    conn.close()

    

    
    # Add group and people to database
    # ...
    
    response_data = {'message': 'Group added successfully'}
    return jsonify(response_data)



@app.route('/addexgr', methods=['POST'])
def addexgr():
    if request.method=='POST':
    
        amttol=request.form['amttol']
        amtU=request.form['amtU']
        group_name = request.form['num-people1']
        num_people = int(request.form['num-people'])
        people = []
        for i in range(1, num_people+1):
            person_name = request.form.get(f'person{i}')
            people.append(person_name)
        conn=sqlite3.connect('database.db')
        c=conn.cursor()
        dic=[]
        d=c.execute("SELECT Name FROM login_log")
        for x in d:
            for s in x:
                dic.append(s)
            name=dic[-1]

        
        people[num_people-1]=name   
        # print(group_name,people,amttol,amtU)
        per=0
        per=(amttol-amtU)/num_people
        for i in range(0,num_people):
            frname=people[i]
            
            sql= f"UPDATE Info SET owebyfr = owebyfr + {amttol-amtU} WHERE Username=? AND frname=?"
            c.execute(sql,(name,frname,))

            sql= f"UPDATE Info SET owebyU = owebyU + {amttol-amtU} WHERE Username=? AND frname=?"
            c.execute(sql,(frname,name,))


        
        
        # Do something with the retrieved data here
        
        return redirect(url_for('Expense'))

@app.route('/addexfr', methods=['POST'])
def addexfr():
    frname=request.form['name']
    amttol=request.form['amttol']
    amtU=request.form['amtU']

    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    dic=[]
    d=c.execute("SELECT Name FROM login_log")
    for x in d:
        for s in x:
            dic.append(s)
    name=dic[-1]
    
    # sql= f"UPDATE Info SET owebyfr = owebyfr + {amttol-amtU} WHERE Username=? AND frname=?"
    # c.execute(sql,(name,frname,))

    # sql= f"UPDATE Info SET owebyU = owebyU + {amttol-amtU} WHERE Username=? AND frname=?"
    # c.execute(sql,(frname,name,))

    


    print(frname,amttol,amtU)
    
    # Do something with the retrieved data here
    
    return redirect(url_for('Expense'))

@app.route('/login')
def login():
    return render_template('Login.html')
@app.route('/signup')
def signup():
    return render_template('Signup.html')
@app.route('/Groups')
def Groups():
    return render_template('Groups.html')
@app.route('/Expense', methods=['POST','GET'])
def Expense():
    return render_template('expense.html')



# @app.route('/Profile')
# def Profile():
#     return render_template('profile.html')
# @app.route('/Dashboard')
# def Dashboard():
#     return render_template('Dashboard.html')
# @app.route('/Friends')
# def Friends():
#     return render_template('friends.html')


if __name__=='__main__':
    app.run(debug=True)