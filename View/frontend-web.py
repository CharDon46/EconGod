from flask import Flask, render_template

app = Flask(__name__)

# Set homepage
@app.route('/')
def home():
    return render_template("./home1/home.html")

# Run the flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)