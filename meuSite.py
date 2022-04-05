from flask import Flask, render_template


app = Flask(__name__)

# @app.route('/')
# def homepage():
#     return render_template('home.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.errorhandler(404)
def page_not_found(error):
    return ('<h1>Ta usando Droga mizera <h1>'), 404

if __name__ =='__main__':
    app.run(debug=True)



