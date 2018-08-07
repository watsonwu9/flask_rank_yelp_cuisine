# from sqlalchemy import create_engine,MetaData,Table
# from sqlalchemy import Column, Text, Integer, String,Float
# from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,request,redirect,url_for
from wtforms import Form, SelectField


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////Users/IAN/Desktop/uiuc/DMC/task4/Flask/cuisines.db'
db = SQLAlchemy(app)
#app.debug = True

class Cuisine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.Integer)
    dish = db.Column(db.String(60))
    name = db.Column(db.String(80))
    count = db.Column(db.Float)
    stars = db.Column(db.Float)
    full_address = db.Column(db.String(250))

    def __repr__(self):
        return self.dish + self.name

class DishForm(Form):
    choices =  [('chow mein','chow mein'),
                ('xiaolongbao','xiaolongbao'),
                ('chicken rice','chicken rice'),
                ('tsao\'s chicken','tsao\'s chicken'),
                ('peking duck','peking duck'),
                ('wonton strips','wonton strips'),
                ('soy milk','soy milk'),
                ('chinese chicken salad','chinese chicken salad'),
                ('dim sum','dim sum'),
                ('brown rice','brown rice'),
                ('general chicken','general chicken'),
                ('beef chow fun','beef chow fun'),
                ('bubble tea','bubble tea'),
                ('sesame chicken','sesame chicken'),
                ('char siu','char siu'),
                ('egg drop soup','egg drop soup'),
                ('roast duck','roast duck'),
                ('chicken fried rice','chicken fried rice'),
                ('Peking duck','Peking duck'),
                ('egg foo young','egg foo young'),
                ('bean sprouts','bean sprouts'),
                ('chicken lettuce wraps','chicken lettuce wraps'),
                ('dumplings','dumplings'),
                ('steamed buns','steamed buns'),
                ('chop suey','chop suey'),
                ('mapo tofu','mapo tofu'),
                ('fish ball','fish ball'),
                ('spring roll','spring roll'),
                ('rice chicken','rice chicken'),
                ('lotus root','lotus root'),
                ('rice noodle','rice noodle'),
                ('frog legs','frog legs'),
                ('egg roll','egg roll'),
                ('tom yum','tom yum'),
                ('wonton','wonton'),
                ('lo mein','lo mein'),
                ('beef rice','beef rice'),
                ('lobster','lobster'),
                ('shrimp','shrimp'),
                ('chicken soup','chicken soup'),
                ('chicken wings','chicken wings'),
                ('kung pao chicken','kung pao chicken'),
                ('wonton soup','wonton soup'),
                ('dandan noodles','dandan noodles'),
                ('tomato soup','tomato soup'),
                ('hainanese chicken rice','hainanese chicken rice'),
                ('cong you bing','cong you bing'),
                ('hot pot','hot pot'),
                ('bok choy','bok choy')]





    select = SelectField('', choices=choices)


@app.route('/',methods=['POST','GET'])
def index():
    search = DishForm(request.form)
    if request.method == 'POST':
        allCuisine = Cuisine.query.filter_by(dish=search.select.data).all()
        #return render_template("form.html",allCuisine = allCuisine,form=search)
    else:
        allCuisine = Cuisine.query.all()
        #return render_template("form.html",allCuisine = allCuisine,form=search)
    table = Results(allCuisine)
    table.border = True
    return render_template("form.html",table = table,form=search)

from flask_table import Table, Col
class Results(Table):
    id = Col('id', show=False)
    ranking = Col('Ranking')
    name = Col('Cuisine')
    stars = Col('Stars')
    full_address = Col('Address')



if __name__ == '__main__':
    app.run()

