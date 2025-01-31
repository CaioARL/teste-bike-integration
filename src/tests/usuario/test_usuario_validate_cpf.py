# -----------------------------
from pathlib import Path

dirProject = str(Path().resolve())
import sys

sys.path.append(dirProject)
# ----------------------------
import json
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos
import random

# Configuração
cpf_valido = "37410313056"
cpf_invalido = "12345678900"


def _validate_cpf(cpf, expected_message):
    end_point = servicos.ServicosUsuario.VALIDATE_CPF.value

    params = {"cpf": cpf}
    call = RequestUtil.doRequest(end_point, params, None)
    assert call.status_code == 200, "Erro! Status Code diferente de 200"
    assert call.text == expected_message, "Erro! Mensagem diferente do esperado"


def test_usuario_validate_cpf():
    _validate_cpf(cpf_valido, "CPF válido")
    _validate_cpf(cpf_invalido, "CPF inválido")


if __name__ == "__main__":
    test_usuario_validate_cpf()
