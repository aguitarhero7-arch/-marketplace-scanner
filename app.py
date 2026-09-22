from flask import Flask,render_template,jsonify
from database import connect
from scanner import scan
app=Flask(__name__)
@app.get('/')
def home(): return render_template('index.html',listings=connect().execute('SELECT * FROM listings ORDER BY first_seen DESC').fetchall())
@app.get('/api/listings')
def api(): return jsonify([dict(x) for x in connect().execute('SELECT * FROM listings ORDER BY first_seen DESC').fetchall()])
if __name__=='__main__': app.run(host='0.0.0.0',port=5000)
