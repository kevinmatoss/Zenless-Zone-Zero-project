from flask import Flask
from database import init_db
from routes.characters import characters_bp
from routes.items import items_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zzz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

app.register_blueprint(characters_bp, url_prefix='/api')
app.register_blueprint(items_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
