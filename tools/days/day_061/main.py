from days.day_061.files.helpers import *


def day_061():
    title("FLASK: ADVANCED FORMS")
    load_dotenv()
    template_folder_path = os.path.join(os.path.dirname(__file__), "files", "templates")
    static_folder_path = os.path.join(os.path.dirname(__file__), "files", "static")
    app = Flask(
        __name__, template_folder=template_folder_path, static_folder=static_folder_path
    )

    app.secret_key = os.getenv("SOME_SECRET_KEY_FOR_FLASK")
    bootstrap = Bootstrap5(app)

    class LoginForm(FlaskForm):
        email = StringField("Email", validators=[DataRequired()])
        password = PasswordField("Password", validators=[DataRequired()])
        submit = SubmitField(label="Log In")

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        login_form = LoginForm()
        if login_form.validate_on_submit():
            if (
                login_form.email.data == "admin@email.com"
                and login_form.password.data == "12345678"
            ):
                return render_template("success.html")
            else:
                return render_template("denied.html")
        return render_template("login.html", form=login_form)

    if __name__ == "days.day_061.main":
        app.run(debug=True, use_reloader=False)
