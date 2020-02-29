import sqlite3

def new_user():
    found = 0
    while found == 0:
        username = input("Wpisz swoją nazwę użytkownika: ")
        conn = sqlite3.connect('register.db')
        c = conn.cursor()
        find_user = ("SELECT * FROM user WHERE username = ?")
        c.execute(find_user,[(username)])

        if c.fetchall():
            print("Ta nazwa już istnieje, spróbuj ponownie ")
        else:
            found = 1

        email = input("Wpisz swój email: ")
        password = input("Wpisz hasło: ")
        password1 = input("Powtórz hasło: ")

        while password != password1:
            print("Hasło się nie zgadza, powtórz je ponownie ")
            password = input("Wpisz hasło: ")
            password1 = input("Powtórz hasło: ")
        insert_data = '''INSERT INTO user(username, email, password) VALUES(?,?,?) '''
        c.execute(insert_data,[(username), (email), (password)])
        conn.commit()

new_user()