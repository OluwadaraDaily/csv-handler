from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('routes', __name__)

@bp.route('/')
def hello():
  return 'Hello, World!'

@bp.route('/<name>')
def show(name):
  return f'<h1>{name}</h1>'

@bp.route('/upload', methods=["GET", "POST"])
def upload_csv():
  if request.method == 'POST':
    print(f'DATA ->{request.form}')
    print(f'FILE ->{request.files["csv-file"]}')
    print(f'REQUEST ->{request}')
    return redirect(url_for("routes.upload_csv"))
  else:
    return render_template("upload_csv.html")
    