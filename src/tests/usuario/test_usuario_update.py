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


def _usuario_create():
    end_point = servicos.ServicosUsuario.CREATE.value
    email_aleatorio = "joaosilva" + str(random.randint(1, 1000)) + "@gmail.com"
    nome_usuario_aleatorio = "joaosilva" + str(random.randint(1, 1000))

    body = _get_body(nome_usuario_aleatorio, email_aleatorio)
    try:
        call = RequestUtil.doRequestPost(end_point, None, body)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"

    assert call.status_code == 201, "Erro! Status Code diferente de 201"
    id = call.json()["id"]

    print("Usuario criado com sucesso id: ", id)
    return call.json()


def _usuario_update(usuario_json):
    end_point = servicos.ServicosUsuario.UPDATE.value

    nome_usuario_aleatorio = "joaosilva" + str(random.randint(1, 1000))
    email_aleatorio = "joaosilva" + str(random.randint(1, 1000)) + "@gmail.com"

    nome = usuario_json["nomeUsuario"]
    email = usuario_json["email"]

    params = {"id": usuario_json["id"]}

    body = _get_body(nome_usuario_aleatorio, email_aleatorio)
    try:
        call = RequestUtil.doRequestPut(end_point, params, body)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"

    assert call.status_code == 200, "Erro! Status Code diferente de 201"
    assert nome != nome_usuario_aleatorio, "Erro! Nome do Usuario diferente do esperado"
    assert email != email_aleatorio, "Erro! Email do Usuario diferente do esperado"

    print("Teste de Update realizado com Sucesso!")


def _usuario_delete(id_usuario):
    end_point = servicos.ServicosUsuario.DELETE.value
    params = {"id": id_usuario}
    try:
        call = RequestUtil.doRequestDelete(end_point, params, None)
    except:
        assert False, "Erro! Site não Acessível! Favor verificar VPN ou conexão de Rede"

    assert call.status_code == 200, "Erro! Status Code diferente de 200"
    print("Usuario deletado com sucesso id: ", id_usuario)


def _get_body(username, email):
    return {
        "nome": "João da Silva",
        "nomeUsuario": username,
        "endereco": {
            "cep": "89010025",
            "estado": "SC",
            "cidade": "Blumenau",
            "bairro": "Centro",
            "rua": "Rua Doutor Luiz de Freitas Melro",
            "numero": 123,
        },
        "email": email,
        "senha": "123456",
        "cpf": "123456",
        "cnpj": "123456",
        "nivelHabilidade": 1,
    }


def test_usuario_update():
    usuario_json = _usuario_create()
    _usuario_update(usuario_json)
    _usuario_delete(usuario_json["id"])


if __name__ == "__main__":
    test_usuario_update()
