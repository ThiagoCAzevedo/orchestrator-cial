from config.settings import settings
import httpx

base_url = settings.CORE_URL

def execute_al():
    post_url = f"{base_url.rstrip('/')}/assembly/upsert"
    httpx.post(post_url)

execute_al() 

# -- BASE -- 
# 1. assembly_line -> /assembly/upsert

# 2. forecaster
"""
1. /forecast/upsert/fx4pd
2. /forecast/upsert
"""

# 3. consumption -> /consumption/update/to-consume

# 4. requests_builder
"""
1. /requests-builder/upsert/to-request
2. /requests-builder/requester
"""

# -- CASO NÃO TENHA VALORES NA TABELA REQUESTS MADE --
# Voltar para 1. (assembly_line) e repetir o processo