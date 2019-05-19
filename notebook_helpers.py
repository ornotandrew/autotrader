import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_candles(df):
    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator()  # every month
    yearsFmt = mdates.DateFormatter('%Y')

    fig, ax = plt.subplots()

    df.plot.line(x='Close time', y='Close', ax=ax)

    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    fig.autofmt_xdate()
    ax.grid(True, linestyle='--')

    plt.rcParams['figure.figsize'] = [15, 10]

    return fig, ax
