# Fixed Income Analytics and Backtests
I intend to put together a set of fixed income toolkits that help perform backtests.

**Yield Spreads Backtest:** https://github.com/vdp96/fixed_income/blob/main/yield_spread_steepening_strat.ipynb


## Yield Spread Back Test Work Flow and Description:

**Tech Used:** Python, Jupyter Notebook

**Timeframe:** 1984 - 2023

**Data Source:** https://www.federalreserve.gov/data/nominal-yield-curve.htm

Yield Curve data has been acquired from the link mentioned above

**Main Ideas and Assumptions:** 
- Positions are rebalanced weekly
- 2 year bonds for front leg and 10 year bond for back leg
- Positions are taken using leverage
- Cash position is invested/borrowed at 1 week rate
- PNL each week is reinvested into the strategy

## Backtest Conclusion:
1. Steepening Strategy has performed well over the 40 years. This is expected because long term bonds fluctuate higher than short term bonds in most of the market conditions.   
2. Flattening Strategy did not do well in buy and hold case implying that flattening strategy should only be implemented in certain market conditions like recession.