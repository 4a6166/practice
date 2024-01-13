# example from https://pbpython.com/monte-carlo.html

import pandas as pd
import numpy as np
import seaborn as sns

sns.set_style('whitegrid')

## BACKGROUND
# Example data looks like this:
# | Sales Rep | Sales Target | Actual Sales | Percent to Plan | Commission Rate | Commission Amount |
# | 0         | $0,000       | $0.00        | 00.0%           | 0.0%            | $0,000            |
# | Calcs     | -            | -            | AS/ST           | Calc(%TP)       | CR*AS             |
# | ---       | ---          | ---          | ---             | ---             | ---               |
# | 1         | $100,000     | $95,000      | 95.0%           | 3.0%            | $2,850            |
# | 2         | $200,000     | $204,000     | 102.0%          | 4.0%            | $8,160            |
# | 3         | $75,000      | $60,000      | 80.0%           | 2.0%            | $1,200            |
# | 4         | $400,000     | $480,000     | 120.0%          | 4.0%            | $19,200           |
# | 5         | $500,000     | $400,000     | 80.0%           | 2.0%            | $8,000            |
# | -         | -            | -            | -               | -               | -                 |
# | Total     | $1,275,000   | $1,239,000   | -               | -               | $39,410           |

## mean and std_dev from "historical sources"
avg = 1
std_dev = .1
num_reps = 500
num_simulations = 1000
sales_target_values = [75_000, 100_000, 200_000, 300_000, 400_000, 500_000]
sales_target_prob = [.3, .3, .2, .1, .05, .05]

all_stats = []

for i in range(num_simulations):

    ## Assumption: Normal distribution
    pct_to_target = np.random.normal(avg, std_dev, num_reps).round(2)
    # print (pct_to_target[:10]) # pulse check: get first 10 numbers

    ## Assumption: Non-normal distribution example. Woudl normally need to get from historical or hand-wave with assumptions
    sales_target = np.random.choice(sales_target_values, num_reps, p=sales_target_prob)

    ## Building the pandas dataframe
    df = pd.DataFrame(index=range(num_reps), data={'Pct_To_Target': pct_to_target,
                                                   'Sales_Target': sales_target})
    ## backing into the actual sales from ranomly generated data
    df['Sales'] = df['Pct_To_Target'] * df['Sales_Target']

    def calc_commission_rate(x):
        # Return the commission rate based on the table:
        # 0-90% => 2%
        # 91-99% => 3%
        # >= 100 => 4%

        if x <= .90:
            return .02
        if x <= .99:
            return .03
        else:
            return .04

    df['Commission_Rate'] = df['Pct_To_Target'].apply(calc_commission_rate)
    df['Commission_Amount'] = df['Commission_Rate']*df['Sales']

    # print(df) # At this point we have one MC iteration
    # print(df['Commission_Amount'].sum())
    all_stats.append([df['Sales'].sum().round(0),
                      df['Commission_Amount'].sum().round(0),
                      df['Sales_Target'].sum().round(0)
                      ])

result_df = pd.DataFrame(all_stats, columns=['Sales',
                                             'Commission_Amount',
                                             'Sales_Target'
                                             ])

# print(result_df.describe()) # prints out in scientific notation
# result_df.describe().style.format('{:,}') # does not work
# print(result_df.describe().apply('{:,}'.format)) # does not work

## This one prints nicely
pd.set_option('display.float_format', lambda x: '{:,}'.format(int(x)))
print(result_df.describe())
println()

# print(result_df.describe().applymap(lambda x: f"${x:,}"))
# print(result_df.describe().applymap(lambda x: f"${x:0.2f}"))
print(result_df.style.format({
    'Sales': '{:,.0f}',
    'Commission_Amount': '{:,.0f}',
    'Sales_Target': '{:,.0f}'
    }))
