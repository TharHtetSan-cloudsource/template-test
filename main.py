from flask import Flask,url_for,render_template

app = Flask(__name__,static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.get("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')