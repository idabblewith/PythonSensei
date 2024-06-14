from days.day_074.files.helpers import *


def day_074():
    title("GTRENDS AND MATPLOTLIB")
    bitcoin_trend_data = os.path.join(
        os.path.dirname(__file__), "files", "data", "Bitcoin Search Trend.csv"
    )
    bitcoin_daily_data = os.path.join(
        os.path.dirname(__file__), "files", "data", "Daily Bitcoin Price.csv"
    )
    ue_data_19 = os.path.join(
        os.path.dirname(__file__),
        "files",
        "data",
        "UE Benefits Search vs UE Rate 2004-19.csv",
    )
    ue_data_20 = os.path.join(
        os.path.dirname(__file__),
        "files",
        "data",
        "UE Benefits Search vs UE Rate 2004-20.csv",
    )
    tesla_data = os.path.join(
        os.path.dirname(__file__), "files", "data", "TESLA Search Trend vs Price.csv"
    )

    df_tesla = pd.read_csv(tesla_data)
    df_btc_search = pd.read_csv(bitcoin_trend_data)
    df_btc_price = pd.read_csv(bitcoin_daily_data)
    df_unemployment = pd.read_csv(ue_data_19)
    df_unemployment_20 = pd.read_csv(ue_data_20)

    nls("================== TESLA ==================")
    nls(f"Tesla (HEAD):\n{df_tesla.head()}")
    nls(f"Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}")
    nls(f"Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}")
    nls(f"Description:\n{df_tesla.describe()}")
    nls("================== UNEMPLOYMENT ==================")
    nls(f"Unemployment Shape:\n{df_unemployment.shape}")
    nls(f"Unemployment (HEAD):\n{df_unemployment.head()}")
    nls(
        f"Largest value for Unemployemnt Benefits in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}"
    )
    nls("================== BITCOIN PRICE ==================")
    nls(f"Bitcoin Price Shape:\n{df_btc_price.shape}")
    nls(f"Bitcoin Price (HEAD):\n{df_btc_price.head()}")
    nls("================== BITCOIN SEARCH ==================")
    nls(f"Bitcoin Search Shape:\n{df_btc_search.shape}")
    nls(f"Bitcoin Search (HEAD):\n{df_btc_search.head()}")
    nls(f"largest BTC News Search {df_btc_search.BTC_NEWS_SEARCH.max()}")

    nls("================== DF MISSING VALUES ==================")

    nls(f"Missing values for Tesla?: {df_tesla.isna().values.any()}")
    nls(f"Missing values for U/E?: {df_unemployment.isna().values.any()}")
    nls(f"Missing values for BTC Search?: {df_btc_search.isna().values.any()}")
    nls(f"Missing values for BTC Price?: {df_btc_price.isna().values.any()}")
    nls(f"Number of missing values (BTC Price): {df_btc_price.isna().values.sum()}")
    nls(df_btc_price[df_btc_price.CLOSE.isna()])

    nls(f"Cleaned NA (Price):\n{df_btc_price.dropna(inplace=True)}")

    nls("================== STR TO DATE ==================")
    df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
    df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
    df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
    df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
    nls(f"Tesla Month (HEAD):\n{df_tesla.MONTH.head()}")

    nls("================== DAILY TO MONTHLY DATA ==================")
    df_btc_monthly = df_btc_price.resample("M", on="DATE").last()
    nls(f"BTC MONTHLY (SHAPE):\n{df_btc_monthly.shape}")
    nls(f"BTC MONTHLY (HEAD):\n{df_btc_monthly.head()}")

    nls("================== DATA VISUALISATION ==================")

    # Create locators for ticks on the time axis
    years = mdates.YearLocator()
    months = mdates.MonthLocator()
    years_fmt = mdates.DateFormatter("%Y")

    # Register date converters to avoid warning messages
    from pandas.plotting import register_matplotlib_converters

    register_matplotlib_converters()

    nls("================== TESLA CHART ==================")

    # ax1 = plt.gca() # get current axis
    # ax2 = ax1.twinx()

    # ax1.set_ylabel('TSLA Stock Price', color='#E6232E') # can use a HEX code
    # ax2.set_ylabel('Search Trend', color='skyblue') # or a named colour

    # ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E')
    # ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue')

    fig1 = plt.figure(figsize=(14, 8), dpi=120)  # increases size and resolution
    fig1.canvas.manager.set_window_title("Tesla Web Search vs Price")
    plt.title("Tesla Web Search vs Price", fontsize=18)

    # Increase the size and rotate the labels on the x-axis
    plt.xticks(fontsize=14, rotation=45)

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    # format the ticks
    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_major_formatter(years_fmt)
    ax1.xaxis.set_minor_locator(months)

    # Also, increase fontsize and linewidth for larger charts
    ax1.set_ylabel("TSLA Stock Price", color="#E6232E", fontsize=14)
    ax2.set_ylabel("Search Trend", color="skyblue", fontsize=14)

    # Set the minimum and maximum values on the axes
    ax1.set_ylim([0, 600])
    ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

    ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color="#E6232E", linewidth=3)
    ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color="skyblue", linewidth=3)

    # Displays chart explicitly
    plt.show()

    nls("================== BTC CHART ==================")

    fig2 = plt.figure(figsize=(14, 8), dpi=120)  # increases size and resolution
    fig2.canvas.manager.set_window_title("Bitcoin News Search vs Resampled Price")
    plt.title("Bitcoin News Search vs Resampled Price", fontsize=18)
    plt.xticks(fontsize=14, rotation=45)

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.set_ylabel("BTC Price", color="#F08F2E", fontsize=14)
    ax2.set_ylabel("Search Trend", color="skyblue", fontsize=14)

    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_major_formatter(years_fmt)
    ax1.xaxis.set_minor_locator(months)

    ax1.set_ylim(bottom=0, top=15000)
    ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])

    # Experiment with the linestyle and markers
    ax1.plot(
        df_btc_monthly.index,
        df_btc_monthly.CLOSE,
        color="#F08F2E",
        linewidth=3,
        linestyle="--",
    )
    ax2.plot(
        df_btc_monthly.index,
        df_btc_search.BTC_NEWS_SEARCH,
        color="skyblue",
        linewidth=3,
        marker="o",
    )

    plt.show()

    nls("================== UNEMPLOYMENT CHART ==================")
    fig3 = plt.figure(figsize=(14, 8), dpi=120)  # increases size and resolution
    fig3.canvas.manager.set_window_title(
        'Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate'
    )
    plt.title(
        'Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate',
        fontsize=18,
    )
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14, rotation=45)

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.set_ylabel("FRED U/E Rate", color="purple", fontsize=14)
    ax2.set_ylabel("Search Trend", color="skyblue", fontsize=14)

    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_major_formatter(years_fmt)
    ax1.xaxis.set_minor_locator(months)

    ax1.set_ylim(bottom=3, top=10.5)
    ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])

    # Show the grid lines as dark grey lines
    ax1.grid(color="grey", linestyle="--")

    # Change the dataset used
    ax1.plot(
        df_unemployment.MONTH,
        df_unemployment.UNRATE,
        color="purple",
        linewidth=3,
        linestyle="--",
    )
    ax2.plot(
        df_unemployment.MONTH,
        df_unemployment.UE_BENEFITS_WEB_SEARCH,
        color="skyblue",
        linewidth=3,
    )

    plt.show()

    fig4 = plt.figure(figsize=(14, 8), dpi=120)  # increases size and resolution
    fig4.canvas.manager.set_window_title(
        'Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE'
    )
    plt.title(
        'Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE', fontsize=18
    )
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14, rotation=45)

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_major_formatter(years_fmt)
    ax1.xaxis.set_minor_locator(months)

    ax1.set_ylabel("FRED U/E Rate", color="purple", fontsize=16)
    ax2.set_ylabel("Search Trend", color="skyblue", fontsize=16)

    ax1.set_ylim(bottom=3, top=10.5)
    ax1.set_xlim([df_unemployment.MONTH[0], df_unemployment.MONTH.max()])

    # Calculate the rolling average over a 6 month window
    roll_df = (
        df_unemployment[["UE_BENEFITS_WEB_SEARCH", "UNRATE"]].rolling(window=6).mean()
    )

    ax1.plot(
        df_unemployment.MONTH, roll_df.UNRATE, "purple", linewidth=3, linestyle="-."
    )
    ax2.plot(
        df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, "skyblue", linewidth=3
    )

    plt.show()

    df_unemployment_20.MONTH = pd.to_datetime(df_unemployment_20.MONTH)
    fig5 = plt.figure(figsize=(14, 8), dpi=120)  # increases size and resolution
    fig5.canvas.manager.set_window_title(
        'Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020'
    )
    plt.title(
        'Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18
    )

    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14, rotation=45)
    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.set_ylabel("FRED U/E Rate", color="purple", fontsize=16)
    ax2.set_ylabel("Search Trend", color="skyblue", fontsize=16)

    ax1.set_xlim([df_unemployment_20.MONTH.min(), df_unemployment_20.MONTH.max()])

    ax1.plot(df_unemployment_20.MONTH, df_unemployment_20.UNRATE, "purple", linewidth=3)
    ax2.plot(
        df_unemployment_20.MONTH,
        df_unemployment_20.UE_BENEFITS_WEB_SEARCH,
        "skyblue",
        linewidth=3,
    )

    plt.show()
