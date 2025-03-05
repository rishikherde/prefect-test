from pipeline import data_pipeline
from prefect import deploy

if __name__ == "__main__":
    deploy(
        data_pipeline.to_deployment(
            name="data-processing-pipeline",
            parameters={
                "input_file": "studentsdata.csv",
                "output_file": "newstudents.csv"
            },
        ),
        work_pool_name="default-agent-pool",
        source="https://github.com/rishikherde/prefect-test.git", #replace with your repo
        entrypoint="pipeline.py:data_pipeline",
    )