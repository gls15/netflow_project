import sqlite3

def sql_connection():
    try:
        con = sqlite3.connect("file_access.db")
        return con
    except sqlite3.Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS file_access(config_file text, report_file text, pwd_hash blob, iv blob, pad integer, PRIMARY KEY(report_file))")
    con.commit()

def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute("UPDATE OR IGNORE file_access SET config_file = ?, report_file = ?, pwd_hash = ?, iv = ?, pad = ?", entities)
    cursorObj.execute("INSERT OR IGNORE INTO file_access(config_file, report_file, pwd_hash, iv, pad) VALUES(?, ?, ?, ?, ?)", entities)
    con.commit()

def sql_fetch(con, filename):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM file_access WHERE report_file = ?", (filename,))
    row = cursorObj.fetchone()
    return row

