# MécanoBot-Assistance-Technique-pour-Fauteuils-Roulants
📌 Contexte
Développé lors d'un datathon pour une startup spécialisée dans la mobilité, MécanoBot est un chatbot intelligent conçu pour accompagner les utilisateurs de fauteuils roulants. Son rôle ? Résoudre les problèmes mécaniques courants en fournissant des réponses instantanées, basées sur une analyse approfondie des manuels techniques et guides de réparation.

🚀 Fonctionnalités Clés

1. Collecte & Préparation des Données
Extraction automatisée des données depuis les manuels de réparation et documentations techniques.
Nettoyage des données (suppression des doublons, normalisation du texte).

2. Création du Dataset Questions-Réponses
Structuration des données en paires {question → réponse} pour l’entraînement du modèle.
Annotation manuelle pour améliorer la pertinence des réponses.

3. Traitement du Langage Naturel (NLP)
Tokenisation et vectorisation du texte avec les bibliothèques comme NLTK et spaCy.
Utilisation de TF-IDF (Term Frequency-Inverse Document Frequency) pour pondérer les mots clés et identifier les réponses les plus pertinentes.

4. Modèle de Similarité Cosine
Implémentation d’un algorithme de similarité cosinus pour comparer les questions utilisateur avec la base de connaissances.
Retourne la réponse la plus proche en temps réel.

5. Application Web Flask (Déploiement)
Interface intuitive avec système d’authentification (inscription/connexion).
Base de données SQLite pour enregistrer les interactions utilisateurs.

Design responsive compatible mobile (Bootstrap/CSS).

🛠️ Technologies Utilisées
Ce projet combine plusieurs technologies et outils pour offrir une solution efficace et performante :

🌐 Backend & Web Framework
Flask : Framework Python léger et puissant pour développer l'application web

SQLite : Base de données légère pour stocker les interactions utilisateurs

🤖 Intelligence Artificielle & NLP
Cosine Similarity : Algorithme clé pour mesurer la similarité entre questions et trouver les réponses les plus pertinentes

Scikit-learn : Implémentation des algorithmes de NLP (TF-IDF, Similarité Cosinus)

NLTK : Bibliothèque pour le traitement avancé du texte (tokenization, suppression des stopwords)

📊 Data Processing
Pandas : Outil essentiel pour le nettoyage, la manipulation et l'analyse des données structurées

💄 Frontend & Interface
HTML/CSS : Fondations du rendu visuel

Bootstrap : Framework pour une interface responsive et moderne


