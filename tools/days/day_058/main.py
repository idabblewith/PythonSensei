from days.day_058.files.helpers import *


def day_058():
    title("FLASK: TINDOG")
    template_folder_path = os.path.join(os.path.dirname(__file__), "files", "templates")
    static_folder_path = os.path.join(os.path.dirname(__file__), "files", "static")
    app = Flask(
        __name__, template_folder=template_folder_path, static_folder=static_folder_path
    )

    @app.route("/")
    def home():
        return render_template("index.html")

    if __name__ == "days.day_058.main":
        app.run(debug=True, use_reloader=False)
