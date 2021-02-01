from flask import Flask

from flask import Flask, render_template

app = Flask(__name__) # create a flask app named app
@app.route("/")
def home():
        return render_template('home.html', title="home")


@app.route("/login/")
def login():
   return render_template('login.html', title="Login")

@app.route("/home/")
def page():
    return render_template('home.html', title="Login")




if __name__ == "__main__":
 app.run(port=5005)


