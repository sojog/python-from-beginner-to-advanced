import sqlite3


with sqlite3.connect("chuck.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        """

        CREATE TABLE IF  NOT EXISTS jokes( id INTEGER PRIMARY KEY AUTOINCREMENT,
        value TEXT NOT NULL
        );
        """
    )
    joke = "In ancient China there is a legend that one day a child will be born from a dragon, grow to be a man, and vanquish evil from the land. That man is not Chuck Norris, because Chuck Norris killed that man."

    cursor.execute(f"""
        INSERT INTO jokes ( value) VALUES ( "{joke}");
    """)
    conn.commit()

