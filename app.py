from flask import Flask
app = Flask(__name__)

@app.route('/', mehtods=['GET','POST'])
def index():
    return "STATAS OF ML"

if __name__=="__main__":
    app.run(debug=True)