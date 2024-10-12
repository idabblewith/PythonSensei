from days.day_087.files.helpers import *


def day_087():
    title("CAFE AND WIFI")

    # MOdels
    from flask_sqlalchemy import SQLAlchemy
    from flask import Flask, redirect, url_for, render_template, request
    import os

    db = SQLAlchemy()

    class Cafe(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        address = db.Column(db.String(200), nullable=False)
        wifi = db.Column(db.Boolean, default=False)
        power = db.Column(db.Boolean, default=False)

    # App
    def create_app():
        template_folder_path = os.path.join(
            os.path.dirname(__file__), "files", "templates"
        )
        # static_folder_path = os.path.join(os.path.dirname(__file__), "files", "static")
        app = Flask(
            __name__,
            template_folder=template_folder_path,
            # static_folder=static_folder_path,
        )
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes87.db"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        db.init_app(app)

        with app.app_context():
            db.create_all()

        return app

    # Routes

    app = create_app()

    @app.route("/")
    def index():
        cafes = Cafe.query.all()
        return render_template("index.html", cafes=cafes)

    @app.route("/add", methods=["GET", "POST"])
    def add_cafe():
        if request.method == "POST":
            name = request.form["name"]
            address = request.form["address"]
            wifi = "wifi" in request.form
            power = "power" in request.form

            new_cafe = Cafe(name=name, address=address, wifi=wifi, power=power)
            db.session.add(new_cafe)
            db.session.commit()

            return redirect(url_for("index"))

        return render_template("add_cafe.html")

    if __name__ == "days.day_087.main":
        app.run(debug=True, use_reloader=False)
