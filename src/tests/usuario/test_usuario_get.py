# -----------------------------
from pathlib import Path

dirProject = str(Path().resolve())
import sys

sys.path.append(dirProject)
# ----------------------------
import json
from src.util.requestUtil import RequestUtil
import src.enum.servicos as servicos
import random

# Configuracao teste
nome_esperado = "João da Silva"


def _usuario_create():
    end_point = servicos.ServicosUsuario.CREATE.value
    email_aleatorio = "joaosilva" + str(random.randint(1, 1000)) + "@gmail.com"
    nome_usuario_aleatorio = "joaosilva" + str(random.randint(1, 1000))

    body = {
        "nome": "João da Silva",
        "nomeUsuario": nome_usuario_aleatorio,
        "endereco": {
            "cep": "89010025",
            "estado": "SC",
            "cidade": "Blumenau",
            "bairro": "Centro",
            "rua": "Rua Doutor Luiz de Freitas Melro",
            "numero": 123,
        },
        "email": email_aleatorio,
        "senha": "123456",
        "cpf": "123456",
        "cnpj": "123456",
        "nivelHabilidade": 1,
    }
    try:
        call = RequestUtil.doRequestPost(end_point, None, body)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"

    assert call.status_code == 201, "Erro! Status Code diferente de 201"
    id = call.json()["id"]

    print("Usuario criado com sucesso id: ", id)
    return id


def _usuario_get(id_usuario):
    end_point = servicos.ServicosUsuario.GET.value
    params = {"id": id_usuario}
    try:
        call = RequestUtil.doRequest(end_point, params, None)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"

    assert call.status_code == 200, "Erro! Status Code diferente de 200"
    assert (
        call.json()["nome"] == nome_esperado
    ), "Erro! Nome do Usuário diferente do esperado"
    print("Teste de Get realizado com Sucesso!")


def _usuario_delete(id_usuario):
    end_point = servicos.ServicosUsuario.DELETE.value
    params = {"id": id_usuario}
    try:
        call = RequestUtil.doRequestDelete(end_point, params, None)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"

    assert call.status_code == 200, "Erro! Status Code diferente de 200"
    print("Usuario deletado com sucesso id: ", id_usuario)


def test_usuario_get():
    id_usuario = _usuario_create()
    _usuario_get(id_usuario)
    _usuario_delete(id_usuario)


if __name__ == "__main__":
    test_usuario_get()
