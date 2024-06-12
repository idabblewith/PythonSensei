from days.day_059.files.helpers import *


def day_059():
    title("FLASK: BASIC BLOG 2")
    template_folder_path = os.path.join(os.path.dirname(__file__), "files", "templates")
    static_folder_path = os.path.join(os.path.dirname(__file__), "files", "static")
    app = Flask(
        __name__, template_folder=template_folder_path, static_folder=static_folder_path
    )

    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

    @app.route("/")
    def get_all_posts():
        return render_template("index.html", all_posts=posts)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/post/<int:index>")
    def show_post(index):
        requested_post = None
        for blog_post in posts:
            if blog_post["id"] == index:
                requested_post = blog_post
        return render_template("post.html", post=requested_post)

    if __name__ == "days.day_059.main":
        app.run(debug=True, use_reloader=False)
