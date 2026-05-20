import numpy as np #array operations
from scipy.stats import norm #normal distribution functions
from scipy.optimize import brentq #root finding for implied volatility
from scipy.stats import norm

def d1(S,K,T,r,sigma):
    return (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
def d2(S,K,T,r,sigma):
    return d1(S,K,T,r,sigma) - sigma * np.sqrt(T)
def call_price(S,K,T,r,sigma):
    return S * norm.cdf(d1(S,K,T,r,sigma)) - K * np.exp(-r*T) * norm.cdf(d2(S,K,T,r,sigma))
def put_price(S,K,T,r,sigma):
    return K * np.exp(-r*T) * norm.cdf(-d2(S,K,T,r,sigma)) - S * norm.cdf(-d1(S,K,T,r,sigma))

#defining Delta 
def delta(S,K,T,r,sigma,option_type='call'):
    if option_type == 'call':
        return norm.cdf(d1(S,K,T,r,sigma))
    elif option_type == 'put':
        return norm.cdf(d1(S,K,T,r,sigma)) - 1
    else:
        raise ValueError("option_type must be 'call' or 'put'")

# defining Gamma
def gamma(S,K,T,r,sigma):
    return norm.pdf(d1(S,K,T,r,sigma)) / (S * sigma * np.sqrt(T))
#Defining theta
def theta(S,K,T,r,sigma,option_type='call'):
    if option_type == 'call':
        return (-S * norm.pdf(d1(S,K,T,r,sigma)) * sigma / (2 * np.sqrt(T)) 
                - r * K * np.exp(-r*T) * norm.cdf(d2(S,K,T,r,sigma)))
    elif option_type == 'put':
        return (-S * norm.pdf(d1(S,K,T,r,sigma)) * sigma / (2 * np.sqrt(T)) 
                + r * K * np.exp(-r*T) * norm.cdf(-d2(S,K,T,r,sigma)))
    else:
        raise ValueError("option_type must be 'call' or 'put'")

# defining Vega
def vega(S,K,T,r,sigma):
    return S * norm.pdf(d1(S,K,T,r,sigma)) * np.sqrt(T) / 100

#defining Rho
def rho(S,K,T,r,sigma,option_type='call'):
    if option_type == 'call':
        return K * T * np.exp(-r*T) * norm.cdf(d2(S,K,T,r,sigma)) / 100
    elif option_type == 'put':
        return -K * T * np.exp(-r*T) * norm.cdf(-d2(S,K,T,r,sigma)) / 100
    else:
        raise ValueError("option_type must be 'call' or 'put'")

def implied_volatility(market_price, S, K, T, r, option_type="call"):
    if option_type == "call":
        intrinsic = max(S - K * np.exp(-r * T), 0)
        price_fn  = call_price
    else:
        intrinsic = max(K * np.exp(-r * T) - S, 0)
        price_fn  = put_price
    
    # Can't solve if price is below intrinsic value
    if market_price <= intrinsic:
        return np.nan
    
    # Objective function — we want this to equal zero
    objective = lambda sigma: price_fn(S, K, T, r, sigma) - market_price
    
    try:
        iv = brentq(objective, 1e-6, 10.0, xtol=1e-6, maxiter=500)
        return round(iv, 6)
    except ValueError:
        return np.nan