
# Predictive Anime Recommender with Hype Detection: HypeBlend

A modern hybrid recommendation system that blends Collaborative Filtering with a real-time Social Hype Detector to recommend relevant and trending anime.

| Status | Tech Stack | License |
| :--- | :--- | :--- |
|  |     | [](https://www.google.com/search?q=LICENSE) |

-----

## Table of Contents

1.  [About the Project](https://www.google.com/search?q=%23about-the-project)
2.  [Features](https://www.google.com/search?q=%23features)
3.  [Project Structure](https://www.google.com/search?q=%23project-structure)
4.  [Technologies Used](https://www.google.com/search?q=%23technologies-used)
5.  [Setup and Installation](https://www.google.com/search?q=%23setup-and-installation)
6.  [Usage](https://www.google.com/search?q=%23usage)
7.  [Output Screenshots](https://www.google.com/search?q=%23output-screenshots)

-----

## 1\. About the Project

This project implements a unique **Hybrid Recommendation Engine** designed to solve the "cold start" and "discovery" problems in media recommendation. The system provides:

1.  **Personalization:** Based on user history (Collaborative Filtering).
2.  **Trend-Awareness:** Boosted by the current community sentiment and discussion volume ("Hype Score").

The data pipeline runs on Python, the model is served by a lightweight Flask API, and the results are presented in a high-contrast, dark-mode dashboard styled to be visually impactful and easily understood.

## 2\. Features

  * **Hybrid Engine:** Uses **SVD (Surprise)** for collaborative filtering, dynamically adjusted by the real-time Hype Score.
  * **Hype Detector:** Collects raw commentary data from the **Reddit API (PRAW)** and uses **TextBlob** for sentiment analysis to quantify current trends.
  * **Interactive Dashboard:** A visually attractive frontend using **Chart.js** to display key metrics and the Hype Ranking.
  * **Secure Configuration:** Uses **python-dotenv** and `.gitignore` to secure API keys and suppress sensitive data.

## 3\. Project Structure

The project follows a standard Flask/ML structure, separating data, models, and application logic (`src`).

```
.
├── data/
├── models/
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

| Category | Library | Logo | Purpose |
| :--- | :--- | :--- | :--- |
| **Backend/Web** | **Python (3.9+)** | \![Python Logo] | Core programming language. |
| | **Flask** | \![Flask Logo] | Lightweight framework for serving the API and web pages. |
| **ML/Data Core** | **Pandas** | \![Pandas Logo] | Efficient data manipulation and aggregation. |
| | **NumPy (\<2.0)** | \![NumPy Logo] | Fundamental library for numerical operations. |
| | **scikit-learn** | \![Scikit-learn Logo] | Standard ML library (used for overall structure/metrics). |
| | **Surprise** | \![Surprise Logo] | Specialized library for Collaborative Filtering (SVD). |
| **Data/NLP** | **requests** |  | HTTP requests for the Jikan API. |
| | **PRAW** |  | Python Reddit API Wrapper for social data collection. |
| | **TextBlob** |  | Fast sentiment analysis (polarity) for social comments. |
| **Utilities** | **joblib** |  | Efficient serialization (saving/loading) of ML assets. |
| | **python-dotenv** |  | Loads secrets from the `.env` file securely. |
| **Frontend/Viz** | **Matplotlib/Seaborn** |  | Used internally for potential data analysis and debugging. |
| | **Chart.js** |  | Dynamic, responsive charting on the frontend dashboard. |

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
    # source venv/bin/activate  # Linux/macOS
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Secrets:** Create a `.env` file in the project root with your API keys.

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

### Accessing the Frontend

The server runs on `http://127.0.0.1:5000/`.

  * **Recommendations:** `http://127.0.0.1:5000/`
  * **Hype Trends Dashboard:** `http://127.0.0.1:5000/trends`

## 7\. Output Screenshots

(Paste your two finalized images here—one for the recommendation table, one for the dark dashboard.)

-----

## 7. Output Screenshots

### 7.1. Hype Trends Dashboard
A view of the dynamic dashboard showing the Hype Score ranking and key metrics.
![Hype Dashboard Final View](assets/hype_dashboard.png)

### 7.2. Personalized Recommendations Table
The final table showing Hybrid Scores for a specific user.
![Recommendations Table View](assets/recommendations_table.png)

## 8\. License

This project is licensed under the MIT License.

This video provides an excellent introduction to building dashboards with Flask and Chart.js, which is highly relevant to the project's final steps. [Building a chart with Flask and Chart.js](https://www.youtube.com/watch?v=Tm5GrpKkshc)