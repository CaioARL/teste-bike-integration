# -----------------------------
from pathlib import Path
dirProject = str(Path().resolve())
import sys
sys.path.append(dirProject)
# ----------------------------
import json
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos

def test_evento_create():
    end_point = servicos.ServicosEvento.CREATE.value
    body = {
        "nome": "Evento de lançamento do novo produto",
        "descricao": "Evento de lançamento do novo produto",
        "data": "2025-01-30T23:16:26.906Z",
        "endereco": {
            "cep": "89010025",
            "estado": "SC",
            "cidade": "Blumenau",
            "bairro": "Centro",
            "rua": "Rua Doutor Luiz de Freitas Melro",
            "numero": 123
        },
        "faixaKm": 10,
        "gratuito": "true",
        "idTipoEvento": 1
        }
    try:
        call = RequestUtil.doRequestPost(end_point, None, body)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"
        
    assert call.status_code == 201, "Erro! Status Code diferente de 201"
    print("Teste de Create realizado com Sucesso!")
    
if __name__ == "__main__":
    test_evento_create()