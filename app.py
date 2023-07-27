from flask import Flask, jsonify
import os, api 
from dotenv import load_dotenv



app = Flask(__name__)

app.config['JSON_AS_ASCII']= False

@app.route('/', methods=['GET'])
def routes_info():
    """Print all defined routes and their endpoint docstrings

    This also handles flask-router, which uses a centralized scheme
    to deal with routes, instead of defining them as a decorator
    on the target function.
    """
    routes = []
    for rule in app.url_map.iter_rules():
        try:
            if rule.endpoint != 'static':
                if hasattr(app.view_functions[rule.endpoint], 'import_name'):
                    import_name = app.view_functions[rule.endpoint].import_name
                    obj = import_string(import_name) # type:ignore
                    routes.append({rule.rule: "%s\n%s" % (",".join(list(rule.methods)), obj.__doc__)})
                else:
                    routes.append({rule.rule: app.view_functions[rule.endpoint].__doc__})
        except Exception as exc:
            routes.append({rule.rule: 
                           "(%s) INVALID ROUTE DEFINITION!!!" % rule.endpoint})
            route_info = "%s => %s" % (rule.rule, rule.endpoint)
            app.logger.error("Invalid route: %s" % route_info, exc_info=True)
            

    return jsonify(code=200, data=routes)

""" 

    DB PESSOAL
"""
load_dotenv('./environment/pessoal.env')
@app.route('/pessoal/servidor/servidor')
@app.route('/pessoal/servidor')
def pessoalServidor():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_SERVIDOR"),os.getenv("TB_SERVIDOR")))

@app.route('/pessoal/servidor/ex-servidor')
@app.route('/pessoal/ex-servidor')
def pessoalExServidor():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_SERVIDOR"),os.getenv("TB_EX_SERVIDOR")))

@app.route('/pessoal/servidor/servidor-ativo')
@app.route('/pessoal/servidor-ativo')
def pessoalServidorAtivo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_SERVIDOR"),os.getenv("TB_SERVIDOR_ATIVO")))

@app.route('/pessoal/servidor/servidor-ausente')
@app.route('/pessoal/servidor-ausente')
def pessoalServidorAusente():
    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_SERVIDOR"),os.getenv("TB_SERVIDOR_AUSENTE")))

@app.route('/pessoal/servidor/servidor-inativo')
@app.route('/pessoal/servidor-inativo')
def pessoalServidorInativo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_SERVIDOR"),os.getenv("TB_SERVIDOR_INATIVO")))

@app.route('/pessoal/servidor/servidor-inst-pensao')
@app.route('/pessoal/servidor-pensao')
def pessoalServidorPensao():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_SERVIDOR"),os.getenv("TB_SERVIDOR_INST_PENSAO")))

@app.route('/pessoal/servidor/servidor-presente')
@app.route('/pessoal/servidor-presente')
def pessoalServidorPresente():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_SERVIDOR"),os.getenv("TB_SERVIDOR_PRESENTE")))

@app.route('/pessoal/residente/residente')
@app.route('/pessoal/residente')
def pessoalResidente():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_RESIDENTE"),os.getenv("TB_RESIDENTE")))

@app.route('/pessoal/residente/residente-ativo')
@app.route('/pessoal/residente-ativo')
def pessoalResidenteAtivo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_RESIDENTE"),os.getenv("TB_RESIDENTE_ATIVO")))


@app.route('/pessoal/terceirizado/terceirizado')
@app.route('/pessoal/terceirizado')
def pessoalTerceirizado():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_TERCEIRIZADO"),os.getenv("TB_TERCEIRIZADO")))

@app.route('/pessoal/teceirizado/terceirizado-ativo')
@app.route('/pessoal/terceirizado-ativo')
def pessoalTerceirizadoAtivo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_TERCEIRIZADO"),os.getenv("TB_TERCEIRIZADO_ATIVO")))

@app.route('/pessoal/estagiario/estagiario')
@app.route('/pessoal/estagiario')
def pessoalEstagiario():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_ESTAGIARIO"),os.getenv("TB_ESTAGIARIO")))

@app.route('/pessoal/estagiario/estagiario-ativo')
@app.route('/pessoal/estagiario-ativo')
def pessoalEstagiarioAtivo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_ESTAGIARIO"),os.getenv("TB_ESTAGIARIO_ATIVO")))

@app.route('/pessoal/promotor/promotor')
@app.route('/pessoal/promotor')
def pessoalPromotor():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_PROMOTOR"),os.getenv("TB_PROMOTOR")))

@app.route('/pessoal/promotor/promotor-ativo')
@app.route('/pessoal/promotor-ativo')
def pessoalPromotorAtivo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_PROMOTOR"),os.getenv("TB_PROMOTOR_ATIVO")))

@app.route('/pessoal/procurador/procurador')
@app.route('/pessoal/procurador')
def pessoalProcurador():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_PROCURADOR"),os.getenv("TB_PROCURADOR")))

@app.route('/pessoal/procurador/procurador-ativo')
@app.route('/pessoal/procurador-ativo')
def pessoalProcuradorAtivo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_PROCURADOR"),os.getenv("TB_PROCURADOR_ATIVO")))

@app.route('/pessoal/autoridade/autoridade')
@app.route('/pessoal/autoridade')
def pessoalAutoridade():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_AUTORIDADE"),os.getenv("TB_AUTORIDADE")))

@app.route('/pessoal/autoridade/autoridade-ativa')
@app.route('/pessoal/autoridade-ativa')
def pessoalAutoridadeAtiva():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_AUTORIDADE"),os.getenv("TB_AUTORIDADE_ATIVA")))

@app.route('/pessoal/dependente/dependente')
@app.route('/pessoal/dependente')
def pessoalDependente():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_DEPENDENTE"),os.getenv("TB_DEPENDENTE")))

@app.route('/pessoal/dependente/dependente-ativo')
@app.route('/pessoal/dependente-ativo')
def pessoalDependenteAtivo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_DEPENDENTE"),os.getenv("TB_DEPENDENTE_ATIVO")))

@app.route('/pessoal/conferencia/conferencia')
@app.route('/pessoal/conferencia')
def pessoalConferencia():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_CONFERENCIA"),os.getenv("TB_CONFERENCIA")))

@app.route('/pessoal/emprestimo/emprestimo', methods=['GET'])
@app.route('/pessoal/emprestimo',methods=['GET'])
def pessoalEmprestimo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_EMPRESTIMO"),os.getenv("TB_EMPRESTIMO")))


@app.route('/pessoal/beneficio/beneficio', methods=['GET'])
@app.route('/pessoal/beneficio',methods=['GET'])
def pessoalBeneficio():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_BENEFICIO"),os.getenv("TB_BENEFICIO")))

@app.route('/pessoal/beneficio/beneficio-ativo', methods=['GET'])
@app.route('/pessoal/beneficio-ativo',methods=['GET'])
def pessoalBeneficioAtivo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_BENEFICIO"),os.getenv("TB_BENEFICIO_ATIVO")))

@app.route('/pessoal/folha-beneficio/folha-beneficio', methods=['GET'])
@app.route('/pessoal/folha-beneficio',methods=['GET'])
def pessoalFolhaBeneficio():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_FOLHA_BENEFICIO"),os.getenv("TB_FOLHA_BENEFICIO")))

@app.route('/pessoal/juiz/juiz', methods=['GET'])
@app.route('/pessoal/juiz',methods=['GET'])
def pessoalJuiz():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_JUIZ"),os.getenv("TB_JUIZ")))

@app.route('/pessoal/juiz/juiz-ativo', methods=['GET'])
@app.route('/pessoal/juiz-ativo',methods=['GET'])
def pessoalJuizAtivo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_JUIZ"),os.getenv("TB_JUIZ_ATIVO")))

@app.route('/pessoal/membro/membro', methods=['GET'])
@app.route('/pessoal/membro',methods=['GET'])
def pessoalMembro():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_MEMBRO"),os.getenv("TB_MEMBRO")))

@app.route('/pessoal/membro/membro-ativo', methods=['GET'])
@app.route('/pessoal/membro-ativo',methods=['GET'])
def pessoalMembroAtivo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_MEMBRO"),os.getenv("TB_MEMBRO_ATIVO")))

@app.route('/pessoal/pensionista/pensionista', methods=['GET'])
@app.route('/pessoal/pensionista',methods=['GET'])
def pessoalPensionista():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_PENSIONISTA"),os.getenv("TB_PENSIONISTA")))

@app.route('/pessoal/pensionista/pensionista-ativo', methods=['GET'])
@app.route('/pessoal/pensionista-ativo',methods=['GET'])
def pessoalPensionistaAtivo():

    return jsonify(api.Api(os.getenv('DB_PESSOAL'),os.getenv("SCHEMA_PENSIONISTA"),os.getenv("TB_PENSIONISTA_ATIVO")))

"""

    DB PJE

"""
load_dotenv('./environment/pje.env')

@app.route('/pje/admsadp/arquivo', methods=['GET'])
def pjeArquivo():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_ADMSADP"),os.getenv("TB_ARQUIVO")))

@app.route('/pje/admsadp/arquivo-local', methods=['GET'])
def pjeArquivoLocal():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_ADMSADP"),os.getenv("TB_ARQUIVO_LOCAL")))

@app.route('/pje/admsadp/processo', methods=['GET'])
def pjeAdmSadpProcesso():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_ADMSADP"),os.getenv("TB_PROCESSO")))

@app.route('/pje/admsadp/processo-zona', methods=['GET'])
def pjeAdmSadpPProcessoZona():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_ADMSADP"),os.getenv("TB_PROCESSO_ZONA")))

@app.route('/pje/admsadp/protocolo', methods=['GET'])
def pjeProtocolo():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_ADMSADP"),os.getenv("TB_PROTOCOLO")))


@app.route('/pje/processo/processo', methods=['GET'])
def pjeProcesso():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_PROCESSO"),os.getenv("TB_PROCESSO")))

@app.route('/pje/processo/data-processo', methods=['GET'])
def pjeDataProcesso():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_PROCESSO"),os.getenv("TB_DATA_PROCESSO")))

@app.route('/pje/rn-1g/processo', methods=['GET'])
def pjeRNg1Processo():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_RN_1G"),os.getenv("TB_PROCESSO_RN_1G")))
@app.route('/pje/rn-1g/data-processo', methods=['GET'])

def pjeRNg1DataProcesso():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_RN_1G"),os.getenv("TB_DATA_PROCESSO_RN_1G")))

@app.route('/pje/rn-2g/processo', methods=['GET'])
def pjeRNg2Processo():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_RN_2G"),os.getenv("TB_PROCESSO_RN_2G")))

@app.route('/pje/rn-2g/data-processo', methods=['GET'])
def pjeRNg2DataProcesso():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_RN_2G"),os.getenv("TB_DATA_PROCESSO_RN_2G")))

@app.route('/pje/sadp/processo', methods=['GET'])
def pjeSadpProcesso():
    return jsonify(api.Api(os.getenv('DB_PJE'),os.getenv("SCHEMA_SADP"),os.getenv("TB_SADP_PROCESSOS")))

""" 

    DB PARDAL

"""

load_dotenv('./environment/pardal.env')
@app.route('/pardal/denuncia', methods=['GET'])
def pardalDenuncia():
    return jsonify(api.Api(os.getenv('DB_PARDAL'),os.getenv("SCHEMA_PARDAL_PUBLIC"),os.getenv("TB_PARDAL_DENUNCIA")))

@app.route('/pardal', methods=['GET'])
def pardalLog():
    return jsonify(api.Api(os.getenv('DB_PARDAL'),os.getenv("SCHEMA_PARDAL"),os.getenv("TB_PARDAL")))

""" 

    DB DADOS

"""
load_dotenv('./environment/dados.env')
@app.route('/dados', methods=['GET'])
def dados():
    return jsonify(api.Api(os.getenv('DB_DADOS'),os.getenv("SCHEMA_DADOS"),os.getenv("TB_DADOS")))
""" 

    DB CAVE

"""
load_dotenv('./environment/cave.env')
@app.route('/cave', methods=['GET'])
def cave():
    return jsonify(api.Api(os.getenv('DB_CAVE'),os.getenv("SCHEMA_CAVE"),os.getenv("TB_CAVE")))
""" 

    DB SIAFI

"""
load_dotenv('./environment/siafi.env')
@app.route('/siafi/execucao-orcamentaria', methods=['GET'])
def siafiExec():
    return jsonify(api.Api(os.getenv('DB_SIAFI'),os.getenv("SCHEMA_SIAFI"),os.getenv("TB_EXEC")))

@app.route('/siafi/importacao-dados', methods=['GET'])
def siafiData():
    return jsonify(api.Api(os.getenv('DB_SIAFI'),os.getenv("SCHEMA_SIAFI"),os.getenv("TB_SIAFI_DATA")))

""" 

    DB BIAUDI

"""
load_dotenv('./environment/biaudi.env')
@app.route('/biaudi/deliberacoes', methods=['GET'])
def biaudiDelib():
    return jsonify(api.Api(os.getenv('DB_BIAUDI'),os.getenv("SCHEMA_BIAUDI"),os.getenv("TB_BIAUDI")))


""" 

    DB BICRE

"""

load_dotenv('./environment/bicre.env')
@app.route('/bicre/rn-1g/multidimensional', methods=['GET'])
def bicre1GMult():
    return jsonify(api.Api(os.getenv('DB_BICRE'),os.getenv("SCHEMA_BICRE_1G"),os.getenv("TB_MULT_1G")))

@app.route('/bicre/rn-1g/processo', methods=['GET'])
def bicre1GProcesso():
    return jsonify(api.Api(os.getenv('DB_BICRE'),os.getenv("SCHEMA_BICRE_1G"),os.getenv("TB_PROCESSO_1G")))

@app.route('/bicre/rn-1g-andamento/multidimensional', methods=['GET'])
def bicre1GAndamentoMult():
    return jsonify(api.Api(os.getenv('DB_BICRE'),os.getenv("SCHEMA_BICRE_1G_ANDAMENTO"),os.getenv("TB_MULT_1G_ANDAMENTO")))

@app.route('/bicre/rn-1g-andamento/processo-evento', methods=['GET'])
def bicre1GAndamentoProcesso():
    return jsonify(api.Api(os.getenv('DB_BICRE'),os.getenv("SCHEMA_BICRE_1G_ANDAMENTO"),os.getenv("TB_PROCESSO_1G_ANDAMENTO")))

""" 

    DB BIINDICADORES

"""
load_dotenv('./environment/biindicadores.env')
@app.route('/biindicadores/md-indicadores-sadp', methods=['GET'])
def biindicadoresMdSadp():
    return jsonify(api.Api(os.getenv('DB_BIINDICADORES'),os.getenv("SCHEMA_BIINDICADORES"),os.getenv("TB_MD_INDICADORES")))

@app.route('/biindicadores/multi-dados', methods=['GET'])
def biindicadoresMultiDados():
    return jsonify(api.Api(os.getenv('DB_BIINDICADORES'),os.getenv("SCHEMA_BIINDICADORES"),os.getenv("TB_STG_MULTI_DADOS")))
@app.route('/biindicadores/multi-dados-1', methods=['GET'])
def biindicadoresMultiDados1():
    return jsonify(api.Api(os.getenv('DB_BIINDICADORES'),os.getenv("SCHEMA_BIINDICADORES"),os.getenv("TB_STG_MULTI_DADOS_1")))
@app.route('/biindicadores/multi-dados-2', methods=['GET'])
def biindicadoresMultiDados2():
    return jsonify(api.Api(os.getenv('DB_BIINDICADORES'),os.getenv("SCHEMA_BIINDICADORES"),os.getenv("TB_STG_MULTI_DADOS_2")))
@app.route('/biindicadores/multi-dados-sadp', methods=['GET'])
def biindicadoresMultiDadosSadp():
    return jsonify(api.Api(os.getenv('DB_BIINDICADORES'),os.getenv("SCHEMA_BIINDICADORES"),os.getenv("TB_STG_MULTI_DADOS_SADP")))


""" 

    DB BISAOF

"""
load_dotenv('./environment/bisaof.env')
@app.route('/bisaof/contratos-empenhos/multidimensional', methods=['GET'])
def bisaofContratosEmpenhos():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_EMPENHOS"),os.getenv("TB_MULTIDIMENSIONAL_EMPENHOS")))
@app.route('/bisaof/execucao-orcamentaria/multidimensional', methods=['GET'])
def bisaofExecOrcamentaria():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_EXEC_ORCAMENTARIA"),os.getenv("TB_MULTIDIMENSIONAL_EXEC_ORCAMENTARIA")))

@app.route('/bisaof/materiais-almoxarifado/multidimensional', methods=['GET'])
def bisaofAlmoxarifado():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_ALMOXARIFADO"),os.getenv("TB_MULTIDIMENSIONAL_ALMOXARIFADO")))

@app.route('/bisaof/materiais-nota-recebimento/multidimensional', methods=['GET'])
def bisaofNotaRecebimento():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_NOTA_RECEBIMENTO"),os.getenv("TB_MULTIDIMENSIONAL_NOTA_RECEBIMENTO")))

@app.route('/bisaof/materiais-nota-recebimento/ax-nota-recebimento', methods=['GET'])
def bisaofNotaRecebimentoAX():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_NOTA_RECEBIMENTO"),os.getenv("TB_RECEBIMENTO_AX_NOTA")))

@app.route('/bisaof/materiais-nota-recebimento/ax-nota-recebimento-item', methods=['GET'])
def bisaofNotaRecebimentoItemAX():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_NOTA_RECEBIMENTO"),os.getenv("TB_RECEBIMENTO_AX_NOTA_ITEM")))

@app.route('/bisaof/materiais-patrimonio/multidimensional', methods=['GET'])
def bisaofPatrimonioMultidimensional():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_PATRIMONIO"),os.getenv("TB_MULTIDIMENSIONAL_PATRIMONIO")))

@app.route('/bisaof/materiais-patrimonio/ul', methods=['GET'])
def bisaofPatrimonioUL():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_PATRIMONIO"),os.getenv("TB_PATRIMONIO_UL")))

@app.route('/bisaof/materiais-requisicao/atendimento', methods=['GET'])
def bisaofRequisicaoAtendimento():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_REQUISICAO"),os.getenv("TB_MULTIDIMENSIONAL_REQUISICAO_ATENDIMENTO")))

@app.route('/bisaof/materiais-requisicao/item', methods=['GET'])
def bisaofRequisicaoItem():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_REQUISICAO"),os.getenv("TB_MULTIDIMENSIONAL_REQUISICAO_ITEM")))

@app.route('/bisaof/materiais-requisicao/requisicao', methods=['GET'])
def bisaofRequisicao():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_REQUISICAO"),os.getenv("TB_MULTIDIMENSIONAL_REQUISICAO")))

@app.route('/bisaof/materiais-requisicao/asi-requisicao', methods=['GET'])
def bisaofRequisicaoASI():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_REQUISICAO"),os.getenv("TB_MULTIDIMENSIONAL_REQUISICAO_ASI")))

@app.route('/bisaof/materiais-requisicao/requisicao-ax-lote', methods=['GET'])
def bisaofRequisicaoAXLote():
    return jsonify(api.Api(os.getenv('DB_BISAOF'),os.getenv("SCHEMA_REQUISICAO"),os.getenv("TB_MULTIDIMENSIONAL_REQUISICAO_AX_LOTE")))

""" 

    DB BIAGE

"""
load_dotenv('./environment/biage.env')

@app.route('/biage/agua-esgoto/agua', methods=['GET'])
def biageAguaEsgoto():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_AGUA_ESGOTO"),os.getenv("TB_AGUA")))

@app.route('/biage/energia', methods=['GET'])
def biageEnergia():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_ENERGIA"),os.getenv("TB_ENERGIA")))

@app.route('/biage/impressoes', methods=['GET'])
def biageImpressoes():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_IMPRESSOES"),os.getenv("TB_IMPRESSOES")))

@app.route('/biage/indicador-geral', methods=['GET'])
def biageIndicadorGeral():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_INDICADOR_GERAL"),os.getenv("TB_INDICADOR_GERAL")))

@app.route('/biage/predios-tre', methods=['GET'])
def biagePrediosTRE():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_PREDIOS_TRE"),os.getenv("TB_PREDIOS_TRE")))

@app.route('/biage/qualidade-vida', methods=['GET'])
def biageQualidadeVida():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_QUALIDADE_VIDA"),os.getenv("TB_QUALIDADE_VIDA")))

@app.route('/biage/qualidade-vida-tre', methods=['GET'])
def biageQualidadeVidaTRE():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_QUALIDADE_VIDA_TRE"),os.getenv("TB_QUALIDADE_VIDA_TRE")))

@app.route('/biage/residuos', methods=['GET'])
def biageResiduos():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_RESIDUOS"),os.getenv("TB_RESIDUOS")))

@app.route('/biage/telefonia/movel', methods=['GET'])
def biageTelefoniaMovel():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_TELEFONIA"),os.getenv("TB_TELEFONIA_MOVEL")))

@app.route('/biage/telefonia/fixa', methods=['GET'])
def biageTelefoniaFixa():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_TELEFONIA"),os.getenv("TB_TELEFONIA_FIXA")))

@app.route('/biage/veiculos/abastecimento', methods=['GET'])
def biageVeiculosAbastecimento():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_VEICULOS"),os.getenv("TB_ABASTECIMENTO")))

@app.route('/biage/veiculos/manutencao', methods=['GET'])
def biageVeiculosManutencao():
    return jsonify(api.Api(os.getenv('DB_BIAGE'),os.getenv("SCHEMA_VEICULOS"),os.getenv("TB_MANUTENCAO")))

""" 

    DB BIEJE

"""
load_dotenv('./environment/bieje.env')

@app.route('/bieje/capacitacao/acao-externa', methods=['GET'])
def biejeCapacitacao():
    return jsonify(api.Api(os.getenv('DB_BIEJE'),os.getenv("SCHEMA_CAPACITACAO"),os.getenv("TB_ACAOCAPEXTERNA")))

@app.route('/bieje/public/acao-externa', methods=['GET'])
def biejeAcaoExterna():
    return jsonify(api.Api(os.getenv('DB_BIEJE'),os.getenv("SCHEMA_PUBLIC_EJE"),os.getenv("TB_ACAOCAPEXTERNA_PUBLIC,")))


""" 

    DB BISGP

"""
load_dotenv('./environment/bisgp.env')
@app.route('/bisgp/aposentadoria', methods=['GET'])
def bisgpAposentadoria():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_APOSENTADORIA"),os.getenv("TB_MULTI_APOSENTADORIA")))

@app.route('/bisgp/beneficio', methods=['GET'])
def bisgpBeneficio():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_BENEFICIO"),os.getenv("TB_MULTI_BENEFICIO")))

@app.route('/bisgp/cad-prev', methods=['GET'])
def bisgpCadPrev():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_CAD_PREV"),os.getenv("TB_ENTIDADE_CAD")))

@app.route('/bisgp/calculos-conferencia', methods=['GET'])
def bisgpCalculoConferencia():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_CALCULOS_CONFERENCIA"),os.getenv("TB_MULT_CALCULO")))

@app.route('/bisgp/emprestimos', methods=['GET'])
def bisgpEmprestimos():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_EMPRESTIMOS"),os.getenv("TB_MULT_EMPRESTIMOS")))

@app.route('/bisgp/folha-beneficio', methods=['GET'])
def bisgpFolhaBeneficio():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_FOLHA_BENEFICIO"),os.getenv("TB_MULTI_FOLHA")))

@app.route('/bisgp/limite-rgps', methods=['GET'])
def bisgpLimiteRgps():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_RGPS_HIST"),os.getenv("TB_MULTI_RGPS_HIST")))

@app.route('/bisgp/hora-base-hist', methods=['GET'])
def bisgpHorabaseHist():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_HORA_BASE"),os.getenv("TB_MULTI_HORA_BASE")))

@app.route('/bisgp/margem-folha/mrg-base', methods=['GET'])
def bisgpMRGbase():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_MARGEM_FOLHA"),os.getenv("TB_MRG_BASE")))

@app.route('/bisgp/margem-folha/mrg-consig', methods=['GET'])
def bisgpMRGconsig():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_MARGEM_FOLHA"),os.getenv("TB_MRG_CONSIG")))

@app.route('/bisgp/margem-folha', methods=['GET'])
def bisgpMargemFolha():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_MARGEM_FOLHA"),os.getenv("TB_MULTI_MARGEM_FOLHA")))

@app.route('/bisgp/pensao', methods=['GET'])
def bisgpPensao():
    return jsonify(api.Api(os.getenv('DB_BISGP'),os.getenv("SCHEMA_PENSAO"),os.getenv("TB_MULTI_PENSAO")))


""" 

    DB BISJ

"""
# > IPLENO 
load_dotenv('./environment/bisj.env')
@app.route('/bisj/ipleno/acao', methods=['GET'])
def bisjIplenoAcao():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO"),os.getenv("TB_STG_ACAO")))

@app.route('/bisj/ipleno/acao-pje', methods=['GET'])
def bisjIplenoAcaoPJE():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO"),os.getenv("TB_STG_ACAO_PJE")))

@app.route('/bisj/ipleno/acao-sadp', methods=['GET'])
def bisjIplenoAcaoSADP():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO"),os.getenv("TB_STG_ACAO_SADP")))

@app.route('/bisj/ipleno/autoridade', methods=['GET'])
def bisjIplenoAutoridade():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO"),os.getenv("TB_STG_AUTORIDADE")))

@app.route('/bisj/ipleno/decisao', methods=['GET'])
def bisjIplenoDecisao():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO"),os.getenv("TB_STG_DECISAO")))

@app.route('/bisj/ipleno/dominio', methods=['GET'])
def bisjIplenoDominio():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO"),os.getenv("TB_STG_DOMINIO")))

@app.route('/bisj/ipleno/ind-julg', methods=['GET'])
def bisjIplenoIndJulg():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO"),os.getenv("TB_STG_IND_JULG")))

@app.route('/bisj/ipleno/item-julg', methods=['GET'])
def bisjIplenoItemJulg():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO"),os.getenv("TB_STG_ITEM_JULG")))

@app.route('/bisj/ipleno/membro', methods=['GET'])
def bisjIplenoMembro():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO"),os.getenv("TB_STG_MEMBRO")))

@app.route('/bisj/ipleno/sessao', methods=['GET'])
def bisjIplenoSessao():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO"),os.getenv("TB_STG_SESSAO")))

# > IPLENO PROCESSO

@app.route('/bisj/ipleno-processo/assunto', methods=['GET'])
def bisjIplenoAssunto():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_PROCESSO"),os.getenv("TB_STG_ASSUNTO")))
@app.route('/bisj/ipleno-processo/assunto-sadp', methods=['GET'])
def bisjIplenoAssuntoSADP():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_PROCESSO"),os.getenv("TB_STG_ASSUNTO_SADP")))
@app.route('/bisj/ipleno-processo/parte-sadp', methods=['GET'])
def bisjIplenoParteSADP():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_PROCESSO"),os.getenv("TB_STG_PARTE_SADP")))
@app.route('/bisj/ipleno-processo/pje-sadp', methods=['GET'])
def bisjIplenoPJEsadp():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_PROCESSO"),os.getenv("TB_STG_PJE_SADP")))
@app.route('/bisj/ipleno-processo/proc-part-ass-pje', methods=['GET'])
def bisjIplenoProcPartAssPJE():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_PROCESSO"),os.getenv("TB_STG_PROC_PART_ASS_PJE")))
@app.route('/bisj/ipleno-processo/processo-partes-sadp', methods=['GET'])
def bisjIplenoProcessoPartesSADP():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_PROCESSO"),os.getenv("TB_STG_PROCESSO_PARTES_SADP")))
@app.route('/bisj/ipleno-processo/processo-partes', methods=['GET'])
def bisjIplenoProcessoPartes():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_PROCESSO"),os.getenv("TB_STG_PROCESSO_PARTES")))
@app.route('/bisj/ipleno-processo/processo-sadp', methods=['GET'])
def bisjIplenoProcessoSADP():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_PROCESSO"),os.getenv("TB_STG_PROCESSO_SADP")))
@app.route('/bisj/ipleno-processo/sadp', methods=['GET'])
def bisjIplenoSADP():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_PROCESSO"),os.getenv("TB_STG_SADP")))


# > IPLENO SESSAO

@app.route('/bisj/ipleno-sessao/dados', methods=['GET'])
def bisjIplenoDados():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_SESSAO"),os.getenv("TB_STG_DADOS")))

@app.route('/bisj/ipleno-sessao/fato', methods=['GET'])
def bisjIplenoFato():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_SESSAO"),os.getenv("TB_STG_FATO")))

@app.route('/bisj/ipleno-sessao/sessao-mem-sub', methods=['GET'])
def bisjIplenoSessaoMemSub():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_IPLENO_SESSAO"),os.getenv("TB_STG_SESSAO_MEM_SUB")))

# PJE ATA

@app.route('/bisj/pje-ata/processo-parte', methods=['GET'])
def bisjPJEataProcesso():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_PJE_ATA"),os.getenv("TB_STG_PROCESSO_PARTE")))

# PJE RELATORIO

@app.route('/bisj/pje-relatorio/multi-dados', methods=['GET'])
def bisjPJErelatorioDados():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_PJE_RELATORIO"),os.getenv("TB_STG_MULTI_DADOS")))

# PJE RN 2G

@app.route('/bisj/pje-rn-2g/multidimensional', methods=['GET'])
def bisjPjeRN2gMultidimensional():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_PJE_RN_2G"),os.getenv("TB_MULTIDIMENSIONAL_PJE_2G")))

@app.route('/bisj/pje-rn-2g/processo', methods=['GET'])
def bisjPjeRN2gProcesso():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_PJE_RN_2G"),os.getenv("TB_STG_PROCESSO")))

# PJE RN 2G ANDAMENTO

@app.route('/bisj/pje-rn-2g-andamento/multidimensional', methods=['GET'])
def bisjPjeRN2gAndamentoMultidimensional():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_PJE_RN_2G_ANDAMENTO"),os.getenv("TB_MULTIDIMENSIONAL_PJE_2G_ANDAMENTO")))

@app.route('/bisj/pje-rn-2g-andamento/processo', methods=['GET'])
def bisjPjeRN2gAndamentoProcesso():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_PJE_RN_2G_ANDAMENTO"),os.getenv("TB_STG_PROCESSO_EVENTO")))



# PRESTACAO CONTAS

@app.route('/bisj/prestacao-contas', methods=['GET'])
def bisjPrestacaoDados():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_PRESTACAO_CONTAS"),os.getenv("TB_STG_PRESTACAO_CONTAS")))

@app.route('/bisj/prestacao-contas/multi-dados', methods=['GET'])
def bisjPrestacaoMultiDados():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_PRESTACAO_CONTAS"),os.getenv("TB_STG_MULTI_DADOS")))

# PRESTACAO CONTAS PLANILHA

@app.route('/bisj/prestacao-contas-planilha/dados-mistos', methods=['GET'])
def bisjPrestacaoDadosMistos():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_PRESTACAO_CONTAS_PLANILHA"),os.getenv("TB_STG_DADOS_MISTOS")))

@app.route('/bisj/prestacao-contas-planilha', methods=['GET'])
def bisjPrestacaoContasPlanilha():
    return jsonify(api.Api(os.getenv('DB_BISJ'),os.getenv("SCHEMA_PRESTACAO_CONTAS_PLANILHA"),os.getenv("TB_PRESTACAO_CONTAS_PLANILHA")))


""" 

    DB BISTIE

"""
load_dotenv('./environment/bistie.env')
@app.route('/bistie/acao', methods=['GET'])
def bistieAcao():
    return jsonify(api.Api(os.getenv('DB_BISTIE'),os.getenv("SCHEMA_ACAO"),os.getenv("TB_ACAO")))

@app.route('/bistie/indicador', methods=['GET'])
def bistieIndicador():
    return jsonify(api.Api(os.getenv('DB_BISTIE'),os.getenv("SCHEMA_INDICADOR"),os.getenv("TB_INDICADOR")))

@app.route('/bistie/iniciativa', methods=['GET'])
def bistieIniciativa():
    return jsonify(api.Api(os.getenv('DB_BISTIE'),os.getenv("SCHEMA_INICIATIVA"),os.getenv("TB_INICIATIVA")))

@app.route('/bistie/orcamento', methods=['GET'])
def bistieOrcamento():
    return jsonify(api.Api(os.getenv('DB_BISTIE'),os.getenv("SCHEMA_ORCAMENTO"),os.getenv("TB_EXECUCAO")))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)