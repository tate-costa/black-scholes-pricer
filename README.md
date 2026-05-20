# Black-Scholes Options Pricer
**Tate Costa - MS Statistics Portfolio **
A complete Black-Scholes options pricing engine, in which runs on real market data. Within the interactive notebook, live option chains are pulled from Yahoo Finance, using the created formulas for the Black-Scholes model, it is reversed to solve for implied volatility across each strike price within the chain, and generate trade signals by comparing market implied volatility against historical volatility forecasts. 

Although this may currently seems like a relatively simple strategy to come up with my own volatility forecast, I plan to continue on and develop GARCH models in order to more closely identify the volatility of the specific stock, and utilize this value to make more justified decisions on trading strategy. 


## What this project does:

1. Pulls real stock data and calculates historical volatility
2. Automatically finds the closest option expiry based on the target date input by user
3. Fetches the live options chain from Yahoo finance based on the stock chosen by user
4. Prices options using Black-Scholes.
5. Solves for the implied volatility on every strike within the chain
6. Compares implied volatility against 30-day realized volatility forecast
7. Computes all five greeks with more simplified interpretation
8. Visualises the volatility smile, edge by strike, and delta curve

##The Main Idea

Black-Scholes is a tool to translate a given volatility into the options price. The market has a volatility forecast embedded within each option price. If your own forecast of volatility is more accurate than the markets, an edge to obtain financial advantage reveals itself.

## Project Structure
black-scholes-pricer/
│
├── src/
│   └── black_scholes.py         # Core pricing engine
│                                  # d1, d2, call, put, Greeks,
│                                  # IV solver, options chain
│
├── black-scholes.ipynb          # Full analysis built step by step
│                                  # with explanation at every stage
│
├── black-scholes-interact.ipynb # Interactive version — input any
│                                  # ticker and get a full analysis
│
├── black_scholes_chart.png      # Sample output — AAPL analysis
|
└── README.md
