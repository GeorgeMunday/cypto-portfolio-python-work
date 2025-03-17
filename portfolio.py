import pandas as pd
import matplotlib.pyplot as plt

def bar_graph(x, y):
    plt.xlabel(str(x.name))
    plt.ylabel(str(y.name))
    plt.title("Portfolio")
    plt.bar(x, y)
    plt.show()

def graph(x, y):
    plt.xlabel(str(x.name))
    plt.ylabel(str(y.name))
    plt.title("Portfolio")
    plt.plot(x, y)
    plt.show()

def date_graph(MSFT_df, AMZN_df, IBM_df, GOOG_df, AAPL_df):
    plt.figure(figsize=(10, 6))
    plt.plot(MSFT_df['date'], MSFT_df['price'], label='Microsoft (MSFT)')
    plt.plot(AMZN_df['date'], AMZN_df['price'], label='Amazon (AMZN)')
    plt.plot(IBM_df['date'], IBM_df['price'], label='IBM (IBM)')
    plt.plot(GOOG_df['date'], GOOG_df['price'], label='Google (GOOG)')
    plt.plot(AAPL_df['date'], AAPL_df['price'], label='Apple (AAPL)')
    
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.title('Stock Prices of MSFT, AMZN, IBM, GOOG, and AAPL')
    plt.xticks(rotation = 90, fontsize = 5)
    plt.legend()
    plt.tight_layout()
    plt.show()

def get_data_from_csv(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def filter_logic(df):
    filter_options = {
        "price": ("Purchase Price", "Asset Name"),
        "quantity": ("Quantity", "Asset Name"),
        "prices": ("Current Price", "Asset Name"),
    }
    while True:
        filter_option = input("Enter your filter option (purchase price, quantity, prices):").strip().lower()
        if filter_option in filter_options:
            y, x = filter_options[filter_option]
            bar_graph(df[x], df[y])
            break
        else:
            print("Invalid filter option")

def display_portfolio(df):
    print(df)
    print("################################################################################")
    while True:
        try:
            user_input = input("Would you like to filter (yes/no)? ").strip().lower()
            if user_input == "yes":
                filter_logic(df)
                break
            elif user_input == "no":
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input")

def View_whole_Portfolio():
    df = get_data_from_csv("stock_crypto_portfolio.csv")
    if df is not None:
        display_portfolio(df)

def stock_portfolio():
    df = get_data_from_csv("stock_crypto_portfolio.csv")
    if df is not None:
        df = df[df["Type"] == "Stock"]
        display_portfolio(df)

def crypto_portfolio():
    df = get_data_from_csv("stock_crypto_portfolio.csv")
    if df is not None:
        df = df[df["Type"] == "Crypto"]
        display_portfolio(df)

def portfolio_insights():
    df = get_data_from_csv("stocks.csv")
    if df is not None:
        max_price = df["price"].max()
        min_price = df["price"].min()
        avg_price = df["price"].mean()

        print(f"Maximum Profit: {max_price}")
        print(f"Minimum Profit: {min_price}")
        print(f"Average Profit: {avg_price}")

        df = df.sort_values(by="price")
        y = df["price"]
        x = df["symbol"]
        bar_graph(x, y)

def stocks_today():
    df = get_data_from_csv("stocks.csv")
    if df is not None:
        MSFT_df = df[df["symbol"] == "MSFT"]
        AMZN_df = df[df["symbol"] == "AMZN"]
        IBM_df = df[df["symbol"] == "IBM"]
        GOOG_df = df[df["symbol"] == "GOOG"]
        AAPL_df = df[df["symbol"] == "AAPL"]
        date_graph(MSFT_df, AMZN_df, IBM_df, GOOG_df, AAPL_df)

def portfolio():
    options = {
        1: View_whole_Portfolio,
        2: stock_portfolio,
        3: crypto_portfolio,
        4: portfolio_insights,
        5: stocks_today,
        6: exit
    }
    while True:
        try:
            user_input = input("""Enter your option:
1. View portfolio
2. Stock portfolio
3. Crypto portfolio
4. Portfolio insights
5. Stocks today
6. Exit
Enter here: """)
            user_input = int(user_input)
            if 1 <= user_input <= 6:
                break
            else:
                raise ValueError
        except ValueError:
            print("Incorrect data")

    options[user_input]()

def menu():
    print("Welcome to the portfolio program.")
    counter = 0
    while counter < 3:
        usernames = ["hello", "world", "python"]
        passwords = ["hello", "world", "python"]
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in usernames and passwords[usernames.index(username)] == password:
            print("Welcome to your portfolio.")
            portfolio()
            break
        else:
            print("Incorrect username or password. Please try again.")
            counter += 1
    else:
        print("You have exceeded the maximum number of attempts. Please try again later.")
        exit()
        
menu()