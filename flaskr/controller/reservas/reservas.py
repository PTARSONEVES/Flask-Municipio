import functools
from datetime import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from ...database.db import get_db
from ...forms.reservas.preresform import FormPreres

bp = Blueprint('reservas', __name__, url_prefix='/reservas')

@bp.route('/prereserva',methods=['GET','POST'])
def prereserva():
    form = FormPreres()
    error=None
    if request.method == 'POST':
        print('usando1')
        if form.validate_on_submit():
            username=form.usuario.data
            email=form.email.data
            checkin=form.checkin.data
            checkout=form.checkout.data
            hspadulto=form.hspadulto.data
            hspcrianca=form.hspcrianca.data
            print('username: ',username)
            print('email: ',email)
            criacao=datetime.now()
            db=get_db()
            try:
                query = ("SELECT * FROM user where email=%s;")
                db.execute(query,(email))
                user=db.fetchone()
                if user is None:
                    query = ("INSERT INTO user (username, class_id, email, email_confirmed, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)")
                    db.execute(query,(username,3,email,0,criacao,criacao))
                db.execute(query,(email))
                user=db.fetchone()
                user_id=user["id"]
                username=user["username"]
            except:
                query("INSERT INTO user (username, class_id, email, email_confirmed, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)")
                db.execute(query,(username,3,email,0,criacao,criacao))
        if form.errors != {}:
            for err in form.errors.values():
                flash(f"Erros ao preencher formulário {err}", category="danger")
    return render_template('reservas/prereserva.html',form=form)