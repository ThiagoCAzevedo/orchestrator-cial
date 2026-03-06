# aqui, é onde vai fazer todo pipeline mais importante do sistema


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




# -- CASO TENHA VALORES NA TABELA REQUESTS MADE --
# 5. requests_made