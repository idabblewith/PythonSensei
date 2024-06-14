from days.day_071.files.helpers import *


def day_071():
	title("PANDAS DATA EXPLORATION")
	salary_data_path = os.path.join(
		os.path.dirname(__file__), "files", "salaries_by_college_major.csv"
	)
	df = pd.read_csv(salary_data_path)
	nls("HEAD Print:")
	print(df.head())
	nls("Shape Print:")
	print(df.shape)
	nls("Columns Print:")
	print(df.columns)
	nls("Is NA Print:")
	print(df.isna())

	nls("Cleaning NA and printing tail...")
	clean_df = df.dropna()
	print(clean_df.tail())

	nls("Starting Median Salary...")
	print(clean_df["Starting Median Salary"].max())

	nls("Starting Median Salary row ID...")
	print(clean_df["Starting Median Salary"].idxmax())

	nls("That Row's data for salary...")
	print(clean_df["Starting Median Salary"][43])

	nls("Row 43's Undergraduate Major cell's data...")
	print(clean_df["Undergraduate Major"].loc[43])
	print(clean_df["Undergraduate Major"][43])

	nls("All Row 43's Data...")
	print(clean_df.loc[43])

	nls("The Highest Mid-Career Salary")
	print(f"Salary:\n{clean_df["Mid-Career Median Salary"].max()}\n")
	print(
		f"Index for the max mid career salary:\n{clean_df['Mid-Career Median Salary'].idxmax()}\n"
	)
	print(f"Undergraduate:\n{clean_df["Undergraduate Major"][8]}\n")

	nls("The Lowest Starting and Mid-Career Salary")
	print(f"Lowest Starting Salary:\n{clean_df["Starting Median Salary"].min()}\n")
	print(
		f"Major:\n{clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]}\n"
	)
	print(f"Lowest Mid Career Undergraduate/Salary Details:\n\n{clean_df.loc[clean_df["Mid-Career Median Salary"].idxmin()]}\n")

	# Create column for spread in salaries
	spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
	# ALTERNATIVE: clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
	clean_df.insert(1, 'Spread', spread_col)
	print(clean_df.head())

	nls("Lowest Risk Major")
	low_risk = clean_df.sort_values('Spread')
	low_risk[['Undergraduate Major', 'Spread']].head()

	nls("Highest Potential Major")
	highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
	highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

	nls("Highest Risk Major (big salary spread)")
	highest_spread = clean_df.sort_values('Spread', ascending=False)
	highest_spread[['Undergraduate Major', 'Spread']].head()

	nls("Best Mid Career Salary")
	highest_spread = clean_df.sort_values('Mid-Career Median Salary', ascending=False)
	highest_spread[['Undergraduate Major', 'Mid-Career Median Salary']].head()

	nls("Grouped")
	print(f"Count:\n{clean_df.groupby('Group').count()}")
	pd.options.display.float_format = '{:,.2f}'.format
	print(f"Mean:\n{clean_df.groupby('Group').mean(numeric_only=True)}")
	
