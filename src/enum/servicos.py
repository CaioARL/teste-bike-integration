from enum import Enum

class ServicosConfiguracao(Enum):
    CONFIGS = '/api/v1/configuracao-api-externa/list'
    CONFIG = '/api/v1/configuracao-api-externa/get'
    CONFIGS_BY_NAME = '/configuracao-api-externa/getByNome'
    
class ServicosEmail(Enum):
    ANY_MESSAGE = '/api/v1/email/sendAnyMessage'
    
class ServicosEmpresa(Enum):
    IS_ACTIVE = '/api/v1/empresa/isActiveCnpj'
    GET_BY_CNPJ = '/api/v1/empresa/getByCnpj'

class ServicosEndereco(Enum):
    COORDINATES_BY_CEP_AND_NUMBER = '/api/v1/endereco/getLatAndLonByCepAndNumber'
    CEP_BY_COORDINATES = '/api/v1/endereco/getCepByLatAndLon'
    CEP = '/api/v1/endereco/getByCep'
    
class ServicosEvento(Enum):
    CREATE = '/api/v1/evento/create'
    UPDATE = '/api/v1/evento/update'
    DELETE = '/api/v1/evento/delete'
    GET = '/api/v1/evento/get'
    LIST = '/api/v1/evento/list'
    GET_AS_GEOJSON = '/api/v1/evento/getAsGeoJson'
    LIST_AS_GEOJSON = '/api/v1/evento/listAsGeoJson'
    
class ServicosIndex(Enum):
    VERSION = '/app/version'
    GET = '/app/get'
    PING = '/app/ping'
    HOME = '/app/home'
    DETAIL = '/app/detail'
    
class ServicosInfraestrutura(Enum):
    LIST = '/api/v1/infraestrutura/list'
    GET = '/api/v1/infraestrutura/get'
    LIST_AS_GEOJSON = '/api/v1/infraestrutura/listAsGeoJson'
    GET_AS_GEOJSON = '/api/v1/infraestrutura/getAsGeoJson'
    
class ServicosLogin(Enum):
    LOGIN = '/api/v1/login/do'
    RECOVER = '/api/v1/login/recover'
    
class ServicosNivelHabilidade(Enum):
    CREATE = '/api/v1/nivel-habilidade/create'
    LIST = '/api/v1/nivel-habilidade/list'
    
class ServicosTipoEvento(Enum):
    CREATE = '/api/v1/tipo-evento/create'
    LIST = '/api/v1/tipo-evento/list'
    
class ServicosTipoEvento(Enum):
    CREATE = '/api/v1/tipo-evento/create'
    LIST = '/api/v1/tipo-evento/list'
    
class ServicosToken(Enum):
    SEND_TOKEN = '/api/v1/token/sendToken'
    LIST_BY_USER = '/api/v1/token/listByUser'
    IS_VALID_TOKEN = '/api/v1/token/isValidToken'
    
class ServicosUsuario(Enum):
    UPDATE = '/api/v1/usuario/update'
    CREATE = '/api/v1/usuario/create'
    DELETE = '/api/v1/usuario/delete'
    GET = '/api/v1/usuario/get'
    VALIDATE_CPF = '/api/v1/usuario/validate/cpf'