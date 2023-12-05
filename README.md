# Final-Project
# Anna Carmody, Rafi Dahdal, and Jacob Stanley

## Project Description
### Questions of Interest
- Our first question is: how does average salary change over time and/or based on job title? This question highlights that we want to discover insights into overall global payment trends and valuation of certain careers (Vazquez). 
- Our second question is: how does the size of a company impact the average salary of a worker? This question sheds light on the relationship between company size and worker compensation, as large companies generally offer “higher salaries and bonuses” (Hering).

## Data Decription & Upload:
We are using the salaries.csv dataset from Kaggle, which was retrieved from the website ai-jobs.net, which gathers salary data from professionals worldwide in the fields of AI, machine learning, and data science. The main objective of the website is to provide data that can offer improved insights into global compensation trends (Vazquez). 
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
### Visualization 2:
![Viz2](https://github.com/acarmody2/Final-Project/assets/152214854/b577d7a6-d3cf-465e-99e5-fb933f8d106c)
In the above visualization, it is evident that managerial positions within the field of data commanded the highest global salaries on average. These include roles such as manager, tech lead, director, and positions with titles like "head of." Notably, data architects also enjoyed higher average compensation compared to engineers or scientists, a trend that may be attributed to the scarcity of such roles in the job market or the specialized skill set required. Roles related to data science or cloud computing consistently boasted higher average salaries when compared to positions in machine learning or research. This pattern underscores the demand for skills associated with data science and cloud technologies in the current job landscape.
### Visualization 3:
![VIZ3](https://github.com/acarmody2/Final-Project/assets/152214854/0709c4f4-a4a9-49bf-9424-124497c067a7)
In the above visualization, it is evident that both large and medium-sized companies offer higher average salaries than smaller companies. Interestingly, medium-sized companies outpaced large companies in average salaries, registering around $150,000 in contrast to approximately $135,000 for large companies. This discrepancy might be attributed to the possibility that larger companies, on average, have a higher number of employees, which could impact their allocation of resources and constrain individual employee budgets.

##  Discussion & Summary
### Chat-GPT4 Prompting & Response:
Our team used Chat-GPT4 to examine an article and answer the same questions of interest for our project to compare responses and see if our findings aligned. 
- Prompted Chat-GPT4 by asking: Based on this article: [LINK](https://365datascience.com/career-advice/data-science-salaries-around-the-world/) how does average salary change over time and/or based on job title? And how does the size of a company impact the average salary of a worker?
- Chat-GPT4's response: The article does not provide specific information on how average salary changes over time or based on job title. However, it does mention that data science salaries can vary greatly depending on the level of expertise, industry, and location. As for the impact of the size of a company on the average salary of a worker, the article states that larger companies tend to pay more. This is because they have more resources and can afford to pay higher salaries. However, smaller companies and startups may offer other benefits such as equity or a more flexible work environment. It's also important to note that the article mentions that the highest paying industries for data science professionals are finance and healthcare, while the lowest paying industries are education and government. In terms of location, the article states that the United States pays the highest salaries for data science professionals, followed by Australia and Canada. Please note that these are general trends and actual salaries can vary based on a variety of factors.
### Discussion
Chat-GPT4 and the article state that the impact of the company size on the average salary of a worker is that larger companies tend to pay more than smaller companies. This differs from our dataset and visualizations, where medium-sized companies tend to pay the most comparatively. However, our dataset and the response aligned in that larger companies tend to pay more than small companies. 
Another exciting aspect of Chat-GPT4 and our article's findings compared to our own is that they mentioned that the highest-paying industries for data science professionals are finance and healthcare, and education and government are the lowest-paying industries for data scientists. This information could work well in collaboration with our findings for job titles concerning salary. Thus, a salary for an individual in the finance and healthcare industry with the job titles of manager, tech lead, director, or "head of " are probably among the highest earners in the data science field. 
Finally, another way that our dataset and this article/ Chat-GPT4 differ is through location information. Chat-GPT4 found that the highest salaries for data science professionals are in the United States, followed by Australia and Canada. Again, our dataset did not have identical location information compared to salaries. Still, we found that the global salary for data science professionals has been rising for many years. Notably, with 2023, being the highest global average salary yet in this field being about $155,000. 
We wonder if the United States, Australia, and Canada have the highest salaries because they have more individuals with job titles of manager, tech lead, director, or "head of. Similarly, we also are intrigued if these three locations also have more finance and healthcare industry opportunities for data scientists as these were some of the highest paying industries. Overall, we found this article to be highly informative and interesting in relation to our dataset and findings.

