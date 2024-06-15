from days.day_077.files.helpers import *


def day_077():
    title("LINEAR REG. & SEABORN")
    raw_file = os.path.join(
        os.path.dirname(__file__), "files", "cost_revenue_dirty.csv"
    )
    data = pd.read_csv(raw_file)
    # Presentation
    pd.options.display.float_format = "{:,.2f}".format

    from pandas.plotting import register_matplotlib_converters

    register_matplotlib_converters()

    # Preliminary exploration
    data.shape
    data.sample(5)
    data.tail()
    print(f"Any NaN values among the data? {data.isna().values.any()}")
    print(f"Any duplicates? {data.duplicated().values.any()}")

    duplicated_rows = data[data.duplicated()]
    print(f"Number of duplicates: {len(duplicated_rows)}")
    # Show NaN values and data types per column
    data.info()

    # Conversion to numerals of usd budgets
    chars_to_remove = [",", "$"]
    columns_to_clean = [
        "USD_Production_Budget",
        "USD_Worldwide_Gross",
        "USD_Domestic_Gross",
    ]

    for col in columns_to_clean:
        for char in chars_to_remove:
            # Replace each character with an empty string
            data[col] = data[col].astype(str).str.replace(char, "")
        # Convert column to a numeric data type
        data[col] = pd.to_numeric(data[col])

    data.head()
    data.Release_Date = pd.to_datetime(data.Release_Date)
    data.head()
    data.info()

    # Descriptive statistics
    data.describe()
    data[data.USD_Production_Budget == 1100.00]
    data[data.USD_Production_Budget == 425000000.00]

    # zero rev
    zero_domestic = data[data.USD_Domestic_Gross == 0]
    print(f"Number of films that grossed $0 domestically {len(zero_domestic)}")
    zero_domestic.sort_values("USD_Production_Budget", ascending=False)

    # zero ww
    zero_worldwide = data[data.USD_Worldwide_Gross == 0]
    print(f"Number of films that grossed $0 worldwide {len(zero_worldwide)}")
    zero_worldwide.sort_values("USD_Production_Budget", ascending=False)

    # itl releases
    international_releases = data.loc[
        (data.USD_Domestic_Gross == 0) & (data.USD_Worldwide_Gross != 0)
    ]
    print(f"Number of international releases: {len(international_releases)}")
    international_releases.head()

    # same thing but with .query() to get itl release 0 us some rev ww
    international_releases = data.query(
        "USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0"
    )
    print(f"Number of international releases: {len(international_releases)}")
    international_releases.tail()

    # unreleased
    # Date of Data Collection
    scrape_date = pd.Timestamp("2018-5-1")
    future_releases = data[data.Release_Date >= scrape_date]
    print(f"Number of unreleased movies: {len(future_releases)}")
    future_releases

    # exclude future releases
    data_clean = data.drop(future_releases.index)
    data.shape[0] - data_clean.shape[0]

    # Films that lost money
    money_losing = data_clean.loc[
        data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross
    ]
    len(money_losing) / len(data_clean)

    # money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
    # money_losing.shape[0]/data_clean.shape[0]

    # SEABORN
    plt.figure(figsize=(8, 4), dpi=200)

    ax = sns.scatterplot(
        data=data_clean, x="USD_Production_Budget", y="USD_Worldwide_Gross"
    )

    ax.set(
        ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel="Revenue in $ billions",
        xlabel="Budget in $100 millions",
    )

    plt.show()

    plt.figure(figsize=(8, 4), dpi=200)
    ax = sns.scatterplot(
        data=data_clean,
        x="USD_Production_Budget",
        y="USD_Worldwide_Gross",
        hue="USD_Worldwide_Gross",  # change colour
        size="USD_Worldwide_Gross",
    )  # change size of dot

    ax.set(
        ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel="Revenue in $ billions",
        xlabel="Budget in $100 millions",
    )

    plt.show()

    plt.figure(figsize=(8, 4), dpi=200)

    # set styling on a single chart
    with sns.axes_style("darkgrid"):
        ax = sns.scatterplot(
            data=data_clean,
            x="USD_Production_Budget",
            y="USD_Worldwide_Gross",
            hue="USD_Worldwide_Gross",
            size="USD_Worldwide_Gross",
        )

    ax.set(
        ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel="Revenue in $ billions",
        xlabel="Budget in $100 millions",
    )

    plt.figure(figsize=(8, 4), dpi=200)

    with sns.axes_style("darkgrid"):
        ax = sns.scatterplot(
            data=data_clean,
            x="Release_Date",
            y="USD_Production_Budget",
            hue="USD_Worldwide_Gross",
            size="USD_Worldwide_Gross",
        )

        ax.set(
            ylim=(0, 450000000),
            xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
            xlabel="Year",
            ylabel="Budget in $100 millions",
        )

    dt_index = pd.DatetimeIndex(data_clean.Release_Date)
    years = dt_index.year

    # # How to convert the year 1999 to the 90s decade
    # 1999//10*10

    decades = years // 10 * 10
    data_clean["Decade"] = decades

    old_films = data_clean[data_clean.Decade <= 1960]
    new_films = data_clean[data_clean.Decade > 1960]

    old_films.describe()

    old_films.sort_values("USD_Production_Budget", ascending=False).head()

    sns.regplot(
        data=old_films,
        x="USD_Production_Budget",
        y="USD_Worldwide_Gross",
    )

    plt.figure(figsize=(8, 4), dpi=200)
    with sns.axes_style("whitegrid"):
        sns.regplot(
            data=old_films,
            x="USD_Production_Budget",
            y="USD_Worldwide_Gross",
            scatter_kws={"alpha": 0.4},
            line_kws={"color": "black"},
        )

    plt.figure(figsize=(8, 4), dpi=200)
    with sns.axes_style("darkgrid"):
        ax = sns.regplot(
            data=new_films,
            x="USD_Production_Budget",
            y="USD_Worldwide_Gross",
            color="#2f4b7c",
            scatter_kws={"alpha": 0.3},
            line_kws={"color": "#ff7c43"},
        )

    ax.set(
        ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel="Revenue in $ billions",
        xlabel="Budget in $100 millions",
    )

    #   REGRESSIONS (SCIKIT LEARN)

    # Create regression object
    regression = LinearRegression()
    # Explanatory Variable(s) or Feature(s)
    X = pd.DataFrame(new_films, columns=["USD_Production_Budget"])

    # Response Variable or Target
    y = pd.DataFrame(new_films, columns=["USD_Worldwide_Gross"])

    # Find the best-fit line
    regression.fit(X, y)

    # Theta zero
    regression.intercept_

    # Theta one
    regression.coef_

    # R-squared
    regression.score(X, y)

    nls("New Film Model")
    print(f"The slope coefficient is: {regression.coef_[0]}")
    print(f"The intercept is: {regression.intercept_[0]}")
    print(f"The r-squared is: {regression.score(X, y)}")

    nls("Old Film Model")
    X = pd.DataFrame(old_films, columns=["USD_Production_Budget"])
    y = pd.DataFrame(old_films, columns=["USD_Worldwide_Gross"])
    regression.fit(X, y)
    print(f"The slope coefficient is: {regression.coef_[0]}")
    print(f"The intercept is: {regression.intercept_[0]}")
    print(f"The r-squared is: {regression.score(X, y)}")

    # Making a prediction with model:
    budget = 350000000
    revenue_estimate = regression.intercept_[0] + regression.coef_[0, 0] * budget
    revenue_estimate = round(revenue_estimate, -6)
    print(f"The estimated revenue for a $350M film is around ${revenue_estimate:.2f}")
