## Alec Davidson
## Hayden Westbrook
## Quentin Kantaris
import flask, flask.views, os

app = flask.Flask(__name__)

class View(flask.views.MethodView):
  def get(self):
    return flask.render_template('index.html')
  
  @property
  def post(self):
    
    return self.get()
  
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])


