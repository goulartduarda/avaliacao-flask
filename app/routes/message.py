from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Message, Contact

bp = Blueprint('message', __name__, url_prefix='/messages')

@bp.route('/')
@login_required
def messages():
    mensagens = Message.query.filter_by(user_id=current_user.id).all()
    contatos = Contact.query.filter_by(user_id=current_user.id).all()
    return render_template('messages.html', mensagens=mensagens, contatos=contatos)

@bp.route('/send', methods=['POST'])
@login_required
def send_message():
    titulo = request.form['titulo']
    texto = request.form['texto']
    contato_id = request.form['contato']
    mensagem = Message(titulo=titulo, texto=texto, user_id=current_user.id, contact_id=contato_id)
    db.session.add(mensagem)
    db.session.commit()
    return redirect(url_for('message.messages'))
