import sqlite3

from flask import Flask, request

app = Flask(__name__)
db = sqlite3.connect("notes.db", check_same_thread=False)


# @mitigates #api against #sqli using #bound-params -- "request.args q is passed to db.execute as a bound parameter in search_notes"
# @flows #api -> #db via sqlite3 -- "search reads notes matching q"
# @comment -- "GET /notes searches note bodies"
@app.get("/notes")
def search_notes():
    q = request.args.get("q", "")
    rows = db.execute("SELECT id, body FROM notes WHERE body LIKE ?", (f"%{q}%",)).fetchall()
    return {"notes": rows}
