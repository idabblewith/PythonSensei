from days.day_068.files.helpers import *


def day_068():
    title("BLOG: AUTHENTICATION")
    template_folder_path = os.path.join(os.path.dirname(__file__), "files", "templates")
    static_folder_path = os.path.join(os.path.dirname(__file__), "files", "static")
    app = Flask(
        __name__, template_folder=template_folder_path, static_folder=static_folder_path
    )
    load_dotenv()
    app.config["SECRET_KEY"] = os.getenv("SOME_SECRET_KEY_FOR_FLASK")

    # CREATE DATABASE
    class Base(DeclarativeBase):
        pass

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    db = SQLAlchemy(model_class=Base)
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.get_or_404(User, user_id)

    # CREATE TABLE
    class User(UserMixin, db.Model):
        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        email: Mapped[str] = mapped_column(String(100), unique=True)
        password: Mapped[str] = mapped_column(String(100))
        name: Mapped[str] = mapped_column(String(1000))

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return render_template("index.html", logged_in=current_user.is_authenticated)

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":

            email = request.form.get("email")
            result = db.session.execute(db.select(User).where(User.email == email))

            # Note, email in db is unique so will only have one result.
            user = result.scalar()
            if user:
                # User already exists
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for("login"))

            hash_and_salted_password = generate_password_hash(
                request.form.get("password"), method="pbkdf2:sha256", salt_length=8
            )
            new_user = User(
                email=request.form.get("email"),
                password=hash_and_salted_password,
                name=request.form.get("name"),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets"))

        return render_template("register.html", logged_in=current_user.is_authenticated)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            result = db.session.execute(db.select(User).where(User.email == email))
            user = result.scalar()
            # Email doesn't exist or password incorrect.
            if not user:
                flash("That email does not exist, please try again.")
                return redirect(url_for("login"))
            elif not check_password_hash(user.password, password):
                flash("Password incorrect, please try again.")
                return redirect(url_for("login"))
            else:
                login_user(user)
                return redirect(url_for("secrets"))

        return render_template("login.html", logged_in=current_user.is_authenticated)

    @app.route("/secrets")
    @login_required
    def secrets():
        print(current_user.name)
        return render_template("secrets.html", name=current_user.name, logged_in=True)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("home"))

    @app.route("/download")
    @login_required
    def download():
        # return send_from_directory('/static/files/', 'cheat_sheet.pdf')
        return send_from_directory("files", path="static/files/cheat_sheet.pdf")

    if __name__ == "days.day_068.main":
        app.run(debug=True, use_reloader=False)
