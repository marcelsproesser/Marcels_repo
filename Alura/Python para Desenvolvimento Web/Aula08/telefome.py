from telefoneBR import TelefonesBR
import re

telefone = "5514926481234"

telefone_objeto = TelefonesBR(telefone)
# padrao = "([0-9]{2,3})?([0-9]){2})([0-9]{4,5})([0-9]{4})"
# resposta = re.search(padrao, telefone)
# print(resposta.group(1))

print(telefone_objeto)