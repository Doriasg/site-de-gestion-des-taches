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