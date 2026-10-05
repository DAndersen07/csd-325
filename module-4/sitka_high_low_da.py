"""Sitka temperature viewer — Dustin Andersen, Assignment 4.

Changes to sitka_highs.py:
1. Added startup instructions and a Highs, Lows, or Exit menu.
2. Read low temperatures from CSV column 7 along with the highs.
3. Added a repeating menu with input validation.
4. Display highs in red and lows in blue with matching graph titles.
5. Added an exit message and sys.exit() to end the program.
6. Locate the CSV beside this program so it can run from another folder.
"""

import csv
import sys  # DA: used to exit after the user selects Exit.
from datetime import datetime
from pathlib import Path  # DA: locate the data file beside this script.

from matplotlib import pyplot as plt

# DA: explain the menu before loading data or asking for a choice.
print('Sitka Daily Temperatures — 2018')
print('Enter Highs to see daily high temperatures in red.')
print('Enter Lows to see daily low temperatures in blue.')
print('Close the graph window to return to the menu.')
print('Enter Exit to end the program.')

filename = Path(__file__).with_name('sitka_weather_2018_simple.csv')
with open(filename, newline='') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # DA: collect both highs and lows for each date.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])  # DA: TMIN is the seventh CSV column.
        lows.append(low)

# DA: repeat until the user chooses Exit; accept any capitalization.
while True:
    choice = input('\nSelect Highs, Lows, or Exit: ').strip().lower()

    if choice == 'exit':
        print('Thanks for using the Sitka temperature viewer. Goodbye!')
        sys.exit()
    elif choice == 'highs':
        temperatures = highs
        color = 'red'
        title = 'Daily high temperatures - 2018'
    elif choice == 'lows':
        temperatures = lows
        color = 'blue'
        title = 'Daily low temperatures - 2018'
    else:
        print('Please enter Highs, Lows, or Exit.')
        continue

    # DA: create a new graph for the selected temperatures each time.
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)

    # Keep the original graph formatting, using the selected title.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()  # Close this window to return to the menu.
    plt.close(fig)  # DA: clean up the graph before the next selection.
