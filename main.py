# main.py

import logging
import etl.extract as extract
import etl.transform as transform
import etl.load as load
import analysis.model as model
import analysis.evaluate as evaluate
import vis.visualizations as vis

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function to run the ETL pipeline, model training, evaluation, and visualization.
    """
    try:
        logging.info("Starting ETL pipeline...")
        extract.extract_data()
        transform.transform_data()
        load.load_data()
        logging.info("ETL pipeline completed successfully.")

        logging.info("Starting model building and evaluation...")
        model.build_model()
        evaluate.evaluate_model()
        logging.info("Model building and evaluation completed successfully.")

        logging.info("Starting visualization creation...")
        vis.create_visualizations()
        logging.info("Visualization creation completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
