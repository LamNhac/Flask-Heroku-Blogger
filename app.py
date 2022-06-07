from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/tieu-su-ve-nguyen-ngoc-tu')
def blog1():
    return render_template('blog1.html')

@app.route('/blog/gioi-thieu-ve-flask')
def blog2():
    return render_template('blog2.html')

@app.route('/blog/nhung-ly-do-ma-ban-nen-su-dung-flask')
def blog3():
    return render_template('blog3.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404