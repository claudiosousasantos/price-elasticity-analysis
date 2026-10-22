# Price Elasticity Analysis

A Python script that estimates how sensitive customer demand is to price changes, then uses that estimate to simulate a pricing decision.

## How it works
- Takes historical prices and quantities sold
- Calculates the percentage change in price and in quantity between each period
- Divides the quantity change by the price change to get the elasticity for each period, then averages them
- Classifies demand: below -1 is elastic (customers react strongly to price), between -1 and 0 is inelastic (customers barely react)
- Simulates a proposed price change: estimates the new quantity and compares projected revenue to current revenue

## Example result
With the sample data, average elasticity is about -2.18 (elastic). A 10% price increase is projected to cut quantity by roughly 22%, so revenue falls from $9,800 to about $8,400. For elastic demand, raising prices loses more in volume than it gains in price.

## How to run
```bash
python price_elasticity.py
```

## What I learned
- Using `np.diff()` to get the change between consecutive values
- Using slicing (`prices[:-1]`) to line up each change with its starting value
- Dividing whole arrays at once to calculate every period's elasticity without a loop
- What elastic vs. inelastic demand means, and why it decides whether a price increase helps or hurts revenue
- Turning a statistic into a what-if simulation for a business decision

## Limitations
- Six data points is a very small sample, and the periods vary a lot (elasticity ranges from about -1.25 to -3.57).
- It assumes elasticity stays constant and that price is the only thing affecting sales. Seasonality, promotions, and competitors are ignored.
- Averaging per-period ratios is a simple method. A log-log regression across all the data is the more standard approach.

## Dependencies
Requires NumPy:
```bash
pip install numpy
```
