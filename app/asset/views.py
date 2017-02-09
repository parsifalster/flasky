from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import asset
from .. import db
from ..models import User,Asset
from ..email import send_email
from .forms import AssetForm





@asset.route('/new',methods=['GET','POST'])
@login_required
def new():
    name = None
    form = AssetForm()
    if form.validate_on_submit():
        asset = Asset(name = form.name.data,
                      cart = form.cart.data,
                      desc = form.desc.data)
        db.session.add(asset)
        db.session.commit()
        return redirect(url_for('.list'))
    else:
        return render_template('asset/new.html',form=form)

@asset.route('/list',methods=['GET'])
@login_required
def list():
    return render_template('asset/list.html')

