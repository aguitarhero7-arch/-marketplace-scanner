from flask import Flask,render_template,jsonify,request

from database import connect 
from sources.manual_import import ManualImportSource


from scanner import scan

app=Flask(__name__)
@app.get('/')
def home(): return render_template('index.html',listings=connect().execute('SELECT * FROM listings ORDER BY first_seen DESC').fetchall())
@app.get('/api/listings')
def api(): return jsonify([dict(x) for x in connect().execute('SELECT * FROM listings ORDER BY first_seen DESC').fetchall()])
@app.post('/api/import')
def import_listings(): return jsonify({'added':scan(ManualImportSource(request.get_json()))})
if __name__=='__main__': app.run(host='0.0.0.0',port=5000)

