from modules.pipeline.ingestion import IngestionOrchestrationPipeline
from modules.pipeline.execute_validate import ExecutionAndValidationPipeline

def runner():
    ingestion = IngestionOrchestrationPipeline()
    execute_validate = ExecutionAndValidationPipeline()

    # Execute the first part of the pipeline
    ingestion.execute_assembly_line()
    ingestion.execute_forecaster()
    ingestion.execute_consumption()
    ingestion.execute_requests_builder()
    
    # # Check if there are values in the requests made table
    requests_made = ingestion.return_requests_made()

    if requests_made:
        # If there are values, execute the second part of the pipeline
        execute_validate.execute_sap()
        # execute_validate.execute_requests_builder()
    #     execute_validate.execute_requests_checker()

    #     # Check if there are values in LT22
    #     lt22_response = execute_validate._get("requests-checker/lt22/open")
    #     lt22_data = lt22_response.json()

    #     if lt22_data:
    #         # If there are values in LT22, execute requests closure
    #         execute_validate.execute_requests_closure()
    #     else:
    #         # If there are no values in LT22, repeat the process from requests checker
    #         execute_validate.execute_requests_checker()
    # else:
    #     # If there are no values in requests made, repeat the process from assembly line
    #     runner()
    print("fim")