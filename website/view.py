#Pages the user can navigate to

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Account
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/delete-acc', methods=['POST'])
def delete_node():
    acc = json.loads(request.data)
    acc_phone = acc['phoneNumb']
    acc= Account.query.get(acc_phone)
    if acc:
        if acc.user_id == current_user.id:
            db.session.delete(acc)
            db.session.commit()
    
    return jsonify({})

@views.route('/add-account', methods=['GET', 'POST'])
def add_account():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')
        notes = request.form.get('notes')

        if len(name) < 1:
            flash("Business name too short", category='error')
        elif len(phone) < 9:
            flash("Phone Number is required!")
        else:
            new_acc = Account(phone=phone, name=name, address=address, notes=notes, user_id=current_user.id)
            db.session.add(new_acc)
            db.session.commit()
            flash("Account added", category="success")

        return render_template("home.html", user=current_user)
    else:
        return render_template("add_account.html", user=current_user)

