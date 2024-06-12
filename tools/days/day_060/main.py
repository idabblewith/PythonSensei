from days.day_060.files.helpers import *


def day_060():
    title("FLASK: FORMS AND REQUESTS")
    template_folder_path = os.path.join(os.path.dirname(__file__), "files", "templates")
    static_folder_path = os.path.join(os.path.dirname(__file__), "files", "static")
    app = Flask(
        __name__, template_folder=template_folder_path, static_folder=static_folder_path
    )

    load_dotenv()
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")
    RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

    def send_email(name, email, phone, message):
        email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(SENDER_EMAIL, GOOGLE_APP_PASSWORD)
            connection.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, email_message)

    @app.route("/")
    def get_all_posts():
        return render_template("index.html", all_posts=posts)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact", methods=["GET", "POST"])
    def contact():
        if request.method == "POST":
            data = request.form
            send_email(data["name"], data["email"], data["phone"], data["message"])
            return render_template("contact.html", msg_sent=True)
        return render_template("contact.html", msg_sent=False)

    @app.route("/post/<int:index>")
    def show_post(index):
        requested_post = None
        for blog_post in posts:
            if blog_post["id"] == index:
                requested_post = blog_post
        return render_template("post.html", post=requested_post)

    if __name__ == "days.day_060.main":
        app.run(debug=True, use_reloader=False)
