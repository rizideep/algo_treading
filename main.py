from kite_setup import initialize_kite
from kite_trade import RealKiteConnect

def main():
    # Step 1: Initialize Kite Connect and authenticate
    kite = initialize_kite()

    # Instantiate the RealKiteConnect class
    real_kite = RealKiteConnect(kite)

    # Fetching market data for a stock
    symbol = "NSE:RELIANCE"
    market_data = real_kite.market_data(symbol)
    print(f"Market Data for {symbol}: {market_data}")

    # Step 2: Simulating placing a buy order for NSE:RELIANCE
    buy_order = real_kite.place_order(
        variety="regular",
        exchange="NSE",
        tradingsymbol=symbol,
        transaction_type="BUY",
        quantity=10,
        product="MIS",
        order_type="MARKET"
    )
    print("Buy Order Statu:", buy_order)

    # Simulating placing a sell order for NSE:RELIANCE
    sell_order = real_kite.place_order(
        variety="regular",
        exchange="NSE",
        tradingsymbol=symbol,
        transaction_type="SELL",
        quantity=10,
        product="MIS",
        order_type="MARKET"
    )

    print("Sell Order Status:", sell_order)

if __name__ == "__main__":
    main()
