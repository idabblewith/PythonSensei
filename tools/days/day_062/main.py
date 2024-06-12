from days.day_062.files.helpers import *


def day_062():
    title("FLASK: COFFEE AND WIFI")
    load_dotenv()
    template_folder_path = os.path.join(os.path.dirname(__file__), "files", "templates")
    static_folder_path = os.path.join(os.path.dirname(__file__), "files", "static")
    cafe_csv = os.path.join(os.path.dirname(__file__), "files", "cafe-data.csv")
    app = Flask(
        __name__, template_folder=template_folder_path, static_folder=static_folder_path
    )

    app.config["SECRET_KEY"] = os.getenv("SOME_SECRET_KEY_FOR_FLASK")
    Bootstrap5(app)

    class CafeForm(FlaskForm):
        cafe = StringField("Cafe name", validators=[DataRequired()])
        location = StringField(
            "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
        )
        open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
        close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
        coffee_rating = SelectField(
            "Coffee Rating",
            choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
            validators=[DataRequired()],
        )
        wifi_rating = SelectField(
            "Wifi Strength Rating",
            choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
            validators=[DataRequired()],
        )
        power_rating = SelectField(
            "Power Socket Availability",
            choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
            validators=[DataRequired()],
        )
        submit = SubmitField("Submit")

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/add", methods=["GET", "POST"])
    def add_cafe():
        form = CafeForm()
        if form.validate_on_submit():
            with open(cafe_csv, mode="a", encoding="utf-8") as csv_file:
                csv_file.write(
                    f"\n{form.cafe.data},"
                    f"{form.location.data},"
                    f"{form.open.data},"
                    f"{form.close.data},"
                    f"{form.coffee_rating.data},"
                    f"{form.wifi_rating.data},"
                    f"{form.power_rating.data}"
                )
            return redirect(url_for("cafes"))
        return render_template("add.html", form=form)

    @app.route("/cafes")
    def cafes():
        with open(cafe_csv, newline="", encoding="utf-8") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            list_of_rows = []
            for row in csv_data:
                list_of_rows.append(row)
        return render_template("cafes.html", cafes=list_of_rows)

    if __name__ == "days.day_062.main":
        app.run(debug=True, use_reloader=False)
