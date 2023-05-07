# ISS Hackathon Team 21
## Website : Splitwise
### Features
The website created is a web-based clone of the application **Splitwise**. 
1. The website features a Login/Sign-Up page which serves as the home page. The Login option redirects the user directly to the **Dashboard**. The Sign-Up option redirects to a sign-up page where the user has to enter their details. Following this, the user is redirected to the **Dashboard**.
2. The **Dashboard** features two options : **Add an Expense** and **Settle an Expense** which like their namesake are for adding a new expense and settling an old expense with friends respectively.
3. The **Friends** page lists all the friends the user has transactions along with a feature to add more friends and remove existing friends.
4. The **Groups** page lists all the groups the user is a part of - formed from the user's friend list. 
5. The **Profile** page contains the username, user's email address, user's phone number, a list of the user's friends, the total amount that the user owes and the total amount owed to the user by their friends. There is also a **Logout** option for the user to logout of their account.

### Frameworks and Packages
1. Flask
2. SQLite3
3. Google Fonts

### Instructions To Run The Application
All the files connected to the web application have to be placed in a single folder. The Login/Sign-Up page should be opened in the browser first - other pages are navigated to after logging in/signing up. The python files (with extension .py) have to be run on a suitable platform (a text editor like VSCode) before viewing the webpages on the browser. (It is to be noted that the image files used have to be present in the folder)

### Contribution
1. Jayanth - profile.html, app.py, database.db, script.js, style.css, Login.html, Signup.html 
2. Deekshitha - home.html, friends.html, Groups.html, groups.js 
3. Gadha - dashboard.html, expense.html, expense.css, expense.js, expense.py, settle.html, settle.py
4. CSS files for the dashboard, friends, groups, home and profile pages were combined into one file - dashboard.css
