from days.day_072.files.helpers import *


def day_072():
    title("MATPLOTLIB")
    programming_data_path = os.path.join(
        os.path.dirname(__file__), "files", "QueryResults.csv"
    )
    df = pd.read_csv(programming_data_path, names=["DATE", "TAG", "POSTS"], header=0)

    nls(f"HEAD:\n{df.head()}")
    nls(f"TAIL:\n{df.tail()}")
    nls(f"SHAPE OF DF:\n{df.shape}")
    nls(f"COUNT OF ENTRIES PER COLUMN:\n{df.count()}")
    nls(f"TOTAL POSTS PER LANG:\n{df.groupby('TAG').sum()}")
    nls(f"MONTHS OF DATA PER LANG:\n{df.groupby('TAG').count()}")

    # Convert Entire Column to more readable date format
    nls("Better organised date")
    df.DATE = pd.to_datetime(df.DATE)
    nls(df.head())

    # Test df Manipulation
    test_df = pd.DataFrame(
        {
            "Age": ["Young", "Young", "Young", "Young", "Old", "Old", "Old"],
            "Actor": [
                "Jack",
                "Arnold",
                "Keanu",
                "Sylvester",
                "Jack",
                "Arnold",
                "Keanu",
            ],
            "Power": [100, 80, 25, 50, 99, 75, 5],
        }
    )
    nls(f"Test DF:\n{test_df}")
    pivoted_df = test_df.pivot(index="Age", columns="Actor", values="Power")
    nls(f"Pivoted Test DF:\n{pivoted_df}")

    reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
    # fill nas during reshape: reshaped_df = df.pivot_table(index='Date', columns='Tag', values='Posts', fill_value=0)

    nls(f"Reshaped DF:\n{reshaped_df}")
    nls(f"Reshaped shape:\n{reshaped_df.shape}")
    nls(f"Reshaped columns:\n{reshaped_df.columns}")
    nls(f"Reshaped HEAD:\n{reshaped_df.head()}")
    nls(f"Reshaped COUNT:\n{reshaped_df.count()}")

    # Fixing NA
    nls("Replacing NA with 0")
    reshaped_df.fillna(0, inplace=True)
    nls(f"Reshaped HEAD after fixing NA:\n{reshaped_df.head()}")
    nls(f"Any Nas left?\n{reshaped_df.isna().values.any()}")

    # Plotting with matplotlib
    nls("Plotting raw data table")
    fig1 = plt.figure(figsize=(16, 10))
    fig1.canvas.manager.set_window_title("Raw Data Plot")
    plt.title("Raw Data Table", fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Number of Posts", fontsize=14)
    plt.ylim(0, 35000)
    # plot all languages using for loop
    for column in reshaped_df.columns:
        plt.plot(
            reshaped_df.index,
            reshaped_df[column],
            linewidth=3,
            label=reshaped_df[column].name,
        )
    plt.legend(fontsize=16)
    plt.show()

    # The window is number of observations that are averaged (generate a smooted out time series data)
    nls("Plotting smoothed out rolling data table")
    roll_df = reshaped_df.rolling(window=6).mean()
    fig2 = plt.figure(figsize=(16, 10))
    fig2.canvas.manager.set_window_title("Smoothed Out Rolling Data Plot")
    plt.title("Smoothed Out Rolling Data Table", fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Number of Posts", fontsize=14)
    plt.ylim(0, 35000)

    # plot the roll_df instead
    for column in roll_df.columns:
        plt.plot(
            roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name
        )

    plt.legend(fontsize=16)
    plt.show()
    # nli("Continue?")
