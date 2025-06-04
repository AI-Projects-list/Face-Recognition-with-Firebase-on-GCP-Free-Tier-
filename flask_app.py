from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route("/")
def index():
    logs = db.collection("face_logs").order_by("time", direction=firestore.Query.DESCENDING).limit(10).stream()
    return render_template("index.html", logs=[log.to_dict() for log in logs])

if __name__ == "__main__":
    app.run(debug=True)