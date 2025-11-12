# Predictive Anime Recommender with Hype Detection: HypeBlend

A modern hybrid recommendation system that blends Collaborative Filtering with a real-time Social Hype Detector to recommend relevant and trending anime.

-----

## 🛠️ Technology Stack

| Core Language | Backend | ML/Recommenders | Data/NLP | Visualization | Utilities |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  |  |  |
| | |  |  |  |  |
| | |  |  |  | |
| | |  | | | |

-----

## Table of Contents

1.  [About the Project](https://www.google.com/search?q=%231-about-the-project)
2.  [Features](https://www.google.com/search?q=%232-features)
3.  [Project Structure](https://www.google.com/search?q=%233-project-structure)
4.  [Technologies Used](https://www.google.com/search?q=%234-technologies-used)
5.  [Setup and Installation](https://www.google.com/search?q=%235-setup-and-installation)
6.  [Usage](https://www.google.com/search?q=%236-usage)
7.  [Output Screenshots](https://www.google.com/search?q=%237-output-screenshots)
8.  [License](https://www.google.com/search?q=%238-license)

-----

## 1\. About the Project

This project implements a unique **Hybrid Recommendation Engine** designed to solve the "cold start" and "discovery" problems in media recommendation. The system provides:

1.  **Personalization:** Based on user history (Collaborative Filtering).
2.  **Trend-Awareness:** Boosted by the current community sentiment and discussion volume ("Hype Score").

The data pipeline runs on Python, the model is served by a lightweight Flask API, and the results are presented in a high-contrast, dark-mode dashboard styled to be visually impactful and easily understood.

## 2\. Features

  * **Hybrid Engine:** Uses **SVD (Surprise)** for collaborative filtering, dynamically adjusted by the real-time Hype Score.
  * **Hype Detector:** Collects raw commentary data from the **Reddit API (PRAW)** and uses **TextBlob** for sentiment analysis to quantify current trends.
  * **Interactive Dashboard:** A visually attractive frontend using **Chart.js** to display key metrics (Total Items, Top Genres) and the Hype Ranking.
  * **Secure Configuration:** Uses **python-dotenv** and `.gitignore` to secure API keys and suppress sensitive data.

## 3\. Project Structure

The project follows a standard Flask/ML structure, separating data, models, and application logic (`src`).

```
.
├── data/                      # Stores raw/processed data (e.g., ratings.csv)
├── models/                    # Stores trained machine learning models
├── src/                       # Source code for pipeline scripts
│   ├── api_collector.py
│   ├── data_processing.py
│   ├── hype_detector.py
│   └── recommender_model.py
├── templates/                 # Frontend HTML templates
│   ├── index.html
│   └── trends.html (Dark Dashboard)
├── venv/                      # (Ignored)
├── .env                       # (Ignored)
├── app.py                     # Main Flask Application
└── requirements.txt
```

## 4\. Technologies Used

| Category | Library | Purpose |
| :--- | :--- | :--- |
| **Backend/Web** | **Flask** | Lightweight framework for serving the API and web pages. |
| **ML/Data Core** | **Pandas** | Efficient data manipulation and aggregation. |
| | **NumPy (\<2.0)** | Fundamental library for numerical operations. |
| | **Surprise** | Specialized library for Collaborative Filtering (SVD). |
| **Data/NLP** | **requests** | HTTP requests for the Jikan API. |
| | **PRAW** | Python Reddit API Wrapper for social data collection. |
| | **TextBlob** | Fast sentiment analysis (polarity) for social comments. |
| **Utilities** | **joblib** | Efficient serialization (saving/loading) of ML assets. |
| | **python-dotenv** | Loads secrets from the `.env` file securely. |
| **Frontend/Viz** | **Chart.js** | Dynamic, responsive charting on the frontend dashboard. |

### APIs Used

  * **Jikan API (v4)**: Fetches official anime metadata (Scores, Genres, Titles).
  * **Reddit API**: Accessed via PRAW for real-time community sentiment and volume.

## 5\. Setup and Installation

### Prerequisites

  * Python 3.9+
  * Reddit API Credentials (for `.env`)

### Installation Steps

1.  **Clone the Repo:**
    ```bash
    git clone YOUR_REPO_URL
    cd predictive-recommender
    ```
2.  **Create and Activate Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Secrets:** Create a `.env` file in the root directory with your API keys.

### Run Data Pipeline

Execute these scripts sequentially to prepare all data and models:

```bash
python src/api_collector.py
python src/data_processing.py
python src/hype_detector.py
python src/recommender_model.py
```

## 6\. Usage

### Starting the Flask Application

```bash
python app.py
```

The application will run on `http://127.0.0.1:5000/`.

  * **Recommendations:** `http://127.0.0.1:5000/`
  * **Hype Trends Dashboard:** `http://127.0.0.1:5000/trends`

## 7\. Output Screenshots

(Paste your two finalized images here—one for the recommendation table, one for the dark dashboard.)

-----

## 8\. License

This project is licensed under the MIT License.

<br>

\<div align="center"\>
\<h3\>Built by Luana K. Ribeiro\</h3\>
\<a href="[https://www.linkedin.com/in/ataidekaroline/](https://www.linkedin.com/in/ataidekaroline/)" target="\_blank"\>
\<img src="[https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge\&logo=linkedin\&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/LinkedIn-0077B5%3Fstyle%3Dfor-the-badge%26logo%3Dlinkedin%26logoColor%3Dwhite)" alt="LinkedIn Profile"\>
\</a\>
\</div\>
