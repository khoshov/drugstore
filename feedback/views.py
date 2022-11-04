from flask import Blueprint, redirect, render_template

from extensions import db
from feedback.forms import FeedbackForm
from feedback.models import Feedback

blueprint = Blueprint('feedback_form', __name__, url_prefix='/feedback', static_folder='../static')


@blueprint.route('/', methods=['GET', 'POST'])
def form_page():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback(
            email=form.email.data,
            text=form.text.data,
        )
        db.session.add(feedback)
        db.session.commit()
        return redirect('/feedback/success')
    return render_template('feedback.html', form=form)


@blueprint.route('/success')
def success():
    return render_template('feedback_success.html')
