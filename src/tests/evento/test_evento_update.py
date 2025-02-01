# -----------------------------
from pathlib import Path
dirProject = str(Path().resolve())
import sys
sys.path.append(dirProject)
# ----------------------------
import json
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos

def test_evento_update():
    end_point = servicos.ServicosEvento.UPDATE.value
    params = { "id": 1}
    body = {
        "nome": "Ciclismo",
        "descricao": "Evento de ciclismo",
        "data": "2025-01-30T23:16:26.906Z",
        "endereco": {
            "cep": "02267000",
            "estado": "SP",
            "cidade": "São Paulo",
            "bairro": "Tucuruvi",
            "rua": "Av. Dr. Antônio Maria Laet",
            "numero": 123
        },
        "faixaKm": 10,
        "gratuito": "true",
        "idTipoEvento": 1
        }
    try:
        call = RequestUtil.doRequestPut(end_point, params, body)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"
        
    assert call.status_code == 200, "Erro! Status Code diferente de 201"
    print("Teste de Create realizado com Sucesso!")
    
if __name__ == "__main__":
    test_evento_update()