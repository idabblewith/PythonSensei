from days.day_057.files.helpers import *


def day_057():
    title("FLASK: BASIC BLOG")
    template_folder_path = os.path.join(os.path.dirname(__file__), "files", "templates")
    static_folder_path = os.path.join(os.path.dirname(__file__), "files", "static")
    app = Flask(
        __name__, template_folder=template_folder_path, static_folder=static_folder_path
    )
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts_data = res.json()

    post_objects = []
    for post in posts_data:
        post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        post_objects.append(post_obj)

    @app.route("/")
    def get_all_posts():
        return render_template("index.html", all_posts=post_objects)

    @app.route("/post/<int:index>")
    def show_post(index):
        requested_post = None
        for blog_post in post_objects:
            if blog_post.id == index:
                requested_post = blog_post
        return render_template("post.html", post=requested_post)

    if __name__ == "days.day_057.main":
        app.run(debug=True, use_reloader=False)
