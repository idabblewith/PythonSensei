from days.day_088.files.helpers import *


def day_088():
    title("TODO LIST")
    import os
    from flask import Flask, render_template, request, redirect, url_for
    from flask_sqlalchemy import SQLAlchemy

    db = SQLAlchemy()

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
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos88.db"

        # Initialize SQLAlchemy with the app
        db.init_app(app)

        return app

    app = create_app()

    # Create a Todo model
    class Todo(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        content = db.Column(db.String(200), nullable=False)
        completed = db.Column(db.Boolean, default=False)

    with app.app_context():
        # Create the database tables within the application context
        db.create_all()

    # Routes
    @app.route("/")
    def index():
        todos = Todo.query.all()
        return render_template("index.html", todos=todos)

    @app.route("/add", methods=["POST"])
    def add_todo():
        content = request.form["content"]
        new_todo = Todo(content=content)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("index"))

    @app.route("/complete/<int:todo_id>")
    def complete(todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.completed = True
        db.session.commit()
        return redirect(url_for("index"))

    @app.route("/delete/<int:todo_id>")
    def delete(todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("index"))

    if __name__ == "days.day_088.main":
        app.run(debug=True, use_reloader=False)
