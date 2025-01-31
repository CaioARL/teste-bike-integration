# -----------------------------
from pathlib import Path

dirProject = str(Path().resolve())
import sys

sys.path.append(dirProject)
# ----------------------------
import json
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos

# Configuração
nome_api_esperado = "BRASIL_API"


def test_config_get():
    end_point = servicos.ServicosConfiguracao.CONFIG.value
    params = {"id": 1}
    try:
        call = RequestUtil.doRequest(end_point, params, None)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"

    assert call.status_code == 200, "Erro! Status Code diferente de 200"
    assert (
        call.json()["nome"] == nome_api_esperado
    ), "Erro! Nome da API diferente do esperado"

    print("Teste de get realizado com sucesso!")


if __name__ == "__main__":
    test_config_get()
