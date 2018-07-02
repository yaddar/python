from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return "My First Website"


@app.route('/about')
def home2():
    return "My First Website"

if __name__ == "__main__":
    app.run(debug=True)
