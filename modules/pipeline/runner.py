from config.settings import RUNNER_STOP
from modules.pipeline.ingestion import IngestionOrchestrationPipeline
from modules.pipeline.execute_validate import ExecutionAndValidationPipeline


def runner():
    if RUNNER_STOP.is_set():
        return

    ingestion = IngestionOrchestrationPipeline()
    execute_validate = ExecutionAndValidationPipeline()

    if RUNNER_STOP.is_set(): return
    ingestion.execute_assembly_line()

    if RUNNER_STOP.is_set(): return
    ingestion.execute_forecaster()

    if RUNNER_STOP.is_set(): return
    ingestion.execute_consumption()

    if RUNNER_STOP.is_set(): return
    ingestion.execute_requests_builder()

    if RUNNER_STOP.is_set(): return
    requests_made = ingestion.return_requests_made()

    if RUNNER_STOP.is_set(): return
    execute_validate.execute_sap()

    if RUNNER_STOP.is_set(): return

    if requests_made:
        if RUNNER_STOP.is_set(): return
        execute_validate.execute_requests_builder()
        
        if RUNNER_STOP.is_set(): return
        execute_validate.execute_requests_checker()
