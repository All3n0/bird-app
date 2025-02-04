import os
from flask import Flask,jsonify,make_response
from flask_restful import Api,Resource
from flask_migrate import Migrate
from models import db,Bird

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)

class Birds(Resource):
    def get(self):
        birds=[bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds),200)
class BirdsId(Resource):
    def get(self,bird_id):
        bird = Bird.query.get_or_404(bird_id)
        return make_response(jsonify(bird.to_dict()),200)
api.add_resource(BirdsId,'/birds/<int:bird_id>')
api.add_resource(Birds,'/birds')