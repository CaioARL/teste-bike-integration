# -----------------------------
from pathlib import Path
dirProject = str(Path().resolve())
import sys
sys.path.append(dirProject)
# ----------------------------
import json
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos

def test_nivel_habilidade_create():
    end_point = servicos.ServicosNivelHabilidade.CREATE.value
    body = {
        "nome": "Automation test",
        "descricao": "Iniciante"
    }
    try:
        call = RequestUtil.doRequestPost(end_point, None, body)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"
        
    assert call.status_code == 200, "Erro! Status Code diferente de 201"
    print("Teste de Create realizado com Sucesso!")
    
if __name__ == "__main__":
    test_nivel_habilidade_create()