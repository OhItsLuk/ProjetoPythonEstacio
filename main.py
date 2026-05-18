from flask import Flask
from flask_cors import CORS

from app.routes.service_routes import service_bp
from app.routes.class_routes import class_bp
from app.routes.student_routes import student_bp
from app.routes.professional_routes import professional_bp
from app.routes.payment_routes import payment_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(service_bp)
app.register_blueprint(class_bp)
app.register_blueprint(student_bp)
app.register_blueprint(professional_bp)
app.register_blueprint(payment_bp)

@app.route("/")
def home():
    return {
        "message": "API ONG funcionando!"
    }

if __name__ == "__main__":
    app.run(debug=True)