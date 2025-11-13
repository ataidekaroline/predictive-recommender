<h1 align="center">Predictive Anime Recommender with Hype Detection: HypeBlend</h1>

<p align="center">
  <!-- Technology Badges -->
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python" />
  <img src="https://img.shields.io/badge/Flask-lightgrey.svg?logo=flask" /> 
  <img src="https://img.shields.io/badge/Pandas-150458.svg?logo=pandas" />
  <img src="https://img.shields.io/badge/Numpy-013243.svg?logo=numpy" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E.svg?logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Surprise-FFD43B.svg?logo=python" />
  <img src="https://img.shields.io/badge/requests-0052CC.svg?logo=python" />
  <img src="https://img.shields.io/badge/PRAW-darkred.svg?logo=reddit" />
  <img src="https://img.shields.io/badge/TextBlob-blueviolet.svg?logo=python" />
  <img src="https://img.shields.io/badge/joblib-blue.svg?logo=python" />
  <img src="https://img.shields.io/badge/python--dotenv-3949AB.svg?logo=python" />
  <img src="https://img.shields.io/badge/Chart.js-FF6384.svg?logo=chartdotjs" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C.svg?logo=matplotlib" />
  <img src="https://img.shields.io/badge/Seaborn-0F4C81.svg?logo=python" />
</p>

***

## Table of Contents

1. [About the Project](#about-the-project)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Technologies Used](#technologies-used)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [Output Screenshots](#output-screenshots)
8. [HypeBlend Project Deep Dive (Step-by-Step)](#step-by-step)
9. [License](#license)

***

## About the Project

This project implements a unique **Hybrid Recommendation Engine** designed to solve the "cold start" and "discovery" problems in media recommendation. The system provides:

- **Personalization:** Based on user history (Collaborative Filtering).
- **Trend-Awareness:** Boosted by real-time community sentiment and discussion volume ("Hype Score").

The data pipeline runs on Python, the model is served by a lightweight Flask API, and the results are presented in a high-contrast, dark-mode dashboard styled for impact and ease of use.

## Features

- **Hybrid Engine:** Uses **SVD (Surprise)** for collaborative filtering, dynamically adjusted by the real-time Hype Score.
- **Hype Detector:** Collects commentary from **Reddit API (PRAW)** and uses **TextBlob** sentiment analysis to quantify current trends.
- **Interactive Dashboard:** Attractive frontend using **Chart.js** for displaying key metrics and Hype Ranking.
- **Secure Configuration:** Utilizes **python-dotenv** and `.gitignore` to secure API keys and suppress sensitive data.

## Project Structure

Standard Flask/ML directory separation for data, models, and logic.

```
.
├── data/
├── models/
├── src/
│   ├── api_collector.py
│   ├── data_processing.py
│   ├── hype_detector.py
│   └── recommender_model.py
├── templates/
│   ├── index.html
│   └── trends.html
├── venv/           # (ignored)
├── .env            # (ignored)
├── app.py
└── requirements.txt
```

## Technologies Used

| Category         | Library              | Purpose                                                    |
|:-----------------|:---------------------|------------------------------------------------------------|
| **Backend/Web**  | Python (3.9+)        | Core programming language                                  |
|                  | Flask                | Lightweight framework for API and web pages                |
| **ML/Data Core** | Pandas               | Efficient data manipulation                                |
|                  | NumPy (<2.0)         | Fundamental numerical operations                           |
|                  | scikit-learn         | Standard ML structure/metrics                              |
|                  | Surprise             | Collaborative Filtering (SVD)                              |
| **Data/NLP**     | requests             | HTTP requests for Jikan API                                |
|                  | PRAW                 | Python Reddit API Wrapper                                  |
|                  | TextBlob             | Sentiment analysis for social comments                     |
| **Utilities**    | joblib               | Efficient serialization for ML assets                      |
|                  | python-dotenv        | Secure secret management                                   |
| **Frontend/Viz** | Matplotlib/Seaborn   | Data analysis/debugging                                    |
|                  | Chart.js             | Dynamic charting dashboard                                 |

### APIs Used

- **Jikan API (v4)**: Fetches official anime metadata (scores, genres, titles).
- **Reddit API**: Accessed via PRAW for real-time community sentiment and volume.

## Setup and Installation

### Prerequisites

- Python 3.9+
- Reddit API Credentials (for `.env`)

### Installation Steps

1. **Clone the Repo:**
   ```bash
   git clone YOUR_REPO_URL
   cd predictive-recommender
   ```
2. **Create and Activate Environment:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/macOS
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Secrets:** Create a `.env` file in the project root with your API keys.

### Run Data Pipeline

Execute these scripts sequentially to prepare all data and models:

```bash
python src/api_collector.py
python src/data_processing.py
python src/hype_detector.py
python src/recommender_model.py
```

## Usage

### Starting the Flask Application

```bash
python app.py
```

### Accessing the Frontend

Server runs at `http://127.0.0.1:5000/`.

- **Recommendations:** `http://127.0.0.1:5000/`
- **Hype Trends Dashboard:** `http://127.0.0.1:5000/trends`

## Output Screenshots

### Hype Trends Dashboard

A view of the dynamic dashboard showing the Hype Score ranking and key metrics.

<p align="center">
  <img src="assets/hype_dashboard.jpg" alt="dashboard" width="600px">
</p>

Hybrid scores for a specific user.

<p align="center">
  <img src="assets/recommendations_table.jpg" alt="table" width="600px">
</p>


## HypeBlend Project Deep Dive (Step-by-Step)

This guide provides a detailed technical explanation of the **HypeBlend** system, covering the data flow, hybrid scoring logic, and the interpretation of the key metrics displayed on your dashboard.

## 1. Project Phases & Data Pipeline

The project relies on a sequential pipeline to process raw social data and train the recommendation model.

| Script | Phase | Key Action | Generated Output |
| :--- | :--- | :--- | :--- |
| **`api_collector.py`** | **Acquisition** | Fetches core anime metadata (ID, title, score) from the **MAL API**. | `raw_anime_data.csv` |
| **`hype_detector.py`** | **Hype Scoring** | Collects comments from Reddit (**PRAW**), performs **TextBlob** sentiment analysis, and calculates the Hype Score. | `processed_anime_data.csv` |
| **`data_processing.py`** | **User Simulation** | Creates synthetic user ratings (`user_id`, `mal_id`, `rating`) to simulate a community for ML training. | `synthetic_user_ratings.csv` |
| **`recommender_model.py`** | **Training** | Trains the **SVD (Surprise)** Collaborative Filtering model on the synthetic ratings. | `collaborative_filter.model` |

---

## 2. Hybrid Scoring Logic (The Core Engine)

The system's intelligence comes from blending the ML prediction with the social trend data. The final score used for ranking is calculated as follows:

$$\text{Final Hybrid Score} = (\text{Predicted Rating}_{\text{SVD}}) + (\text{Scaled Hype Score} \times 0.3)$$

This formula ensures that highly *relevant* items (high SVD prediction) get a **boost** in rank if they are currently *trending* (high Hype Score).

---

## 3. Understanding the Metrics

### A. Personalized Recommendations Table (`/`)

This table shows the recommended items for a specific user, sorted by the final rank.

| Metric | Range/Scale | Interpretation |
| :--- | :--- | :--- |
| **MAL Score** | 1–10 | Official community average rating. |
| **Current Hype Score** | **-1.0 to +1.0** | **The most dynamic metric.** Quantifies social media buzz. Positive scores (e.g., +0.5) indicate strong positive sentiment/high volume (Hype). |
| **Hybrid Recommendation Score** | 1.0+ | The final predicted rank. The higher the score, the higher the probability the user will enjoy the item **right now**. |

### B. Hype Trends Dashboard (`/trends`)

The dashboard  displays aggregated community engagement and trends.

#### Summary Metrics

| Metric | Data Source | Meaning |
| :--- | :--- | :--- |
| **Total Anime in Index** | `raw_anime_data.csv` | Total number of unique titles the system tracks. |
| **Total Community Engagement** | `scored_by` (Sum) | Represents the overall size of the community whose ratings are factored in. |
| **Top 3 Most Engaged Genres** | `processed_anime_data.csv` | Categorizes popularity by genre, showing where the community's attention is focused. |

#### Chart Interpretation

The bar chart visualizes the **Current Hype Score** of the Top 20 items.

* **Positive Bars (e.g., Teal/Aqua):** Indicate strong community consensus and high discussion volume (True Hype).
* **Negative Bars (e.g., Pink/Coral):** Indicate that the high volume of discussion is driven by negative sentiment, often signaling controversy or backlash.



## License

This project is licensed under the MIT License.

***

<!-- FOOTER: Author & LinkedIn -->

<p align="center">
  <b>Luana K. Ribeiro</b><br>
  <a href="https://www.linkedin.com/in/ataidekaroline/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin" alt="LinkedIn Profile" />
  </a>
</p>


