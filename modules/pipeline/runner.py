from modules.pipeline.ingestion import IngestionOrchestrationPipeline
from modules.pipeline.execute_validate import ExecutionAndValidationPipeline

def runner():
    first_part = IngestionOrchestrationPipeline()
    second_part = ExecutionAndValidationPipeline()

    # Execute the first part of the pipeline
    first_part.execute_assembly_line()
    first_part.execute_forecaster()
    first_part.execute_consumption()
    first_part.execute_requests_builder()

    # Check if there are values in the requests made table
    requests_made = first_part.return_requests_made()

    if requests_made:
        # If there are values, execute the second part of the pipeline
        second_part.execute_sap()
        second_part.execute_requests_builder()
        second_part.execute_requests_checker()

        # Check if there are values in LT22
        lt22_response = second_part._get("requests-checker/lt22/open")
        lt22_data = lt22_response.json()

        if lt22_data:
            # If there are values in LT22, execute requests closure
            second_part.execute_requests_closure()
        else:
            # If there are no values in LT22, repeat the process from requests checker
            second_part.execute_requests_checker()
    else:
        # If there are no values in requests made, repeat the process from assembly line
        runner()