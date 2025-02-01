# -----------------------------
from pathlib import Path
dirProject = str(Path().resolve())
import sys
sys.path.append(dirProject)
# ----------------------------
import json
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos

def test_nivel_habilidade_list():
    end_point = servicos.ServicosNivelHabilidade.LIST.value
    try:
        call = RequestUtil.doRequest(end_point, None, None)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"
        
    assert call.status_code == 200, "Erro! Status Code diferente de 201"
    print("Teste de Create realizado com Sucesso!")
    
if __name__ == "__main__":
    test_nivel_habilidade_list()