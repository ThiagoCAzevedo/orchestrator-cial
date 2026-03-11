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
    # time.sleep(5)

    if RUNNER_STOP.is_set(): return
    ingestion.execute_forecaster()
    # time.sleep(5)

    if RUNNER_STOP.is_set(): return
    ingestion.execute_consumption()
    # time.sleep(5)

    if RUNNER_STOP.is_set(): return
    ingestion.execute_requests_builder()
    # time.sleep(5)

    if RUNNER_STOP.is_set(): return
    requests_made = ingestion.return_requests_made()
    # time.sleep(5)

    if RUNNER_STOP.is_set(): return
    execute_validate.execute_sap()
    # time.sleep(5)

    if RUNNER_STOP.is_set(): return

    if requests_made:
        if RUNNER_STOP.is_set(): return
        execute_validate.execute_requests_builder()
        # time.sleep(5)
        
        if RUNNER_STOP.is_set(): return
        execute_validate.execute_requests_checker()
        # time.sleep(5)
