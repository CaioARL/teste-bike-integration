import pytest
import json
from datetime import datetime
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos
import config as parametros

def pytest_configure(config):
    end_point = parametros.end_point + servicos.ServicosIndex.VERSION.value
    delimiter = "\n" + "----------------------------------------------------" + "\n"

    try:
        RequestUtil.doRequest(end_point, None, None)
    except:
        inf_header = delimiter + "Endpoint: " + end_point +"\nErro! Site não Acessível! Favor verificar VPN ou conexão de Rede\n" + delimiter
        pytest.xfail(inf_header)
    
    # Adicionando a versão as informações Environment
    if hasattr(config, '_metadata'):
        config._metadata[parametros.produto] = "v." + parametros.produto

def pytest_report_header():
    end_point = parametros.end_point + servicos.ServicosIndex.VERSION.value
    delimiter = "\n" + "----------------------------------------------------" + "\n"
    v_datetime = datetime.now()
    data_e_hora_em_texto = v_datetime.strftime('%d/%m/%Y %H:%M:%S')

    try:
        resposta = RequestUtil.doRequest(end_point, None, None)
    except:
        inf_header = "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"   
        inf_header = delimiter + "Endpoint: " + end_point +"\nErro! Site não Acessível! Favor verificar VPN ou conexão de Rede\n" + data_e_hora_em_texto + delimiter
        pytest.xfail(inf_header)

    if resposta.status_code != 200: 
        inf_header = "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"   
        inf_header = delimiter + "Endpoint: " + end_point +"\nErro! Site não Acessível! Favor verificar VPN ou conexão de Rede\n" + data_e_hora_em_texto + delimiter