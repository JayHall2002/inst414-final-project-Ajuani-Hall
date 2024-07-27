import etl.extract as extract
import etl.transform as transform
import etl.load as load
import analysis.model as model
import analysis.evaluate as evaluate
import vis.visualizations as vis

def main():
    # ETL Pipeline
    extract.extract_data()
    transform.transform_data()
    load.load_data()

    # Analysis and Evaluation
    model.build_model()
    evaluate.evaluate_model()

    # Visualization
    vis.create_visualizations()

if __name__ == "__main__":
    main()
