from delivery.ext.auth.form import UserForm
from delivery.ext.auth.controller import create_user, save_user_foto
from flask import Blueprint, current_app, redirect, render_template, request, url_for
bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    print("entrei na funcao main")
    current_app.logger.debug("Entrei na funcao main")
    return render_template("index.html")


@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")

@bp.route("/cadastro", methods=['GET', 'POST'])
def signup():
    form = UserForm()

    if form.validate_on_submit():
        create_user(form.email.data, form.password.data)
        # user = User()
        # form.populate_obj(user)
        # db.session.add(user)
        # db.session.commit()

        #forçar login
        foto = request.files.get('foto')
        if foto:
            save_user_foto(
                foto.filename,
                 foto
                )
        return redirect(url_for('site.index'))
    if request.method == "POST":
        __import__("ipdb").set_trace()

    return render_template("userform.html", form=form)

