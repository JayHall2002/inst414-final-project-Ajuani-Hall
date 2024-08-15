## Kaggle API Key Setup

To access the Kaggle dataset, you'll need your own Kaggle API key.

1. **Generate a Kaggle API Key:**
   - Log in to your Kaggle account.
   - Navigate to the **Account** section.
   - Scroll down to the **API** section and click **Create New API Token**. This will download a `kaggle.json` file.

2. **Place the `kaggle.json` File:**
   - For Unix-based systems (macOS, Linux): Place it in `~/.kaggle/kaggle.json`.
   - For Windows: Place it in `%HOMEPATH%\.kaggle\kaggle.json`.

   Ensure the file has proper permissions set (Unix-based systems):
   ```bash
   chmod 600 ~/.kaggle/kaggle.json

# Project Overview

This project aims to detect bank account fraud using machine learning techniques. The dataset used is the "Bank Account Fraud Dataset" from Kaggle, which includes various features related to bank transactions and user details. The goal is to build a model that can accurately classify transactions as fraudulent or non-fraudulent.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/YOUR_GITHUB_USERNAME/inst414-final-project-ajuani-hall.git
    cd inst414-final-project-ajuani-hall
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # or
    .\venv\Scripts\activate  # On Windows
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure Kaggle API credentials are set up**:
    - Place the `kaggle.json` file in the `~/.kaggle` directory.

## Running the Project

1. **Run the main script**:
    ```bash
    python main.py
    ```

## Code Package Structure

- `data/`: Data files
    - `extracted/`: Extracted raw data files
    - `processed/`: Cleaned and processed data files
    - `outputs/`: Output files such as visualizations
    - `reference-tables/`: Reference tables used in the project
- `etl/`: ETL pipeline scripts
    - `extract.py`: Script to extract data
    - `transform.py`: Script to transform data
    - `load.py`: Script to load data
- `analysis/`: Analysis scripts
    - `model.py`: Script to build and train the model
    - `evaluate.py`: Script to evaluate the model
- `vis/`: Visualization scripts
    - `visualizations.py`: Script to create visualizations
- `main.py`: Main script to run the project
- `README.md`: Project documentation
- `requirements.txt`: List of dependencies

## Updates for Part 3
- Enhanced logging and error handling in `main.py` and other modules.
- Improved ETL processes to include new data sources and better transformations.
- Updated model evaluation to include detailed metrics and logging.
- Added more comprehensive docstrings and comments across all modules.

- # Updates for the Final Project Presentation
- Insured guide on where to place Kaggle API key is uploaded
- Finalized code to ensure all parts are operational.
