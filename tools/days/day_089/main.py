from days.day_089.files.helpers import *


def day_089():
    title("DISAPPEARING TEXT (SESSIONS)")
    from flask import Flask, session, request, render_template_string

    app = Flask(__name__)
    app.secret_key = "your_secret_key"

    @app.route("/")
    def index():
        if "text" not in session:
            session["text"] = ""
        return render_template_string(
            """
			<!doctype html>
			<html lang="en">
			<head>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>Online Writing App</title>
				<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
				<script>
					$(document).ready(function() {
						var typingTimer;
						var doneTypingInterval = 2000;

						$('textarea').on('input', function() {
							clearTimeout(typingTimer);
							typingTimer = setTimeout(saveText, doneTypingInterval);
						});

						function saveText() {
							var text = $('textarea').val();
							$.ajax({
								url: '/save',
								type: 'POST',
								data: { text: text },
								success: function(response) {
									console.log('Text saved:', response);
								},
								error: function(error) {
									console.error('Error saving text:', error);
								}
							});
						}
					});
				</script>
			</head>
			<body>
				<textarea rows="10" cols="30">{{ session['text'] }}</textarea>
			</body>
			</html>
		"""
        )

    # Route for saving text
    @app.route("/save", methods=["POST"])
    def save_text():
        text = request.form["text"]
        session["text"] = text
        return "Text saved."

    @app.route("/load")
    def load_text():
        return session.get("text", "")

    if __name__ == "days.day_089.main":
        app.run(debug=True, use_reloader=False)
