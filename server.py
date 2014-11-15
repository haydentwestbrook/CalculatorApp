## Alec Davidson
## Hayden Westbrook
## Quentin Kantaris
import flask
import flask.views
from calculator.parser import printer

app = flask.Flask(__name__)
app.secret_key = "DavidsonWestbrookKantaris"

class View(flask.views.MethodView):
  def get(self):
    return flask.render_template('index.html')

  def post(self):
    equation = flask.request.form['equation']

    printer(equation)
    return self.get()
  
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])


