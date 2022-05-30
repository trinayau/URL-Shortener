from flask import render_template, request, redirect

from core import app, db
from core.models import Link

@app.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()

    link.visits = link.visits + 1
    db.session.commit()
    return redirect(link.original_url)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_link', methods=['POST'])
def add_link():
    original_url = request.form['original_url']
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()

    return render_template('link_added.html', new_link=link.short_url, original_url=link.original_url)

@app.route('/stats')
def stats():
    links = Link.query.all()

    return render_template('stats.html', links=links)


@app.errorhandler(404)
def page_not_found(e):
    return '404', 404
