# Final-Project
# Anna Carmody, Rafi Dahdal, and Jacob Stanley

## Project Description
### Questions of Interest
- Our first question is: how does average salary change over time and/or based on job title? This question highlights that we want to discover insights into overall global payment trends and valuation of certain careers (Vazquez). 
- Our second question is: how does the size of a company impact the average salary of a worker? This question sheds light on the relationship between company size and worker compensation, as large companies generally offer “higher salaries and bonuses” (Hering).

  ## Data Decription & Upload:
  We are using the salaries.csv dataset from Kaggle, which was retrieved from the website ai-jobs.net, which gathers salary data from professionals worldwide in the fields of AI, machine learning, and data science.
  The main objective of the website is to provide data that can offer improved insights into global compensation trends (Vazquez). 
  The dataset can be downloaded using the following link: [LINK](https://www.kaggle.com/datasets/lorenzovzquez/data-jobs-salaries). 
  The dataset has eleven total columns, but we will use the following four columns in our analysis: work_year, job_title, salary_in_usd, and company_size. See the descriptions and data types of these variables below:
  - work_year: The year the salary was paid (integer) - We will change the data type from an integer to an object
  - job_title: The role worked in during the year (object)
  - salary_in_usd: The salary in USD (FX rate divided by avg. USD rate of respective year via data from fxdata.foorilla.com) (integer)
  - company_size: The average number of people that worked for the company during the year (object)
      - S: less than 50 employees (small)
      - M: 50 to 250 employees (medium)
      - L: more than 250 employees (large)
  ## Interpreting Visualizations
  ### Visualization 1:
  ![pic](https://github.com/acarmody2/Final-Project/assets/152214854/06aeb519-2cf6-4b89-bab2-1599a955f449)
  In the above visualization, the global average salary was about $103,000 at the beginning of 2020 then fell slightly to about $100,000 by the start of 2021. From the start of 2021 to the start of 2022, global average salary rose sharply to about $135,000. From the start of 2022 to the start of 2023, global average salary rose to about $155,000 but not as sharply. The fluctuations in global average salaries can be attributed to the impacts of the COVID-19 pandemic. The initial decline and low average salaries overall likely resulted from widespread unemployment during the pandemic. The subsequent lifting of pandemic restrictions in 2021 and 2022 provides an explanation for the rise in global average salaries.

