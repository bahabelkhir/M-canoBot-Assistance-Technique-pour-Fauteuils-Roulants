from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Configuration de la base de données SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "supersecretkey"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

df = pd.read_csv('Questions_Finales_Nettoy_es.csv')
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['question'])
def chatbot_response(user_input, threshold=0.2):
    # Preprocess the user input
    user_input = user_input.lower().strip()

    # Vectorize the user input
    user_input_vector = vectorizer.transform([user_input])

    # Compute cosine similarity between user input and all questions
    similarities = cosine_similarity(user_input_vector, tfidf_matrix)

    # Find the index of the most similar question and its similarity score
    most_similar_index = similarities.argmax()
    max_similarity = similarities[0, most_similar_index]

    # Check if similarity is above threshold
    if max_similarity >= threshold:
        return df.iloc[most_similar_index]['answer']
    else:
        return "Je n'ai pas de réponse à cette question, merci de bien vouloir contacter l'assistant RavenFox ou reformulez votre question."


# Modèle utilisateur (Correction : suppression de username)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    type_chaise = db.Column(db.String(50), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return redirect(url_for("login"))  # Redirige vers la page de connexion

# Route pour Inscription (Correction : Ajout d'une vérification de l'email)
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nom = request.form["nom"]
        prenom = request.form["prenom"]
        email = request.form["email"]
        password = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")
        type_chaise = request.form["type_chaise"]

        # Vérifier si l'email existe déjà
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Erreur : Cet email est déjà utilisé.", 400  # Message d'erreur

        # Création de l'utilisateur
        user = User(nom=nom, prenom=prenom, email=email, password=password, type_chaise=type_chaise)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    
    return render_template("register.html")

# Route pour Connexion (Correction : Remplacement de username par email)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("chatbot"))
        else:
            return "Erreur : Email ou mot de passe incorrect.", 401  # Message d'erreur

    return render_template("login.html")

# Route du Chatbot
@app.route("/chatbot")
@login_required
def chatbot():
    return render_template("chatbot.html")

# API du Chatbot (simulé)
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("question", "")
    response = chatbot_response(question)  
    return jsonify({"reponse": response})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Création de la base de données
    app.run(debug=True)
