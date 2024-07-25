from days.day_082.files.helpers import *


def day_082():
    title("STOCK ANALYSIS")

    def fetch_historical_prices(symbol, start_date, end_date):
        """
        Fetch historical stock prices using Yahoo Finance.

        Parameters:
        symbol (str): Stock symbol
        start_date (str): Start date for fetching data (YYYY-MM-DD)
        end_date (str): End date for fetching data (YYYY-MM-DD)

        Returns:
        pd.DataFrame: Historical stock prices
        """
        try:
            data = yf.download(symbol, start=start_date, end=end_date)
            return data
        except Exception as e:
            print(f"Error fetching data for {symbol}: {str(e)}")
            return None

    def calculate_moving_average(prices, window=20):
        """
        Calculate the moving average for the closing prices.

        Parameters:
        prices (pd.DataFrame): DataFrame containing stock prices
        window (int): Window size for moving average

        Returns:
        pd.Series: Moving average
        """
        return prices["Close"].rolling(window=window).mean()

    def calculate_rsi(prices, window=14):
        """
        Calculate the Relative Strength Index (RSI) for the closing prices.

        Parameters:
        prices (pd.DataFrame): DataFrame containing stock prices
        window (int): Window size for RSI calculation

        Returns:
        pd.Series: RSI values
        """
        delta = prices["Close"].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_macd(prices, short_window=12, long_window=26, signal_window=9):
        """
        Calculate the Moving Average Convergence Divergence (MACD) for the closing prices.

        Parameters:
        prices (pd.DataFrame): DataFrame containing stock prices
        short_window (int): Short window for MACD calculation
        long_window (int): Long window for MACD calculation
        signal_window (int): Signal window for MACD calculation

        Returns:
        tuple: MACD line, Signal line, MACD histogram
        """
        exp_short = (
            prices["Close"].ewm(span=short_window, min_periods=short_window).mean()
        )
        exp_long = prices["Close"].ewm(span=long_window, min_periods=long_window).mean()
        macd_line = exp_short - exp_long
        signal_line = macd_line.ewm(
            span=signal_window, min_periods=signal_window
        ).mean()
        macd_histogram = macd_line - signal_line
        return macd_line, signal_line, macd_histogram

    def backtest_strategy(prices, rsi, macd_histogram, initial_investment=100000):
        """
        Perform backtesting using RSI and MACD histogram as signals.

        Parameters:
        prices (pd.DataFrame): DataFrame containing stock prices
        rsi (pd.Series): RSI values
        macd_histogram (pd.Series): MACD histogram values
        initial_investment (float): Initial investment amount

        Returns:
        pd.Series: Investment value over time
        """
        buy_signals = (rsi < 30) & (macd_histogram > 0)
        sell_signals = (rsi > 70) & (macd_histogram < 0)

        position = pd.Series(index=prices.index, data=0.0)
        in_position = False

        for i in range(1, len(prices)):
            if buy_signals.iloc[i] and not in_position:
                position.iloc[i] = 1.0
                in_position = True
            elif sell_signals.iloc[i] and in_position:
                position.iloc[i] = -1.0
                in_position = False
            else:
                position.iloc[i] = position.iloc[i - 1]

        daily_returns = prices["Close"].pct_change()
        strategy_returns = daily_returns * position.shift(1).fillna(0)
        cumulative_returns = (1 + strategy_returns).cumprod()
        investment_value = initial_investment * cumulative_returns
        return investment_value

    def plot_backtest_results(
        symbol, prices, investment_value, initial_investment=100000
    ):
        """
        Plot the backtest results with swapped axes.

        Parameters:
        symbol (str): Stock symbol
        prices (pd.DataFrame): DataFrame containing stock prices
        investment_value (pd.Series): Investment value over time
        initial_investment (float): Initial investment amount
        """
        fig, ax2 = plt.subplots(figsize=(12, 6))

        # Plot investment value on the left y-axis
        color = "tab:green"
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Investment Value ($)", color=color)
        ax2.plot(
            prices.index,
            investment_value,
            label=f"Investment Value (${initial_investment})",
            color=color,
        )
        ax2.tick_params(axis="y", labelcolor=color)

        ax1 = ax2.twinx()  # instantiate a second axes that shares the same x-axis

        # Plot stock price on the right y-axis
        color = "tab:blue"
        ax1.set_ylabel("Stock Price ($)", color=color)
        ax1.plot(prices.index, prices["Close"], label="Stock Price", color=color)
        ax1.tick_params(axis="y", labelcolor=color)

        fig.suptitle(f"{symbol} Backtest Results")

        # Legends
        lines_1, labels_1 = ax1.get_legend_handles_labels()
        lines_2, labels_2 = ax2.get_legend_handles_labels()
        ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

        fig.tight_layout()  # otherwise the right y-label is slightly clipped

        plt.show()

    def main(symbol, start_date, end_date):
        historical_data = fetch_historical_prices(symbol, start_date, end_date)
        if historical_data is not None:
            ma = calculate_moving_average(historical_data)
            rsi = calculate_rsi(historical_data)
            macd_line, _, macd_histogram = calculate_macd(historical_data)
            investment_value = backtest_strategy(historical_data, rsi, macd_histogram)
            final_pnl = (investment_value.iloc[-1] / 100000 - 1) * 100
            final_investment_value = investment_value.iloc[-1]
            print(
                f"This strategy shows a PnL of {final_pnl:.2f}% between {start_date} and {end_date}."
            )
            print(
                f"The initial investment of $100,000 would be worth ${final_investment_value:.2f} under this strategy."
            )
            plot_backtest_results(symbol, historical_data, investment_value)

    if __name__ == "days.day_082.main":
        nls("Backtesting initial investment of $100,000 with AAPL")
        symbol = "AAPL"  # Example: Apple stock
        start_date = "2010-01-01"
        end_date = "2023-12-31"
        main(symbol, start_date, end_date)
