import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=20)

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'red')
    # Create second line of best fit
    df1 = df[df['Year'] >= 2000]
    res1 = linregress(df1['Year'], df1['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = res1.slope * x_pred2 + res1.intercept
    plt.plot(x_pred2, y_pred2, 'green')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()