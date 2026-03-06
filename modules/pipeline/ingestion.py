from common.pipeline_base import CoreAPIClient

# 1. assembly_line -> /assembly/upsert

# 2. forecaster
"""
1. /forecast/upsert/fx4pd
2. /forecast/upsert
"""

# 3. consumption -> /consumption/update/to-consume

# 4. requests_builder -> /requests-builder/upsert/to-request

# -- CASO NÃO TENHA VALORES NA TABELA REQUESTS MADE --
# Voltar para 1. (assembly_line) e repetir o processo

class IngestionOrchestrationPipeline(CoreAPIClient):
    def __init__(self):
        super().__init__()

    def execute_assembly_line(self):
        self._post("assembly/upsert")

    def execute_forecaster(self):
        self._post("forecast/upsert/fx4pd")
        self._post("forecast/upsert")

    def execute_consumption(self):
        self._patch("consumption/update/to-consume")

    def execute_requests_builder(self):
        self._post("requests-builder/upsert/to-request")

    def return_requests_made(self):
        response = self._get("requests-builder/response/requests-made/db")
        return response.json()