# Data Collection & Prediction Project

## Project Overview
This project aims to collect, structure, and analyze a dataset that will be used for predictive modeling in the next phase. The dataset must be sourced from an API or web scraping and should not be an already formatted CSV file. The collected data will undergo exploration and transformation before being used for machine learning predictions.

## Repository Structure
```
├── data
│   ├── raw_data.csv  # Unprocessed dataset
│   ├── processed_data.csv  # Cleaned and transformed dataset
│
├── notebooks
│   ├── [team_member_1]_eda.ipynb  # Exploratory Data Analysis (EDA)
│   ├── [team_member_2]_eda.ipynb
    ├── [team_member_2]_eda.ipynb
│
├── scripts
│   ├── data_ingestion.py  # API call or web scraping script to collect data
│
├── README.md  # Project documentation
```

## Data Collection
- **Source:** [Specify the API or website used for scraping]
- **Format:** Unstructured or semi-structured
- **Dataset Size:** More than 1000 rows

## Analytical Questions
1. **What does your dataset explore?**
   - [Provide a brief description of the dataset and its context]
2. **What is your dependent variable?**
   - [Specify the target variable]
3. **Is this variable categorical or quantitative?**
   - [Indicate the type]
4. **What are your independent variables?**
   - [List the independent variables]
5. **Are these variables quantitative or categorical?**
   - [Ensure a mix of both types]
6. **How many independent variables do you have?**
   - [Specify the count, ensuring more than 5]
7. **How large is your dataset?**
   - [Confirm dataset size is greater than 1000 rows]

## Collaboration Guidelines
- **GitHub Repository:** [Provide the repository link]
- **Folder Organization:** Follow the structure outlined above.
- **Code Sharing:** Team members will directly commit to the main branch without using branches.
- **Exploratory Data Analysis:** Each team member will conduct independent EDA and document findings in separate notebooks.

## Next Steps
- **Data Collection:** Use `data_ingestion.py` to fetch and store raw data.
- **EDA:** Perform initial analysis on the dataset.
- **Data Transformation:** Clean and prepare data for predictive modeling.

## References
- Data from: https://data.cityofnewyork.us/Housing-Development/Affordable-Housing-Production-by-Project/hq68-rnsi/about_data

---
This README will be updated as the project progresses.

