# Market Segmentation in Insurance

### Objective  :
This case requires to develop a customer segmentation to give recommendations like saving plans, loans, wealth management, etc. on target customer groups.

 Based on the customers features Ml model will recommends, saving plans, loans ,wealth....

 ### Features Description

```
BALANCE_FREQUENCY:  How often different amounts of money(balances) appear in the dataset of bank accounts.

ONEOFF_PURCHASE: how much money or how many items customers bought in a single transaction.

INSTALLMENTS_PURCHASES: shows how much money or how many items customers bought using installment payments (paying in parts over time).

CASH_ADVANCE: refers to the amount of cash that customers withdraw or borrow from their credit account.

CREDIT_LIMIT: is the maximum amount of money a customer can borrow on their credit account.

PURCHASES_FREQUENCY: tells us how often(many times or frequently) customers buy stuff.

ONEOFF_PURCHASES_FREQUENCY:tells us how often customers make single, one-time purchases.

PURCHASES_INSTALLMENTS_FREQUENCY: shows how often customers make purchases using installment payments.

CASH_ADVANCE_FREQUENCY: shows how often customers take out cash advances from their credit account.

CASH_ADVANCE_TRX: represents the number of transactions where customers took out cash advances from their credit account.

PURCHASES_TRX: stands for the number of transactions where customers made purchases.

PAYMENTS: is the money customers have paid to their credit card.

MINIMUM_PAYMENTS: is the smallest amount of money customers need to pay on their credit card each month.

PRC_FULL_PAYMENT: shows the percentage of the credit card balance that customers pay off completely each month.
```

### Data Description : 
The sample Dataset summarizes the usage behavior of about 9000 active credit card holders during the last 6 months. The file is at a customer level with 18 behavioral variables.
### Data :  
Use the below link to download the Data Set:[here](https://github.com/pik1989/MarketSegmentation/blob/main/Clustered_Customer_Data.csv) 
### Algorithms used :  
In this dataset i've used five clustering algorithm to perform segmentation.These algorithms are given below.
- [K-Means Clustering](https://en.wikipedia.org/wiki/K-means_clustering)
### Final Model  :
We have created a Flask Application based on this clustering technique, where we are taking the customer details & identifying which cluster the custoemr belongs to.



### All Ml Algorithms used in this project
```
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as pt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix,accuracy_score,f1_score,classification_report
import warnings
warnings.filterwarnings('ignore')
```

```bash
  git clone https://github.com/vishnucipher/CUSTOMER SEGMENTATION.git
```

Go to the project directory

```bash
  cd CUSTOMER SEGMENTATION
```

Install dependencies

```bash
  
  pip install pandas
  pip install scikit-learn
  pip install matplotlib
  pip install seaborn
  
```

Start 

```bash
  python3 app.py
```

## Documentation

### The Documetations of all Libraries which are used in this project

[Pandas](https://pandas.pydata.org/docs/)


[Seaborn](https://seaborn.pydata.org/tutorial/introduction)

[Matplotlib](https://matplotlib.org/stable/tutorials/introductory/quick_start.html)
## Other Common Github Profile Sections
👩‍💻 I'm currently working on Machine-Learning Projects





📫 How to reach me **vishnuvardhankalva8@gmail.com**

⚡ Fun fact **I listen songs 8hours per day😆**



### 🛠 Skills
- **Python**
- **Machine-Learning**
- **Data Visualization**
- **Data Preprocessing**
- **Model Building**
- **Undesrstanding the Features in Dataset**
