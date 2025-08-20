<<<<<<< HEAD
from flask import Flask, render_template, flash, redirect, request, url_for, session
from locust import task
from forms import TaskForm
from forms import registerForm, loginForm, update
from flask_sqlalchemy import SQLAlchemy
from models import User, db, Task
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app= Flask(__name__)

"""configuration de la base de données"""
app.config['SECRET_KEY'] = 'une_cle_ultra_secrete_a_changer'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')
"""route pour la page a propos"""
@app.route('/about')
def about():
    return render_template('about.html')

"""route pour le formulaire d'ajout de tache"""
@app.route('/addTaskForm', methods=['GET', 'POST'])
def addTaskForm():
    form = TaskForm()
    
    if form.validate_on_submit():
        user_id= session.get('user_id')
        name = request.form['name']
        deadline = request.form['deadline']
        deadline = datetime.strptime(deadline, '%Y-%m-%d')
        new_task = Task(name=name, deadline=deadline, done=False, user_id=user_id)
        db.session.add(new_task)
        db.session.commit()
        flash("Nouvelle tâche ajoutée avec succès!")
        return redirect('/tasks')
    if form.errors:
        for error in form.errors.values():
            flash(f'Erreur: {error[0]}', 'danger')
    Tasks = Task.query.all()
    return render_template('addTaskForm.html', form=form, Tasks=Tasks)

"""route pour la liste de tâches"""
@app.route('/tasks')
def tasks():
    users_id = session.get('user_id')
    taches = Task.query.filter_by(user_id=users_id).all() if users_id else []
    return render_template('tasks.html',
     taches = taches)

"""route pour supprimer une tache"""
@app.route('/delete/<int:index>')
def delete(index):
    task = Task.query.get(index)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash(f"Tâche '{task.name}' supprimée !")
    return redirect('/tasks') 
@app.route('/modifier/<int:index>', methods=['GET', 'POST'])
def modifier(index):
    task = Task.query.get(index)
    form = update(obj=task)
    if form.validate_on_submit():
        task.name = form.name.data
        task.deadline = form.deadline.data
        task.done = form.done.data
        db.session.commit()
        flash(f"Tâche '{task.name}' modifiée !")
        return redirect('/tasks')
    return render_template('modifier.html', update=form)

"""route pour marquer comme terminée"""
@app.route('/toggle_done/<int:index>', methods=['POST'])
def toggle_done(index):
    task = Task.query.get(index)
    if task:
        task.done = True
        db.session.commit()
        flash(f"Tâche '{task.name}' mise à jour !")
    return redirect('/tasks')  # retourne à la liste des tâches

"""route pour se deconnecter"""
@app.route('/logout')
def logout():
    deconnect = session.pop('user_id', None)  # supprime l'utilisateur de la session
    if deconnect:
        flash("Vous êtes maintenant déconnecté.", "success")
    return redirect(url_for('home'))

"""route pour la page d'accueil de l'utilisateur"""
@app.route('/accueil')
def accueil():
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    tasks = Task.query.filter_by(user_id=user_id).all() if user_id else []
    current_user_id = session.get('user_id')
    autres_utilisateurs = User.query.filter(User.id != current_user_id).all()
    return render_template('accueil.html', user=user, tasks=tasks, others_users=autres_utilisateurs)

"""route pour enregistrer un utilisateur"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    rform = registerForm()
    if rform.validate_on_submit():
        hashed_mdp = generate_password_hash(rform.mdp.data)
        new_user = User(nom=rform.nom.data,
                         prenoms=rform.prenoms.data,
                         email=rform.email.data,
                         mdp=hashed_mdp,
                         sexe=rform.sexe.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Inscription réussie!", "success")
        return redirect(url_for('accueil'))
    users = User.query.all()
    return render_template('register.html', rform=rform, users=users)
"""route pour un utilisateur qui se connecte"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    lform = loginForm()
    user = None 
    if lform.validate_on_submit():
        user = User.query.filter_by(email=lform.email.data).first()
        if user and check_password_hash(user.mdp, lform.mdp.data):
            flash("Connexion réussie!", "success")
            session['user_id'] = user.id
            return redirect(url_for('accueil'))
        else:
            flash("Échec de la connexion. Vérifiez vos identifiants.", "danger")
    return render_template('login.html', lform=lform, user = user)
@app.route('/profil')
def profil():
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    return render_template('profil.html', user=user)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
=======
from flask import Flask, render_template, flash, redirect
from forms import TaskForm
app= Flask(__name__)
app.config['SECRET_KEY'] = 'une_cle_ultra_secrete_a_changer'
taches = []
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/addTaskForm', methods=['GET', 'POST'])
def addTaskForm():
    form = TaskForm()
    if form.validate_on_submit():
        flash("Nouvelle tâche ajoutée avec succès!")
        taches.append({
            'name': form.name.data,
            'deadline': form.deadline.data,
            'done' : form.done.data
        })
        return redirect('/tasks')
    if form.errors:
        for error in form.errors.values():
            flash(f'Erreur: {error[0]}', 'danger')
    return render_template('addTaskForm.html', form=form)
@app.route('/tasks')
def tasks():
    return render_template('tasks.html', taches=taches)
@app.route('/delete/<int:index>')
def delete(index):
    if index >= 0 and index < len(taches):
        del taches[index]
        flash("Tâche supprimée avec succès!")
    return redirect('/tasks') 
@app.route('/toggle_done/<int:index>', methods=['POST'])
def toggle_done(index):
    taches[index]['done'] = not taches[index]['done']  # inverse l'état
    flash(f"Tâche '{taches[index]['name']}' mise à jour !")
    return redirect('/tasks')  # retourne à la liste des tâches

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)
>>>>>>> 1cdae11572f267d8d04bb1999e4744b665ab772c
