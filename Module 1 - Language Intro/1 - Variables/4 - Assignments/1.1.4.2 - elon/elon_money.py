"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

# Elon Musk's available capital
initial_investment = 33_000_000_000  # $33 billion

# Annual Treasury bond interest rates
ten_year_rate = 0.0396    # 3.96%
twenty_year_rate = 0.0432 # 4.32%

# Investment periods
ten_years = 10
twenty_years = 20

# Calculate future value using annual compounding
ten_year_final = initial_investment * (1 + ten_year_rate) ** ten_years

twenty_year_final = initial_investment * (1 + twenty_year_rate) ** twenty_years

# Display results
print("10-year final value: $", ten_year_final)
print("20-year final value: $", twenty_year_final)


# final answer for 10-year
ten_year_final = 48660509081.78675

# final answer for 20-year
twenty_year_final = 76889229275.98897
