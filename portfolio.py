import pandas as pd
import matplotlib.pyplot as plt

def load_csv_data(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def plot_graph(x, y, plot_type='bar'):
    plt.xlabel(str(x.name))
    plt.ylabel(str(y.name))
    plt.title("Portfolio")
    (plt.bar(x, y) if plot_type == 'bar' else plt.plot(x, y))
    plt.show()

def filter_logic(df):
    filter_options = {
        "price": ("Purchase Price", "Asset Name"),
        "quantity": ("Quantity", "Asset Name"),
        "prices": ("Current Price", "Asset Name"),
    }
    while (filter_option := input("Enter filter (price, quantity, prices):").strip().lower()) not in filter_options:
        print("Invalid filter option")
    y, x = filter_options[filter_option]
    plot_graph(df[x], df[y], 'bar')

def display_portfolio(df):
    print(df, "\n" + "#" * 80)
    while input("Would you like to filter (yes/no)? ").strip().lower() == "yes":
        filter_logic(df)

def portfolio_insights():
    df = load_csv_data("stocks.csv")
    if df is not None:
        print(f"Maximum: {df['price'].max()} Minimum: {df['price'].min()} Average: {df['price'].mean()}")
        plot_graph(df["symbol"], df["price"], 'bar')

def date_graph():
    df = load_csv_data("stocks.csv")
    if df is not None:
        symbols = ['MSFT', 'AMZN', 'IBM', 'GOOG', 'AAPL']
        plt.figure(figsize=(10, 6))
        for symbol in symbols:
            df_symbol = df[df["symbol"] == symbol]
            plt.plot(df_symbol['date'], df_symbol['price'], label=f'{symbol} Stock')
        plt.xlabel('Date')
        plt.ylabel('Stock Price (USD)')
        plt.title('Stock Prices Today')
        plt.xticks(rotation=90, fontsize=8)
        plt.legend()
        plt.tight_layout()
        plt.show()

def menu():
    print("Welcome to the portfolio program.")
    usernames, passwords = ["hello", "world", "python"], ["hello", "world", "python"]
    for i in range(3):
        username, password = input("Username: "), input("Password: ")
        if username in usernames and passwords[usernames.index(username)] == password:
            portfolio()
            break
    else:
        print("Maximum attempts exceeded.")
        exit()

def portfolio():
    options = {
        1: lambda: display_portfolio(load_csv_data("stock_crypto_portfolio.csv")),
        2: lambda: display_portfolio(load_csv_data("stock_crypto_portfolio.csv")[load_csv_data("stock_crypto_portfolio.csv")["Type"] == "Stock"]),
        3: lambda: display_portfolio(load_csv_data("stock_crypto_portfolio.csv")[load_csv_data("stock_crypto_portfolio.csv")["Type"] == "Crypto"]),
        4: portfolio_insights,
        5: date_graph,
        6: exit
    }
    while (user_input := input("""Enter option:
1. View portfolio
2. Stock portfolio
3. Crypto portfolio
4. Portfolio insights
5. Stocks today
6. Exit
Enter here: """)) not in {'1', '2', '3', '4', '5', '6'}:
        print("Invalid input")
    options[int(user_input)]()

menu()