from enum import Enum

class ServicosConfiguracao(Enum):
    CONFIGS = '/v1/configuracao-api-externa/list'
    CONFIG = '/v1/configuracao-api-externa/get'
    CONFIGS_BY_NAME = '/v1/configuracao-api-externa/getByNome'
    
class ServicosEmail(Enum):
    ANY_MESSAGE = '/v1/email/sendAnyMessage'
    
class ServicosEmpresa(Enum):
    IS_ACTIVE = '/v1/empresa/isActiveCnpj'
    GET_BY_CNPJ = '/v1/empresa/getByCnpj'

class ServicosEndereco(Enum):
    COORDINATES_BY_CEP_AND_NUMBER = '/v1/endereco/getLatAndLonByCepAndNumber'
    CEP_BY_COORDINATES = '/v1/endereco/getCepByLatAndLon'
    CEP = '/v1/endereco/getByCep'
    
class ServicosEvento(Enum):
    CREATE = '/v1/evento/create'
    UPDATE = '/v1/evento/update'
    DELETE = '/v1/evento/delete'
    GET = '/v1/evento/get'
    LIST = '/v1/evento/list'
    GET_AS_GEOJSON = '/v1/evento/getAsGeoJson'
    LIST_AS_GEOJSON = '/v1/evento/listAsGeoJson'
    
class ServicosIndex(Enum):
    VERSION = '/app/version'
    GET = '/app/get'
    PING = '/app/ping'
    HOME = '/app/home'
    DETAIL = '/app/detail'
    
class ServicosInfraestrutura(Enum):
    LIST = '/v1/infraestrutura/list'
    GET = '/v1/infraestrutura/get'
    LIST_AS_GEOJSON = '/v1/infraestrutura/listAsGeoJson'
    GET_AS_GEOJSON = '/v1/infraestrutura/getAsGeoJson'
    
class ServicosLogin(Enum):
    LOGIN = '/v1/login/do'
    RECOVER = '/v1/login/recover'
    
class ServicosNivelHabilidade(Enum):
    CREATE = '/v1/nivel-habilidade/create'
    LIST = '/v1/nivel-habilidade/list'
    
class ServicosTipoEvento(Enum):
    CREATE = '/v1/tipo-evento/create'
    LIST = '/v1/tipo-evento/list'
    
class ServicosTipoEvento(Enum):
    CREATE = '/v1/tipo-evento/create'
    LIST = '/v1/tipo-evento/list'
    
class ServicosToken(Enum):
    SEND_TOKEN = '/v1/token/sendToken'
    LIST_BY_USER = '/v1/token/listByUser'
    IS_VALID_TOKEN = '/v1/token/isValidToken'
    
class ServicosUsuario(Enum):
    UPDATE = '/v1/usuario/update'
    CREATE = '/v1/usuario/create'
    DELETE = '/v1/usuario/delete'
    GET = '/v1/usuario/get'
    VALIDATE_CPF = '/v1/usuario/validate/cpf'