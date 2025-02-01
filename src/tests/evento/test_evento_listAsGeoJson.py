# -----------------------------
from pathlib import Path
dirProject = str(Path().resolve())
import sys
sys.path.append(dirProject)
# ----------------------------
import json
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos

def test_evento_listAsGeoJson():
    end_point = servicos.ServicosEvento.LIST_AS_GEOJSON.value
    params = {
        "latitude": -49.060425291430356,
        "longitude": -26.925053716216933,
        "raio": 10
        }
    try:
        call = RequestUtil.doRequest(end_point, params, None)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"
        
    assert call.status_code == 200, "Erro! Status Code diferente de 200"
    print("Teste de Version realizado com Sucesso!")
    
if __name__ == "__main__":
    test_evento_listAsGeoJson()