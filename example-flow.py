import prefect
from prefect.storage import S3
from prefect.run_configs import ECSRun
from prefect import task, Flow
import pandas as pd

TASK_ARN = "arn:aws:iam::421126574751:role/ECSTaskS3ECRRole"
RUN_CONFIG = ECSRun(labels=['s3-flow-storge'],
		    task_role_arn=TASK_ARN,
		    image='syousif-gel/prefect-pydata',
                    memory=512, cpu=256)
STORAGE = S3(buckets='prefect-sandbox-poc')


@task
def say_hello():
    logger = prefect.contect.get("logger")
    df = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})
    logger.info(f"Hello from prefect! Dataframe: {df}")
    logger.info(f"Pandas version: {pd.__version__}")


with Flow("s3_pandas", storage=STORAGE,
          run_config=RUN_CONFIG) as flow:
     say_hello()

# Register the flow under the demo project called 04_fargate
flow.register(project_name="04_fargate")
