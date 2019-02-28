from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author':'Corey Schafer',
        'title':'blog1',
        'content':'content1',
        'date':'april',
    },
       {
        'author':'Abhrham Linclo',
        'title':'blog2',
        'content':'content2',
        'date':'may',
    }
]

#routes using a decorator
# / is root page  
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, )

@app.route('/about')
def about():
    return render_template('about.html',title='about')

if __name__ == '__main__':
    app.run(debug=True)