# main.py
import etl.extract as extract
import etl.transform as transform
import etl.load as load
import analysis.model as model
import analysis.evaluate as evaluate
import vis.visualizations as vis
import logging

def main():
    logging.basicConfig(filename='pipeline.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    try:
        logging.info('Starting ETL Pipeline')
        extract.extract_data()
        transform.transform_data()
        load.load_data()
        logging.info('ETL Pipeline completed successfully')

        logging.info('Starting Analysis and Evaluation')
        model.build_model()
        evaluate.evaluate_model()
        logging.info('Analysis and Evaluation completed successfully')

        logging.info('Starting Visualization')
        vis.create_visualizations()
        logging.info('Visualization completed successfully')

    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)

if __name__ == "__main__":
    main()
