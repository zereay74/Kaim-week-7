# ET Medical Telegram Data Scraping and Processing Pipeline

## Project Overview
This repository contains scripts and notebooks for scraping, cleaning, and transforming Ethiopian medical data from Telegram channels. The data is collected, stored in CSV format, and processed for further analysis. Additionally, an object detection pipeline using YOLO v11 is implemented to detect medical images, and the processed data is exposed through a FastAPI application.

## Folder Structure
```
.
├── .github/workflows     # GitHub Actions workflows
├── .vscode               # VS Code settings
├── logs                  # Logs for monitoring
│   ├── data_cleaner.log
│   ├── dbt.log
├── notebooks             # Jupyter notebooks for data processing
│   ├── Task_1_Scrapping_ET_Medical_Telegram_Data.ipynb
│   ├── Task_2_Data_Cleaning_and_Transformation.ipynb
│   ├── Task_3_Medical_Images_Object_Detection.ipynb  # YOLO v11-based object detection
├── scripts               # Python scripts for automation
│   ├── TelegramScraper.py
│   ├── data_load_clean_transform.py
│   ├── sql_data_loader.py
├── tests                 # Unit tests for data validation
├── my_fast_API_project   # FastAPI application for exposing collected data
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
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

4. **Medical Images Object Detection (YOLO v11)**
   - The `Task_3_Medical_Images_Object_Detection.ipynb` notebook uses a pretrained YOLO v11 model to detect medical images extracted from Telegram.
   - Bounding boxes, confidence scores, and class labels are extracted and stored in the dataset.
   - To run the notebook, open it in Jupyter and execute all cells.

5. **Expose Data via FastAPI**
   - The FastAPI application is structured as follows:
     ```
     my_fast_API_project/
     ├── main.py      # Entry point for FastAPI
     ├── database.py  # Database configuration (PostgreSQL + SQLAlchemy)
     ├── models.py    # ORM models
     ├── schemas.py   # Pydantic schemas
     ├── crud.py      # CRUD operations
     ```
   - To start the FastAPI server:
     ```sh
     uvicorn my_fast_API_project.main:app --reload
     ```
   - Access the API documentation at:
     - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
     - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Notebooks
- `Task_1_Scrapping_ET_Medical_Telegram_Data.ipynb` – Jupyter Notebook for Telegram scraping.
- `Task_2_Data_Cleaning_and_Transformation.ipynb` – Jupyter Notebook for data cleaning and transformation.
- `Task_3_Medical_Images_Object_Detection.ipynb` – Jupyter Notebook for medical image detection using YOLO v11.

## Logging
Logs are stored in the `logs/` directory to track errors and processing status.

## API Endpoints
Once the FastAPI server is running, the following endpoints are available:
- **GET /data/{id}** – Retrieve processed data by ID.
- **GET /data/** – Retrieve all processed data.
- More endpoints can be added as needed.

---
This project provides an end-to-end pipeline for collecting, processing, analyzing, and exposing Ethiopian medical data from Telegram channels. 🚀

