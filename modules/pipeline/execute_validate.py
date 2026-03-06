from common.pipeline_base import CoreAPIClient

# -- CASO TENHA VALORES NA TABELA REQUESTS MADE (RETURN DA FUNÇÃO return_requests_made) --
# 1. sap -> /sap/sap-manager/session

# 2. requests_builder -> /requests-builder/requester 

# 3. requests_checker
"""
1. /requests-checker/lt22/open
2. /requests-checker/lt22/request
"""

# -- SE NÃO ACHAR VALORES NA LT22, VOLTAR PARA 3. (requests_checker) E REPETIR O PROCESSO --

# -- SE ACHAR VALORES, EXECUTAR: --
# 4. requests_closure -> /request_closure/update-delete

class ExecutionAndValidationPipeline(CoreAPIClient):
    def __init__(self):
        super().__init__()

    def execute_sap(self):
        self._post("sap/sap-manager/session")

    def execute_requests_builder(self):
        self._post("requests-builder/requester")

    def execute_requests_checker(self):
        self._get("requests-checker/lt22/open")
        self._post("requests-checker/lt22/request")

    def execute_requests_closure(self):
        self._patch("request_closure/update-delete")