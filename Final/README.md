### Margaret Nguyen & Munkhtsatsral Batdelger  
### Read Me File for DATA 400 Project  

## Predicting Student and Professor Diversity Scores: Analysis and Methodology

### I. Description
Our project aims to predict the ethnicity diversity score of a university by comparing:  
- The number of non-white students to the total number of students.  
- The number of non-white professors to the total number of professors.   

We focus on undergraduate students pursuing bachelor’s degrees and build two machine-learning models: one for National Universities and another for Liberal Arts Colleges.  

Our analysis covers ten years, specifically from the 2012-2013 academic year to the 2021-2022 academic year.  
- **Dependent variable**: Student diversity score.  
- **Independent variables**: Major composition, location, gender, professor salaries, instructional staff gender and race, endowment and financial aid, graduation rate, student-to-faculty ratio, total number of undergraduates in the financial aid cohort, and college ranking.  

---

### II. Data Retrieval

#### Primary Dataset: IPEDS Completion Data  
The Integrated Postsecondary Education Data System (IPEDS) collects 12 interrelated survey components annually from colleges and universities participating in federal student financial aid programs.  

#### Secondary Dataset: U.S. News & World Report Historical Rankings  
The U.S. News dataset ranks nearly 1,500 U.S. four-year bachelor’s degree-granting institutions. Data was sourced from Andrew G. Reiter’s dataset collection:  
[Andrew G. Reiter’s Datasets](https://andyreiter.com/datasets/)  

- Includes data for 189 National Universities and 380 Liberal Arts Colleges, categorized by U.S. News.  

---

#### 1. To Obtain Variables:  

- **Visit the IPEDS Data Center**: [IPEDS Data Center](https://nces.ed.gov/ipeds/datacenter/Default.aspx?gotoReportId=7&fromIpeds=true)  
- **Steps for Data Access**:  
  - Select the specific year (2012–2022) using the dropdown menu and press "Continue."  
  - Download files for each survey:  
    - **Institutional Characteristics**: `HD2013` or corresponding year.  
    - **12-Month Enrollment**: `EFFY2013` or corresponding year.  
    - **Fall Enrollment**: `EF2013D` or corresponding year.  
    - **Completions**: `C2013_A` or corresponding year.  
    - **Instructional Staff/Salaries**: `SAL2013_IS` or corresponding year.  
    - **Fall Staff**: `S2013_IS` or corresponding year.  
    - **Finance**:  
      - Private/Public (FASB): `F1213_F2`.  
      - Public (GASB): `F1213_F1A`.  
    - **Student Financial Aid and Net Price**: `SFA1213` or corresponding year.  
    - **Graduation Rates**: `GR2013` or corresponding year.  

---

#### 2. To Obtain College Rankings from 2012 to 2021:  

- **Visit Andrew G. Reiter’s Website**: [Andrew G. Reiter’s Datasets](https://andyreiter.com/datasets/)  
  - **Liberal Arts College Rankings**:  
    - Download: *US News National Liberal Arts College Rankings (Through 2025)*.  
  - **National University Rankings**:  
    - Download: *US News National University Rankings (Top 150) Through 2025*.  

#### Citation:  
Andrew G. Reiter, “U.S. News & World Report Historical Liberal Arts College and University Rankings,” available at: [http://andyreiter.com/datasets/](http://andyreiter.com/datasets/)  
IPEDS Data Center, available at: [https://nces.ed.gov/ipeds/datacenter/Default.aspx?gotoReportId=7&fromIpeds=true](https://nces.ed.gov/ipeds/datacenter/Default.aspx?gotoReportId=7&fromIpeds=true)

---

### III. Data Overview
For this project, we worked with 10 different datasets after cleaning and preprocessing the data.

#### National University Analysis
There are 5 primary datasets used for this analysis:

- **df_nu_final**: This dataset combines college characteristics and rankings from IPEDS data and US News data. It contains **126,445 rows × 50 columns**.

- **df_nu_stu_diversity_training**: This dataset includes data from 2012-2013 to 2020-2021, with **110,928 rows × 50 columns**, and is used to train the student diversity machine learning model.

- **df_nu_stu_diversity_test**: This dataset includes data from 2021-2022, with **14,028 rows × 50 columns**, and is used to test the student diversity machine learning model.

- **df_nu_prof_diversity_training**: This dataset includes data from 2012-2013 to 2020-2021, with **109,829 rows × 50 columns**, and is used to train the professor diversity machine learning model.

- **df_nu_prof_diversity_test**: This dataset includes data from 2021-2022, with **14,028 rows × 50 columns**, and is used to test the professor diversity machine learning model.

#### National Liberal Art College Analysis
There are 5 primary datasets used for this analysis:

- **df_lac_final**: This dataset combines college characteristics and rankings from IPEDS data and US News data. It contains **66,684 rows × 50 columns**.

- **df_lac_stu_diversity_training**: This dataset includes data from **2012-2013 to 2020-2021**, with **57,174 rows × 50 columns**, and is used to train the student diversity machine learning model.

- **df_lac_stu_diversity_test**: This dataset includes data from **2021-2022**, with **7,136 rows × 50 columns**, and is used to test the student diversity machine learning model.

- **df_lac_prof_diversity_training**: This dataset includes data from **2012-2013 to 2020-2021**, with **54,772 rows × 50 columns**, and is used to train the professor diversity machine learning model.

- **df_lac_prof_diversity_test**: This dataset includes data from **2021-2022**, with **7,163 rows × 50 columns**, and is used to test the professor diversity machine learning model.

---

### IV. Libraries
The following libraries are required for this project:

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error
import sys
```

### V. Methodology and Model Specification
We created two machine learning models: one to predict student diversity and another to predict professor diversity. The training datasets include data from 2012-2013 to 2020-2021, while the testing datasets include data from 2021-2022.

**Student Diversity Model**
The equation for the student diversity model is as follows:
$$
\text{stu\_diversity}_{jkt} = \beta_0 + \beta_1 \text{ranking}_{jkt} + \beta_2 \text{hbcu}_{jkt} + \beta_3 \text{pct\_retention}_{jkt} + \beta_4 \text{stu\_faculty\_ratio}_{jkt} + \beta_5 \text{beg\_endowment}_{jkt} + \beta_6 \text{stu\_financial\_aid}_{jkt} + \beta_7 \text{prof\_diversity}_{jkt} + \beta_8 \text{prop\_major}_{jkt} + \beta_9 \text{pct\_female\_stu}_{jkt} + \beta_{10} \text{pct\_male\_stu}_{jkt} + \beta_{11} \text{graduate\_female}_{jkt} + \beta_{12} \text{graduate\_male}_{jkt} + \beta_{13} \text{pct\_female\_prof\_salary}_{jkt} + \beta_{14} \text{pct\_male\_prof\_salary}_{jkt} + \alpha_k + \epsilon
$$

**Professor Diversity Model**
The equation for the professor diversity model is as follows:

$$
\text{prof\_diversity}_{jkt} = \beta_0 + \beta_1 \text{ranking}_{jkt} + \beta_2 \text{hbcu}_{jkt} + \beta_3 \text{pct\_retention}_{jkt} + \beta_4 \text{stu\_faculty\_ratio}_{jkt} + \beta_5 \text{beg\_endowment}_{jkt} + \beta_6 \text{stu\_financial\_aid}_{jkt} + \beta_7 \text{stu\_diversity}_{jkt} + \beta_8 \text{prop\_major}_{jkt} + \beta_9 \text{pct\_female\_stu}_{jkt} + \beta_{10} \text{pct\_male\_stu}_{jkt} + \beta_{11} \text{graduate\_female}_{jkt} + \beta_{12} \text{graduate\_male}_{jkt} + \beta_{13} \text{pct\_female\_prof\_salary}_{jkt} + \beta_{14} \text{pct\_male\_prof\_salary}_{jkt} + \alpha_k + \epsilon
$$