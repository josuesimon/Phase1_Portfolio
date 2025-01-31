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
   - This dataset explores HPD's efforts to finance affordable housing projects throughout NYC. It provides information such as project details, timeline, type, and number of units.
2. **What is your dependent variable? Is this variable categorical or quantitative?**
   - "Total Units" is a quantitative variable.
3. **What are your independent variables? Are these variables quantitative or categorical? How many independent variables do you have?**
   - Here are some of the independent variables:
Borough: (Categorical)
Reporting Construction Type: (Categorical)
Project Name: (Categorical)
Project Start Date: (Quantitative)
Project Completion Date: (Quantitative)
Community Board: (Categorical) 
Council District: (Categorical)
Latitude: (Quantitative)
Longitude: (Quantitative)
 Postcode: (Categorical)
4. **How large is your dataset?**
   - Our entire dataset has 3, 635 rows and 19 columns.

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

