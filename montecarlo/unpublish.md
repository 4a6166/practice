## Monte Carlo notes

**To set up, find what conditions trigger a "success" condition and divide number of successes by number of trials**

Need to have probability values, map randomly distributed numbers to a probability value

To determine probability where it isn't explicit:
Guestimate using three point estimation and PERT formula.
Example: time required to complete a project

1. Fill in this table

| Activities         | Optimistic   | Pessimistic   | Most Likely   |
| ------------------ | ------------ | ------------- | ------------- |
| Choose Topic       | 4            | 7             | 5             |
| Develop Plan       | 5            | 7             | 6             |
| Complete Plan      | 7            | 9             | 8             |
| Write Report       | 2            | 4             | 3             |

2. Calculate the PERT estimate (Optimistic + (4 * Most Likely) + Pessimistic)/6

| Activities         | Optimistic   | Pessimistic   | Most Likely   | PERT Estimate |
| ------------------ | ------------ | ------------- | ------------- | ------------- |
| Choose Topic       | 4            | 7             | 5             | 5.2           |
| Develop Plan       | 5            | 7             | 6             | 6             |
| Complete Plan      | 7            | 9             | 8             | 8             |
| Write Report       | 2            | 4             | 3             | 3             |

## Go notes

Go packages are not working as I intend. Consider rewriting in python or Lua for reusable/portable modules.
