from days.day_079.files.helpers import *


def day_079():
    title("KERNEL DENSITY EST.")
    pd.options.display.float_format = "{:,.2f}".format

    # Create locators for ticks on the time axis
    years = mdates.YearLocator()
    months = mdates.MonthLocator()
    years_fmt = mdates.DateFormatter("%Y")

    # Register date converters to avoid warning messages
    register_matplotlib_converters()

    yearly = os.path.join(
        os.path.dirname(__file__), "files", "annual_deaths_by_clinic.csv"
    )
    monthly = os.path.join(os.path.dirname(__file__), "files", "monthly_deaths.csv")

    df_yearly = pd.read_csv(yearly)
    # parse_dates avoids DateTime conversion later
    df_monthly = pd.read_csv(monthly, parse_dates=["date"])

    # prelim exploration
    print(df_yearly.shape)
    df_yearly

    print(df_monthly.shape)
    df_monthly.tail()

    df_yearly.info()

    df_monthly.info()

    # Alternative to using .info()
    print(f"Any yearly NaN values? {df_monthly.isna().values.any()}")
    print(f"Any monthly NaN values? {df_yearly.isna().values.any()}")

    print(f"Any yearly duplicates? {df_yearly.duplicated().values.any()}")
    print(f"Any monthly duplicates? {df_monthly.duplicated().values.any()}")

    # descriptive stats
    df_yearly.describe()
    df_monthly.describe()

    # percentage of women dying during childbirth
    prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
    print(f"Chances of dying in the 1840s in Vienna: {prob:.3}%")

    # visualisation of births/deaths over time
    plt.figure(figsize=(14, 8), dpi=200)
    plt.title("Total Number of Monthly Births and Deaths", fontsize=18)

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.grid(color="grey", linestyle="--")

    ax1.plot(df_monthly.date, df_monthly.births, color="skyblue", linewidth=3)

    ax2.plot(
        df_monthly.date, df_monthly.deaths, color="crimson", linewidth=2, linestyle="--"
    )

    plt.show()

    plt.figure(figsize=(14, 8), dpi=200)
    plt.title("Total Number of Monthly Births and Deaths", fontsize=18)
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14, rotation=45)

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.set_ylabel("Births", color="skyblue", fontsize=18)
    ax2.set_ylabel("Deaths", color="crimson", fontsize=18)

    # Add locators for tick marks
    ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_major_formatter(years_fmt)
    ax1.xaxis.set_minor_locator(months)

    ax1.grid(color="grey", linestyle="--")

    ax1.plot(df_monthly.date, df_monthly.births, color="skyblue", linewidth=3)

    ax2.plot(
        df_monthly.date, df_monthly.deaths, color="crimson", linewidth=2, linestyle="--"
    )

    plt.show()

    # yearly data split by clinic
    # B
    line = px.line(
        df_yearly,
        x="year",
        y="births",
        color="clinic",
        title="Total Yearly Births by Clinic",
    )

    line.show()

    # D
    line = px.line(
        df_yearly,
        x="year",
        y="deaths",
        color="clinic",
        title="Total Yearly Deaths by Clinic",
    )

    line.show()

    # Proportion
    df_yearly["pct_deaths"] = df_yearly.deaths / df_yearly.births
    df_yearly

    clinic_1 = df_yearly[df_yearly.clinic == "clinic 1"]
    avg_c1 = clinic_1.deaths.sum() / clinic_1.births.sum() * 100
    print(f"Average death rate in clinic 1 is {avg_c1:.3}%.")

    clinic_2 = df_yearly[df_yearly.clinic == "clinic 2"]
    avg_c2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100
    print(f"Average death rate in clinic 2 is {avg_c2:.3}%.")

    # Plotting proportion
    line = px.line(
        df_yearly,
        x="year",
        y="pct_deaths",
        color="clinic",
        title="Proportion of Yearly Deaths by Clinic",
    )

    line.show()

    # Handwashing effect
    # Date when handwashing was made mandatory
    handwashing_start = pd.to_datetime("1847-06-01")

    df_monthly["pct_deaths"] = df_monthly.deaths / df_monthly.births

    # Split monthly into before and after handwashing_start
    before_washing = df_monthly[df_monthly.date < handwashing_start]
    after_washing = df_monthly[df_monthly.date >= handwashing_start]

    bw_rate = before_washing.deaths.sum() / before_washing.births.sum() * 100
    aw_rate = after_washing.deaths.sum() / after_washing.births.sum() * 100
    print(f"Average death rate before 1847 was {bw_rate:.4}%")
    print(f"Average death rate AFTER 1847 was {aw_rate:.3}%")

    # Calculate a rolling average of death rate

    # Convert Date Column to Index first so does not get dropped
    roll_df = before_washing.set_index("date")
    roll_df = roll_df.rolling(window=6).mean()
    roll_df

    # Highlight subsections of a line chart
    plt.figure(figsize=(14, 8), dpi=200)
    plt.title("Percentage of Monthly Deaths over Time", fontsize=18)
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14, rotation=45)

    plt.ylabel("Percentage of Deaths", color="crimson", fontsize=18)

    ax = plt.gca()
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(months)
    ax.set_xlim([df_monthly.date.min(), df_monthly.date.max()])

    plt.grid(color="grey", linestyle="--")

    (ma_line,) = plt.plot(
        roll_df.index,
        roll_df.pct_deaths,
        color="crimson",
        linewidth=3,
        linestyle="--",
        label="6m Moving Average",
    )
    (bw_line,) = plt.plot(
        before_washing.date,
        before_washing.pct_deaths,
        color="black",
        linewidth=1,
        linestyle="--",
        label="Before Handwashing",
    )
    (aw_line,) = plt.plot(
        after_washing.date,
        after_washing.pct_deaths,
        color="skyblue",
        linewidth=3,
        marker="o",
        label="After Handwashing",
    )

    plt.legend(handles=[ma_line, bw_line, aw_line], fontsize=18)

    plt.show()

    # Stats - calculate difference in the avg monthly death rate

    avg_prob_before = before_washing.pct_deaths.mean() * 100
    print(
        f"Chance of death during childbirth before handwashing: {avg_prob_before:.3}%."
    )

    avg_prob_after = after_washing.pct_deaths.mean() * 100
    print(f"Chance of death during childbirth AFTER handwashing: {avg_prob_after:.3}%.")

    mean_diff = avg_prob_before - avg_prob_after
    print(f"Handwashing reduced the monthly proportion of deaths by {mean_diff:.3}%!")

    times = avg_prob_before / avg_prob_after
    print(f"This is a {times:.2}x improvement!")

    # Showing how death rate changed before vs after handwashing
    # NumPy .where() method
    df_monthly["washing_hands"] = np.where(
        df_monthly.date < handwashing_start, "No", "Yes"
    )

    box = px.box(
        df_monthly,
        x="washing_hands",
        y="pct_deaths",
        color="washing_hands",
        title="How Have the Stats Changed with Handwashing?",
    )

    box.update_layout(
        xaxis_title="Washing Hands?",
        yaxis_title="Percentage of Monthly Deaths",
    )

    box.show()

    # Historgram to visualise monthly distr. of outcomes
    hist = px.histogram(
        df_monthly,
        x="pct_deaths",
        color="washing_hands",
        nbins=30,
        opacity=0.6,
        barmode="overlay",
        histnorm="percent",
        marginal="box",
    )

    hist.update_layout(
        xaxis_title="Proportion of Monthly Deaths",
        yaxis_title="Count",
    )

    hist.show()

    # Kernel Density Estimate (KDE) to visualise a smooth distr.

    plt.figure(dpi=200)
    # By default the distribution estimate includes a negative death rate!
    sns.kdeplot(before_washing.pct_deaths, shade=True)
    sns.kdeplot(after_washing.pct_deaths, shade=True)
    plt.title("Est. Distribution of Monthly Death Rate Before and After Handwashing")
    plt.show()

    plt.figure(dpi=200)
    sns.kdeplot(before_washing.pct_deaths, shade=True, clip=(0, 1))
    sns.kdeplot(after_washing.pct_deaths, shade=True, clip=(0, 1))
    plt.title("Est. Distribution of Monthly Death Rate Before and After Handwashing")
    plt.xlim(0, 0.40)
    plt.show()

    # T-Test to show statistical significance
    t_stat, p_value = stats.ttest_ind(
        a=before_washing.pct_deaths, b=after_washing.pct_deaths
    )
    print(f"p-value is {p_value:.10f}")
    print(f"t-statstic is {t_stat:.4}")
