# Adidas Sales Exploratory Analysis
## Sales Mix, Product Performance, and Introductory Statistical Analysis

## Overview
This repository contains a legacy educational analysis of Adidas US sales records from 2020 to 2021 using Python for:
- data preparation;
- exploratory analysis;
- aggregation;
- visualization;
- introductory statistical testing.

## Dataset
The dataset used in this analysis is provided on [Kaggle](https://www.kaggle.com/datasets/heemalichaudhari/adidas-sales-dataset). After the analytical data preparation, the dataset consists of:
- **9,648 analytical records**
- **13 analytical columns**
- **Date range**: January 1, 2020 through December 31, 2021
- **6 retailers**
- **5 regions**
- **6 product categories**
- **3 sales methods**

## Questions Explored
- Which products recorded the most units sold and operating profit?
- How do sales methods vary across retailers and regions?
- How does operating profit differ between records above and below the overall average unit price?
- What exploratory relationship appears between Price per Unit and Total Sales?
- Does the deterministic 1,000-record sample provide evidence that mean Operating Profit exceeds 40,000?

## Methods
- Excel data cleaning
- pandas aggregation
- descriptive statistics
- visualization
- correlation heatmap
- scatter plot with regression trend line
- one-sample t-test

## Key Findings
### Men's Street Footwear
Men's Street Footwear recorded **593,320 units sold** and ranked highest by units sold in the product aggregation.

### Pricing / profit association
An observed descriptive association shows that records grouped into the "Above Average" price category have a higher average Operating Profit compared to records in the "Below Average" price category. *Note: Product mix, units sold, retailer, region, and other factors are not controlled for.*

### Midwest / Southeast online sales method
Online is the largest share of records by Sales Method in the following regions:
- Midwest: approximately 62.2%
- Southeast: approximately 64.7%

### Hypothesis test
A deterministic 1,000-record sample was drawn to test if the mean Operating Profit is greater than 40,000.
- **Sample Mean:** 33,613.355
- **Test Statistic:** -3.655
- **p-value:** 1.000
- **Decision:** Since the p-value is greater than our alpha (0.05), we fail to reject the null hypothesis. The sample does not provide evidence that the mean Operating Profit exceeds 40,000.

## Business Questions for Further Testing
Based on the exploratory analysis, the following questions could be investigated in future tests:
- Do higher-price product segments remain more profitable after controlling for product mix and units sold?
- Could discounting low-performing products actually increase volume or contribution profit?
- Does the strong historical online channel mix in the Midwest and Southeast represent an expansion opportunity?

## Reproducibility
To run the notebook locally from the repository root, install the required dependencies:

```bash
pip install pandas numpy matplotlib seaborn scipy openpyxl
```

Then, you can execute `Adidas_Sales_Analysis.ipynb` using Jupyter.

## Contact
If you have any questions or feedback regarding this analysis, please contact me via Linkedin:

**Linkedin** : https://www.linkedin.com/in/farizalfitra/

I hope this project can provide benefits to anyone who reads it, especially for you who are just interested in getting into the world of data. 
Thank You! Have a Nice day!
