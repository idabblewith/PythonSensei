import os
import time
from days.day_092.files.helpers import *
from days.day_092.files.scraper import scrape_data


def day_092():
    title("CUSTOM WEB SCRAPER")
    from flask import Flask, render_template

    template_folder_path = os.path.join(os.path.dirname(__file__), "files", "templates")
    app = Flask(
        __name__,
        template_folder=template_folder_path,
    )

    # Define a route to scrape data and render it in a template
    @app.route("/")
    def index():
        # URL of the website to scrape
        url = "https://www.news.com.au"

        # Scrape data using the scraper function
        scraped_data = scrape_data(url)
        print(scraped_data)

        time.sleep(2)

        # Render the HTML template with the scraped data (replicatuon of the website)
        return render_template("index.html", data=scraped_data)

    if __name__ == "days.day_092.main":
        app.run(debug=True, use_reloader=False)
