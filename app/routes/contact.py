from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Contact

bp = Blueprint('contact', __name__, url_prefix='/contacts')

@bp.route('/')
@login_required
def contacts():
    contatos = Contact.query.filter_by(user_id=current_user.id).all()
    return render_template('contacts.html', contatos=contatos)

@bp.route('/add', methods=['POST'])
@login_required
def add_contact():
    nome = request.form['nome']
    email = request.form['email']
    celular = request.form['celular']
    contato = Contact(nome=nome, email=email, celular=celular, user_id=current_user.id)
    db.session.add(contato)
    db.session.commit()
    return redirect(url_for('contact.contacts'))
