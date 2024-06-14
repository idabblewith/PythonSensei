from days.day_073.files.helpers import *


def day_073():
    title("LEGO PANDAS")
    colors_data = os.path.join(os.path.dirname(__file__), "files", "data", "colors.csv")
    colors = pd.read_csv(colors_data, header=0)
    nls(f"Colours Head:\n{colors.head()}")
    nls(f"Colours Unique Count:\n{colors['name'].nunique()}")
    nls(f"Trans Colours Count:\n{colors.groupby('is_trans').count()}")
    # colors.is_trans.value_counts()

    sets_data = os.path.join(os.path.dirname(__file__), "files", "data", "sets.csv")
    sets = pd.read_csv(sets_data, header=0)
    nls(f"Sets Head:\n{sets.head()}")
    nls(f"Sets Tail:\n{sets.tail()}")
    nls(f"First Release Year:\n{sets.sort_values('year').head()}")
    nls(f"Sets Sold in First Year:\n{sets[sets['year'] == 1949]}")
    nls(
        f"Top 5 Lego Sets with Most Parts:\n{sets.sort_values('num_parts', ascending=False).head()}"
    )

    sets_by_year = sets.groupby("year").count()
    nls(f"Lego Sets Released Year on Year (HEAD):\n{sets_by_year['set_num'].head()}")
    nls(f"Lego Sets Released Year on Year (HEAD):\n{sets_by_year['set_num'].tail()}")

    # # PLOTTING
    # # Full data
    # fig1 = plt.figure(figsize=(16, 10))
    # fig1.canvas.manager.set_window_title("Number of Themes Released Each Year")
    # plt.title("Number of Themes Released Each Year", fontsize=18)
    # plt.xticks(fontsize=14)
    # plt.yticks(fontsize=14)
    # plt.xlabel("Year", fontsize=14)
    # plt.ylabel("Number of Themes", fontsize=14)
    # plt.plot(sets_by_year.index, sets_by_year.set_num)
    # plt.show()

    # # Without last 2 years
    # fig2 = plt.figure(figsize=(16, 10))
    # fig2.canvas.manager.set_window_title(
    #     "Number of Themes Released Each Year (Without last 2 years)"
    # )
    # plt.title("Number of Themes Released Each Year (Without last 2 years)", fontsize=18)
    # plt.xticks(fontsize=14)
    # plt.yticks(fontsize=14)
    # plt.xlabel("Year", fontsize=14)
    # plt.ylabel("Number of Themes", fontsize=14)
    # plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
    # plt.show()

    # themes_by_year = sets.groupby("year").agg({"theme_id": pd.Series.nunique})
    # themes_by_year.rename(columns={"theme_id": "nr_themes"}, inplace=True)
    # nls(f"Themes by Year (HEAD):\n{themes_by_year.head()}")
    # nls(f"Themes by Year (HEAD):\n{themes_by_year.tail()}")

    # # Number of Themes Released Each Year
    # fig3 = plt.figure(figsize=(16, 10))
    # fig3.canvas.manager.set_window_title("Number of Themes Released Each Year")
    # plt.title("Number of Themes Released Each Year", fontsize=18)
    # plt.xticks(fontsize=14)
    # plt.yticks(fontsize=14)
    # plt.xlabel("Year", fontsize=14)
    # plt.ylabel("Number of Themes", fontsize=14)
    # plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
    # plt.show()

    # ax1 = plt.gca()  # get the axis
    # ax2 = ax1.twinx()  # create another axis that shares the same x-axis

    # # Add styling
    # ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color="g")
    # ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], "b")

    # ax1.set_xlabel("Year")
    # ax1.set_ylabel("Number of Sets", color="green")
    # ax2.set_ylabel("Number of Themes", color="blue")
    # plt.show()

    parts_per_set = sets.groupby("year").agg({"num_parts": pd.Series.mean})
    nls(f"AVERAGE PARTS PER YEAR (HEAD):\n{parts_per_set.head()}")
    nls(f"AVERAGE PARTS PER YEAR (TAIL):\n{parts_per_set.tail()}")
    plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
    plt.show()

    set_theme_count = sets["theme_id"].value_counts()
    nls(f"Sets Count (Last 5):\n{set_theme_count[:5]}")

    themes_data = os.path.join(os.path.dirname(__file__), "files", "data", "themes.csv")
    themes = pd.read_csv(themes_data, header=0)
    nls(f"Themes (HEAD):\n{themes.head()}")
    nls(f"Starwars Themes:\n{themes[themes.name == 'Star Wars']}")
    nls(f"{sets[sets.theme_id == 18]}")
    nls(f"{sets[sets.theme_id == 209]}")
    set_theme_count = pd.DataFrame(
        {"id": set_theme_count.index, "set_count": set_theme_count.values}
    )
    nls(f"Themes Count(HEAD):\n{set_theme_count.head()}")

    # Merged
    merged_df = pd.merge(set_theme_count, themes, on="id")
    merged_df[:3]

    plt.figure(figsize=(14, 8))
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.ylabel("Nr of Sets", fontsize=14)
    plt.xlabel("Theme Name", fontsize=14)

    plt.bar(merged_df.name[:10], merged_df.set_count[:10])
    plt.show()
