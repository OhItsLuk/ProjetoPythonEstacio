import os

from flask import Flask, redirect, url_for
from flask_cors import CORS

from app.routes.service_routes import service_bp
from app.routes.class_routes import class_bp
from app.routes.dashboard_routes import dashboard_bp
from app.routes.student_routes import student_bp
from app.routes.professional_routes import professional_bp
from app.routes.payment_routes import payment_bp

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

CORS(app)

app.register_blueprint(service_bp)
app.register_blueprint(class_bp)
app.register_blueprint(student_bp)
app.register_blueprint(professional_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(dashboard_bp)

@app.route("/")
def home():
    return redirect(url_for("dashboard.login"))

if __name__ == "__main__":
    app.run(debug=True)
