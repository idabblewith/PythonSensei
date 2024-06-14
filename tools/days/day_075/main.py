from days.day_075.files.helpers import *


def day_075():
    title("PLOTTING APP STORE")
    # Show numeric output in decimal format e.g., 2.15
    pd.options.display.float_format = "{:,.2f}".format
    app_data = os.path.join(os.path.dirname(__file__), "files", "data", "apps.csv")
    df_apps = pd.read_csv(app_data)

    nls("================== BASE DATA AND CLEANING ==================")
    nls(f"SHAPE:\n{df_apps.shape}")
    nls(f"HEAD:\n{df_apps.head()}")
    nls(f"SAMPLE:\n{df_apps.sample(5)}")

    nls("DROPPING UNUSED...")
    df_apps.drop(["Last_Updated", "Android_Ver"], axis=1, inplace=True)
    nls(f"NEW HEAD:\n{df_apps.head()}")

    nls("DROPPING UNUSED...")
    nan_rows = df_apps[df_apps.Rating.isna()]
    nls(f"NEW SHAPE:\n{nan_rows.shape}")
    nls(f"NAN ROWS (HEAD):\n{nan_rows.head()}")

    nls("DROPPING NA...")
    df_apps_clean = df_apps.dropna()
    nls(f"NEW SHAPE:\n{df_apps_clean.shape}")

    nls("REMOVING DUPES...")
    duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
    nls(f"DUPLICATE ROWS SHAPE:\n{duplicated_rows.shape}")
    nls(f"DUPLICATE ROWS HEAD:\n{duplicated_rows.head()}")

    nls(f"INSTAGRAM BEFORE:\n{df_apps_clean[df_apps_clean.App == 'Instagram']}")
    df_apps_clean = df_apps_clean.drop_duplicates()
    nls(
        f"INSTAGRAM AFTER SIMPLE DROP:\n{df_apps_clean[df_apps_clean.App == 'Instagram']}"
    )
    df_apps_clean = df_apps_clean.drop_duplicates(subset=["App", "Type", "Price"])

    nls(
        f"INSTAGRAM AFTER SUBSET DROP:\n{df_apps_clean[df_apps_clean.App == 'Instagram']}"
    )

    nls(f"CLEAN SHAPE:\n{df_apps_clean.shape}")

    nls("================== HIGHEST RATED ==================")
    nls(f"{df_apps_clean.sort_values('Rating', ascending=False).head()}")

    nls("================== LARGEST ==================")
    nls(f"{df_apps_clean.sort_values('Size_MBs', ascending=False).head()}")

    nls("================== MOST REVIEWS ==================")
    nls(f"{df_apps_clean.sort_values('Reviews', ascending=False).head(50)}")

    nls("================== PLOTLY TIME! ==================")
    ratings = df_apps_clean.Content_Rating.value_counts()
    nls(ratings)

    # # PIE
    # fig = px.pie(
    #     labels=ratings.index,
    #     values=ratings.values,
    #     title="Content Rating",
    #     names=ratings.index,
    # )
    # fig.update_traces(textposition="outside", textinfo="percent+label")

    # fig.show()

    # DONUT
    fig = px.pie(
        labels=ratings.index,
        values=ratings.values,
        title="Content Rating",
        names=ratings.index,
        hole=0.6,  # makes a donut chart =)
    )
    fig.update_traces(textposition="inside", textfont_size=15, textinfo="percent")

    fig.show()

    nls("================== NUM INSTALLS ==================")
    nls(f"Description:\n{df_apps_clean.Installs.describe()}")
    nls(f"Info:\n{df_apps_clean.info()}")
    # Installs of data type object because of the comma (,) character
    nls(
        f"Grouped by installs count{df_apps_clean[['App', 'Installs']].groupby('Installs').count()}"
    )

    print("Removing any commas, and converting to numerals")
    df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(",", "")
    df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)

    nls(f"UPDATED:\n{df_apps_clean[['App', 'Installs']].groupby('Installs').count()}")

    nls("================== CLEANED MOST EXPENSIVE APPS ==================")
    df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace("$", "")
    df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)

    nls(
        f"CLEANED & SORTED BY PRICE (HEAD):\n{df_apps_clean.sort_values('Price', ascending=False).head(20)}"
    )

    nls("================== CLEANED MOST EXPENSIVE (UNDER $250) ==================")
    df_apps_clean = df_apps_clean[df_apps_clean["Price"] < 250]

    nls(
        f"CLEANED & SORTED BY PRICE (HEAD):\n{df_apps_clean.sort_values('Price', ascending=False).head(5)}"
    )

    nls("================== Highest Grossing Paid Apps ==================")
    df_apps_clean["Revenue_Estimate"] = df_apps_clean.Installs.mul(df_apps_clean.Price)
    nls(
        f"Revenue Est.:\n{df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10]}"
    )

    nls("================== Plotly App Categories ==================")
    # # Number of different categories
    # df_apps_clean.Category.nunique()
    # # Number of apps per category
    # top10_category = df_apps_clean.Category.value_counts()[:10]
    # nls(f"TOP 10 Categories:\n{top10_category}")
    # bar = px.bar(
    #     x=top10_category.index, y=top10_category.values  # index = category name
    # )

    # bar.show()

    # Group apps by category and then sum the number of installations
    category_installs = df_apps_clean.groupby("Category").agg(
        {"Installs": pd.Series.sum}
    )
    category_installs.sort_values("Installs", ascending=True, inplace=True)

    # category popularity
    h_bar = px.bar(
        x=category_installs.Installs,
        y=category_installs.index,
        orientation="h",
        title="Category Popularity",
    )

    h_bar.update_layout(xaxis_title="Number of Downloads", yaxis_title="Category")
    h_bar.show()

    # Category Concentration - Downloads vs. Competition
    cat_number = df_apps_clean.groupby("Category").agg({"App": pd.Series.count})
    cat_merged_df = pd.merge(cat_number, category_installs, on="Category", how="inner")
    print(f"The dimensions of the DataFrame are: {cat_merged_df.shape}")
    cat_merged_df.sort_values("Installs", ascending=False)

    scatter = px.scatter(
        cat_merged_df,  # data
        x="App",  # column name
        y="Installs",
        title="Category Concentration",
        size="App",
        hover_name=cat_merged_df.index,
        color="Installs",
    )

    scatter.update_layout(
        xaxis_title="Number of Apps (Lower=More Concentrated)",
        yaxis_title="Installs",
        yaxis=dict(type="log"),
    )

    scatter.show()

    nls("================== Extracting Nested Data from a Column ==================")
    # Number of Genres?
    len(df_apps_clean.Genres.unique())

    # # Problem: Have multiple categories seperated by ;
    # nls(
    # 	f"Unique Genres Count\n{df_apps_clean.Genres.value_counts().sort_values(ascending=True)[:5]}"
    # )

    # Split the strings on the semi-colon and then .stack them.
    stack = df_apps_clean.Genres.str.split(";", expand=True).stack()
    nls(f"We now have a single column with shape: {stack.shape}")
    num_genres = stack.value_counts()
    nls(f"Number of genres: {len(num_genres)}")

    nls("================== Plotly Colour Scales ==================")
    bar = px.bar(
        x=num_genres.index[:15],  # index = category name
        y=num_genres.values[:15],  # count
        title="Top Genres",
        hover_name=num_genres.index[:15],
        color=num_genres.values[:15],
        color_continuous_scale="Agsunset",
    )

    bar.update_layout(
        xaxis_title="Genre", yaxis_title="Number of Apps", coloraxis_showscale=False
    )

    bar.show()

    nls("================== Plotly Grouped Bar Charts ==================")
    nls(f"Type Value Counts:{df_apps_clean.Type.value_counts()}")
    df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg(
        {"App": pd.Series.count}
    )
    df_free_vs_paid.sort_values("App")

    g_bar = px.bar(
        df_free_vs_paid,
        x="Category",
        y="App",
        title="Free vs Paid Apps by Category",
        color="Type",
        barmode="group",
    )

    g_bar.update_layout(
        xaxis_title="Category",
        yaxis_title="Number of Apps",
        xaxis={"categoryorder": "total descending"},
        yaxis=dict(type="log"),
    )

    g_bar.show()

    nls(
        "================== Plotly Box Plots: Lost Downloads for Paid Apps =================="
    )
    box = px.box(
        df_apps_clean,
        y="Installs",
        x="Type",
        color="Type",
        notched=True,
        points="all",
        title="How Many Downloads are Paid Apps Giving Up?",
    )

    box.update_layout(yaxis=dict(type="log"))

    box.show()

    nls(
        "================== Plotly Box Plots: Revenue by App Category =================="
    )
    df_paid_apps = df_apps_clean[df_apps_clean["Type"] == "Paid"]
    box = px.box(
        df_paid_apps,
        x="Category",
        y="Revenue_Estimate",
        title="How Much Can Paid Apps Earn?",
    )

    box.update_layout(
        xaxis_title="Category",
        yaxis_title="Paid App Ballpark Revenue",
        xaxis={"categoryorder": "min ascending"},
        yaxis=dict(type="log"),
    )

    box.show()

    nls("================== Plotly Pricing Strategies ==================")
    nls(f"Median Price:\n{df_paid_apps.Price.median()}")
    box = px.box(df_paid_apps, x="Category", y="Price", title="Price per Category")

    box.update_layout(
        xaxis_title="Category",
        yaxis_title="Paid App Price",
        xaxis={"categoryorder": "max descending"},
        yaxis=dict(type="log"),
    )

    box.show()
