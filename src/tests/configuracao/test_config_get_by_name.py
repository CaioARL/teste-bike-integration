# -----------------------------
from pathlib import Path

dirProject = str(Path().resolve())
import sys

sys.path.append(dirProject)
# ----------------------------
import json
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos

nomes_apis_base = ["BRASIL_API", "OPEN_STREET_MAP_API", "VIA_CEP"]


def test_config_get_by_name():
    end_point = servicos.ServicosConfiguracao.CONFIGS_BY_NAME.value
    params = {"nome": "a"}
    try:
        call = RequestUtil.doRequest(end_point, params, None)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"

    assert call.status_code == 200, "Erro! Status Code diferente de 200"
    nomes_recebidos: list[str] = []
    for config in json.loads(call.text):
        nomes_recebidos.append(config["nome"])

    # Verifica se todos os nomes esperados estão presentes
    for nome in nomes_apis_base:
        assert nome in nomes_recebidos, f"Erro! Nome {nome} não encontrado"

    print("Teste de get by name realizado com sucesso!")


if __name__ == "__main__":
    test_config_get_by_name()
