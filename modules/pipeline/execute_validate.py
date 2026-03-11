from common.pipeline_base import CoreAPIClient


class ExecutionAndValidationPipeline(CoreAPIClient):
    def __init__(self):
        super().__init__()

    def execute_sap(self):
        self._post("/sap-manager/session")

    def execute_requests_builder(self):
        self._post("requests-builder/requester")

    def execute_requests_checker(self):
        self._post("requests-checker/lt22/open")
        self._post("requests-checker/lt22/request")