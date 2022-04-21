"""
Name: Margaret Kimery
file: lab13.py
problem: Use Python's built-in list functions, Develop while control structures, Use boolean logic
certification of authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(filename):
    with open(filename, "r") as file:
        trade = file.readline()
        trade_volume = trade.split()
        for trade in trade_volume:
            counter = counter + 1
            if trade_volume > 830:
                print("ALERT! TRADE VOLUME IS AT 830!")
                print(counter, " seconds")
            if trade_volume == 500:
                print("ALERT! TRADE VOLUME IS AT 500!")
                print(counter, " seconds")
            else:
                print("CAUTION. WATCH TRADE VOLUME.")
                print(counter, " seconds")
