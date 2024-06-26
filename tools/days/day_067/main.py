from days.day_067.files.helpers import *


def day_067():
    title("BLOG: REST API/CKEDITOR")
    template_folder_path = os.path.join(os.path.dirname(__file__), "files", "templates")
    static_folder_path = os.path.join(os.path.dirname(__file__), "files", "static")
    app = Flask(
        __name__, template_folder=template_folder_path, static_folder=static_folder_path
    )
    load_dotenv()
    app.config["SECRET_KEY"] = os.getenv("SOME_SECRET_KEY_FOR_FLASK")
    ckeditor = CKEditor(app)
    Bootstrap5(app)

    # CREATE DATABASE
    class Base(DeclarativeBase):
        pass

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
    db = SQLAlchemy(model_class=Base)
    db.init_app(app)

    # CONFIGURE TABLE
    class BlogPost(db.Model):
        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
        subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
        date: Mapped[str] = mapped_column(String(250), nullable=False)
        body: Mapped[str] = mapped_column(Text, nullable=False)
        author: Mapped[str] = mapped_column(String(250), nullable=False)
        img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    with app.app_context():
        db.create_all()

    # WTForm
    class CreatePostForm(FlaskForm):
        title = StringField("Blog Post Title", validators=[DataRequired()])
        subtitle = StringField("Subtitle", validators=[DataRequired()])
        author = StringField("Your Name", validators=[DataRequired()])
        img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
        body = CKEditorField("Blog Content", validators=[DataRequired()])
        submit = SubmitField("Submit Post")

    @app.route("/")
    def get_all_posts():
        result = db.session.execute(db.select(BlogPost))
        posts = result.scalars().all()
        return render_template("index.html", all_posts=posts)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    # POSTS ===================================================

    @app.route("/new-post", methods=["GET", "POST"])
    def add_new_post():
        form = CreatePostForm()
        if form.validate_on_submit():
            new_post = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                body=form.body.data,
                img_url=form.img_url.data,
                author=form.author.data,
                date=date.today().strftime("%B %d, %Y"),
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("get_all_posts"))
        return render_template("make-post.html", form=form)

    @app.route("/post/<int:post_id>")
    def show_post(post_id):
        requested_post = db.get_or_404(BlogPost, post_id)
        return render_template("post.html", post=requested_post)

    @app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
    def edit_post(post_id):
        post = db.get_or_404(BlogPost, post_id)
        edit_form = CreatePostForm(
            title=post.title,
            subtitle=post.subtitle,
            img_url=post.img_url,
            author=post.author,
            body=post.body,
        )
        if edit_form.validate_on_submit():
            post.title = edit_form.title.data
            post.subtitle = edit_form.subtitle.data
            post.img_url = edit_form.img_url.data
            post.author = edit_form.author.data
            post.body = edit_form.body.data
            db.session.commit()
            return redirect(url_for("show_post", post_id=post.id))
        return render_template("make-post.html", form=edit_form, is_edit=True)

    @app.route("/delete/<int:post_id>")
    def delete_post(post_id):
        post_to_delete = db.get_or_404(BlogPost, post_id)
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    if __name__ == "days.day_067.main":
        app.run(debug=True, use_reloader=False)
