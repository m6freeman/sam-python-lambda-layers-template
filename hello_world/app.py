from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit
from project_modules import module


tracer = Tracer()
logger = Logger()
metrics = Metrics(namespace="Powertools")


@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    metrics.add_metric(name="ProjectName", unit=MetricUnit.Count, value=1)
    logger.info(module.example_function().unwrap())
    return {"status_code": 200, "message": "hello world"}
