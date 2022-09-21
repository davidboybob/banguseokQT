from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from apps.models.models import QueitTimeNote
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html')


@views.route('/create-note', methods=['POST'])
def create_note():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('내용을 작성해 주세요.', category='error')

        else:
            new_note = QueitTimeNote(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = QueitTimeNote.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})