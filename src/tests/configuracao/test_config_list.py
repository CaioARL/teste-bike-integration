# -----------------------------
from pathlib import Path

dirProject = str(Path().resolve())
import sys

sys.path.append(dirProject)
# ----------------------------
import json
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos


def test_config_list():
    end_point = servicos.ServicosConfiguracao.CONFIGS.value
    try:
        call = RequestUtil.doRequest(end_point, None, None)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"

    assert call.status_code == 200, "Erro! Status Code diferente de 200"
    for item in json.loads(call.text):
        assert "id" in item, "Erro! Campo 'id' não encontrado"
        assert "nome" in item, "Erro! Campo 'nome' não encontrado"
        assert "url" in item, "Erro! Campo 'url' não encontrado"
        assert "atualizadoEm" in item, "Erro! Campo 'atualizadoEm' não encontrado"

    print("Teste de list realizado com sucesso!")


if __name__ == "__main__":
    test_config_list()
