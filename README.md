# TASI_STOCKS_MOVING_AVERAGE
This code gets the data from an initial year up to a current day with moving average (MA) visualization.

The source code is based on Selenium to automatically control one's browser to open each stock on TASI in a single run. It forces a page on investing.com to display (open, close, highest, lowest, and change prices) and then it applies three moving average formulas (MA9, MA20, and MA50) to be plotted. The plots helps one to understand the status of each stock market instead of implementing MA manually on each stock. 

With all stocks on TASI plotted, the amount of time and efforts are shortened to help one to find the suitable stocks to implement other technical analysis.

## THE MOVING AVERAGE FORMULA

![alt text](https://www.orderhive.com/wp-content/uploads/2019/04/Moving-Average.png)

> A: is a single price in a day.<br>
> n: is the total number of As (MA are usually done via 9, 20, and 50 series of consecuative prices)<br>
> The formula above is done via the sum of As divided by their total number <br>
> FORMULA (A1 + A2 .......... An) / n <br>
> n here is the index of the last price to represent the total As above.

## EXAMPLE OF A RESULT IN A FIGURE: ARAMCO 2222

![alt text](https://i.ibb.co/fHdpF6B/Figure-2022-10-23-140843.png)

## COMPARE THE RESULT ABOVE WITH THIS EXAMPLE FROM TRADINGVIEW VIA ARGAAM.COM

![alt text](https://s3.tradingview.com/snapshots/n/nG7WNw2L.png)

< This example, which was resulted by tradingview analysis tools, is created indivisually. How long will this takes one to apply MA on the whole stocks on TASI?
