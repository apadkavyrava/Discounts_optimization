📌 Business Context
The application periodically emails users with discount offers. The goal is to offer the smallest possible discount that still yields a high probability of purchase.

🧠 Solution Overview
The repository contains a two-stage pipeline that tailors email discounts on a per-user basis:

Purchase Probability Model (XGBoost)
Predicts the likelihood that a user will buy given a specific discount.

Discount Grid Search
Sweeps through candidate discounts and selects the minimum one that reaches the desired purchase-probability threshold.

➡️ This results in a focused mailing list containing only those users who are both likely to convert and the discount percentage required to nudge them over the line.

📁 Repository Structure
bash
Copy
Edit
Discount_Optimization/
├── Raw_data/              # Original data provided for the project
├── Analisis/              # Notebooks for data cleaning and baseline dataset creation
├── Train_model/           # Training logic for purchase model and discount optimizer
├── Project_datasets/      # Intermediate and final CSV files used throughout the project
├── Inference/             # Production-ready inference scripts (.py files)
│   └── Prod_model/        # Packaged model code for deployment
└── README.md              # Project overview
