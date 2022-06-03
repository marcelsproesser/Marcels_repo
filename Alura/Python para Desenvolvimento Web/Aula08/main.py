import requests
from acesso_cep import BuscaEndereco

cep = 86010600
objeto_cep = BuscaEndereco(cep)


bairro, cidade, uf = objeto_cep.acessa_via_cep()


print(bairro, ", ", cidade, ", ", uf)
