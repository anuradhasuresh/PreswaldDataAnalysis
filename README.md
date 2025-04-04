
# 📊 Preswald Project: Amazon Best Sellers Data Analysis

This project performs an interactive data analysis on the [Amazon Best Sellers Software dataset](https://www.kaggle.com/datasets/kaverappa/amazon-best-seller-softwares?resource=download), using **Preswald**, a Python-based framework for building and deploying data apps.

🔗 **Live App:** [View the Project](https://bestsellersdataproject-733268-qgzry0za.preswald.app)

---

## 🚀 Features

- Explore top-selling software products on Amazon
- Interactive charts (bar, pie, line plots)
- Country-wise product distribution
- Dynamic filtering and visualization
- Deployed using [Preswald](https://pypi.org/project/preswald/)

---

## 🛠️ Setup Instructions

1. **Clone the Repository**
   git clone <your-repo-url>
   cd <your-project-directory>

2. **Set Up Virtual Environment**
   python3 -m venv venv
   source venv/bin/activate

3. **Install Preswald**
   pip install preswald

4. **Configure Data Sources**
   - Edit `preswald.toml` with your database or file path settings.

5. **Store Secrets Securely**
   - Add API keys, DB passwords, or other credentials in `secrets.toml`.

6. **Run the App Locally**
   preswald run

---

## 📦 Dataset Info

- Source: Kaggle  
- Link: [Amazon Best Seller Software Dataset](https://www.kaggle.com/datasets/kaverappa/amazon-best-seller-softwares?resource=download)  
- Fields include: product name, price, category, country, reviews, rank, etc.

---

## 📈 Sample Visuals

- Pie Chart: Product Distribution by Country
- Bar Chart: Products with Highest Review Count
- Line Chart: Price Trends Across Categories

---

## 📌 Notes

- Make sure Docker is running on your machine if deploying locally with Preswald.
- Any `Bad Request` errors during deployment may require a Docker login.

## ✨ Live App

Check out the deployed version here:  
👉 [https://bestsellersdataproject-733268-qgzry0za.preswald.app](https://bestsellersdataproject-733268-qgzry0za.preswald.app)
