from pipeline import data_pipeline
from prefect import deploy, GitRepository

if __name__ == "__main__":
    deploy(
        data_pipeline.to_deployment(
            name="data-processing-pipeline",
            parameters={
                "input_file": "studentsdata.csv",
                "output_file": "newstudents.csv"
            },
            git=GitRepository(
                url="https://github.com/rishikherde/prefect-test.git",
                branch="main", #or whatever branch you are using
            ),
            entrypoint="pipeline.py:data_pipeline",
        ),
        work_pool_name="default-agent-pool",
    )