# ET Medical Telegram Data Scraping and Processing Pipeline

## Project Overview
This repository contains scripts and notebooks for scraping, cleaning, and transforming Ethiopian medical data from Telegram channels. The data is collected, stored in CSV format, and processed for further analysis.

## Folder Structure
```
.
├── .github/workflows     # GitHub Actions workflows
├── .vscode               # VS Code settings
├── logs                  # Logs for monitoring
├── notebooks             # Jupyter notebooks for data processing
│   ├── Task_1_Scrapping_ET_Medical_Telegram_Data.ipynb
│   ├── Task_2_Data_Cleaning_and_Transformation.ipynb
├── scripts               # Python scripts for automation
│   ├── TelegramScraper.py
│   ├── data_load_clean_transform.py
│   ├── sql_data_loader.py
├── tests                 # Unit tests for data validation
├── .gitignore            # Ignore unnecessary files
├── README.md             # Project documentation
├── requirements.txt      # Dependencies
```

## Getting Started

### Prerequisites
- Python 3.8+
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

### Running the Pipeline
1. **Scrape Telegram Data**
   ```sh
   python scripts/TelegramScraper.py
   ```
   This script extracts messages and media from specified Telegram channels and saves them in CSV format.

2. **Data Cleaning and Transformation**
   ```sh
   python scripts/data_load_clean_transform.py
   ```
   This script processes the scraped data, handling missing values, duplicates, and formatting issues.

3. **Load Data into SQL Database**
   ```sh
   python scripts/sql_data_loader.py
   ```
   This script loads the cleaned data into an SQL database for further analysis.

## Notebooks
- `Task_1_Scrapping_ET_Medical_Telegram_Data.ipynb` – Jupyter Notebook for Telegram scraping.
- `Task_2_Data_Cleaning_and_Transformation.ipynb` – Jupyter Notebook for data cleaning and transformation.

## Logging
Logs are stored in the `logs/` directory to track errors and processing status.

