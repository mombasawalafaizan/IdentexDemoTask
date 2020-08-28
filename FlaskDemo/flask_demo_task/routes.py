from flask import render_template, url_for, flash, redirect, request
from flask_demo_task.models import User
from flask_demo_task.forms import CreateUser
from flask_demo_task import app, db

# Home page
@app.route("/")
@app.route('/home')
def home():
    return render_template('layout.html')

# Creating user
@app.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateUser()
    if form.validate_on_submit():
        flash(f'User {form.name.data} successfully added!', 'success')
        user = User(name=form.name.data, email=form.email.data, mobile_no=form.mobile_no.data, company = form.company.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create.html', title='Create User', form=form)

# List users
@app.route('/list')
def list_users():
    users = User.query.all()
    return render_template('list.html', title='List Users', users = users)

# Delete users
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        # Fetch form data
        details = request.form
        get_email = details['email']
        record = User.query.filter_by(email=get_email).first()
        if record:
            db.session.delete(record)
            db.session.commit()
            flash('Record deleted successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('No record with such email found.', 'danger')
            return redirect(url_for('home'))
    return render_template('delete.html')


# Update users
# Please note that I have not implemented this correctly
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        # Fetch form data
        details = request.form
        get_email = details['email']
        record = User.query.filter_by(email=get_email).first()
        if record:
            db.session.delete(record)
            db.session.commit()
            return render_template('update.html', title='Update entry', record=record)
        
    form = CreateUser()
    if form.validate_on_submit():
        flash(f'Record successfully updated!', 'success')
        user = User(name=form.name.data, email=form.email.data, mobile_no=form.mobile_no.data, company = form.company.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
        #flash('No record with the give email found. Please try again.', 'danger')
    return render_template('update.html')
