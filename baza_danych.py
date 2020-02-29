import sqlite3

conn = sqlite3.connect('register.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user(
                userID integer PRIMARY KEY,
                username varchar(20) NOT NULL,
                email varchar(20) NOT NULL,
                password varchar(20) NOT NULL)
                ''')

#c.execute("INSERT INTO user(userID, username, email, password) VALUES(1,'kisamm','kisam1@o2.pl','admin')")
#conn.commit()


