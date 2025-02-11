from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')  # Add this route to serve index.html
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form.get('name')  # Get user input
    print(f"User entered: {user_name}")  # Store in a variable (for now)
    return render_template("plsplspls.html")

if __name__ == '__main__':
    app.run(debug=True)
