# Ashley Doan 
### Research question



"What is the impact of minimum wage increases on employment rates in the retail and service sectors across U.S. states between 2010 and 2020?"
- Focus: Retail and service sectors (sectors often employing minimum wage workers)
- Timeframe: 2010–2020 
- Geographic Scope: U.S. states 

### Data
Minimum Wage Data:
  - Source: U.S. Department of Labor (DOL) 

Employment Data:
  - Source: U.S. Bureau of Labor Statistics (BLS)
  - Details: State-level employment data (employment rate, unemployment rate, part-time/full-time employment) for specific sectors (e.g., retail, food services).

Demographic data:
  - Source: U.S. Census Bureau’s American Community Survey (ACS)
  - Details: age distribution, gender, and education levels (my analysis will properly control for population differences across states).
 
### EDA 
Descriptive Statistics:

- Calculate mean, median, and variance of minimum wage levels and employment rates by state and sector.
- Analyze trends in minimum wage changes across states.
- Check employment rate changes pre- and post-minimum wage hikes.

Visualization:
- Time-series plots showing changes in minimum wage and employment rates.
- Correlation heatmaps between minimum wage levels and employment rates.
- Box plots comparing employment rates across states with different wage levels.


### Difference-in-difference (DID) regression 
This approach will allow me to estimate the causal impact of minimum wage increases by comparing employment rates in states that raised the minimum wage (treatment group) with those that did not (control group). After running the model, I’ll conduct robustness checks to ensure the reliability of my results. 

### Conclusion
This project will help understand the trade-offs between wage policies and employment, particularly in low-wage sectors, and provide evidence for or against minimum wage increases as a tool for economic policy.








