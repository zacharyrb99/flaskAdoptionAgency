from forms import PetForm
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt' # Where is your database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Needs to be set to false
app.config['SQLALCHEMY_ECHO'] = True # Prints SQL statements to terminal (good for debugging)
app.config['SECRET_KEY'] = 'password'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = PetForm(active=True)

    if form.validate_on_submit():
        name=form.name.data
        species=form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data

        if form.available.data == 'True':
            available=True
        else:
            available=False

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_form.html', form=form)

@app.route('/details/<int:id>')
def show_pet_details(id):
    pet = Pet.query.get_or_404(id)
    return render_template('pet_details.html', pet=pet)
    
@app.route('/details/<int:id>/edit', methods=['GET', 'POST'])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name=form.name.data
        pet.species=form.species.data
        pet.photo_url=form.photo_url.data
        pet.age=form.age.data
        pet.notes=form.notes.data
        
        if form.available.data == 'True':
            pet.available=True
        else:
            pet.available=False

        db.session.commit()
        return redirect(f'/details/{id}')
    else:
        return render_template('edit_pet_form.html', form=form, pet=pet, id=id)


