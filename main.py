from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.sqlite3"

db = SQLAlchemy(app)

# Criando a tabela Post
class Post(db.Model):
    # Adicionando colunas
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    author = db.Column(db.String())

# Home
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/post/add", methods=['POST'])
def add_post():
    try:
        form = request.form
        post = Post(title=form['title'], content=form['content'], author=form['author'])
        db.session.add(post)
        db.session.commit()
    except:
        print("erro")

    return redirect(url_for("home"))

# Criando o Banco de Dados
with app.app_context():
    db.create_all()
app.run(debug=True)