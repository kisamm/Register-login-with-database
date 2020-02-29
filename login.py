import sqlite3


def login():
    while True:
        username = input("Wpisz nazwę użytkownika ")
        password = input("Wpisz hasło ")
        conn = sqlite3.connect('register.db')
        c = conn.cursor()
        find_users = ("SELECT * FROM user WHERE username = ? AND password = ?")
        c.execute(find_users, [(username), (password)])
        results = c.fetchall()

        if results:
            for i in results:
                print("Witamy na stronie " + i[1])
            # return("exit")
            break
        else:
            print("Hasło bądź login jest nieprawidłowy")
            again = input("Chcesz spróbować zalogować się ponownie? y/n: ")
            if again.lower() == "n":
                print("Do widzenia")
                time.sleep(1)
                # return("Exit")
                break

login()
