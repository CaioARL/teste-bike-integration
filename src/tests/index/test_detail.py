# -----------------------------
from pathlib import Path
dirProject = str(Path().resolve())
import sys
sys.path.append(dirProject)
# ----------------------------
import json
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos

def test_detail():
    end_point = servicos.ServicosIndex.DETAIL.value
    try:
        call = RequestUtil.doRequest(end_point, None, None)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"
        
    assert call.status_code == 200, "Erro! Status Code diferente de 200"
    print("Teste de Detail realizado com Sucesso!")
    
if __name__ == "__main__":
    test_detail()