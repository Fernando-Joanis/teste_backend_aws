from datetime import datetime
from orm_db.orm_db import ObjectTest


class DataSerializer:
    def __init__(self, data: dict):
        self.originador = data['Originador']
        self.doc_originador = self.convert_int(self.format_cpf_cnpj(data['Doc Originador']))
        self.cedente = data['Cedente']
        self.doc_cedente = self.convert_int(data['Doc Cedente'])
        self.ccb = self.convert_int(data['CCB'])
        self.id = self.convert_int(data['Id'])
        self.cliente = data['Cliente']
        self.cpf_cnpj = self.format_cpf_cnpj(data['CPF/CNPJ'])
        self.endereco = data['Endereço']
        self.cep = data['CEP']
        self.cidade = data['Cidade']
        self.uf = data['UF']
        self.valor_do_emprestimo = self.convert_float(data['Valor do Empréstimo'])
        self.parcela_valor = self.convert_float(data['Parcela R$'])
        self.total_parcela = self.convert_int(data['Total Parcelas'])
        self.parcela = self.convert_int(data['Parcela #'])
        self.data_emissao = self.format_date(data['Data de Emissão'])
        self.data_vencimento = self.format_date(data['Data de Vencimento'])
        self.preco_aquisicao = self.convert_float(data['Preço de Aquisição'])

    @staticmethod
    def convert_float(number):
        number = number.replace(',', '.')
        new_number = ''
        for n in number:
            if n.isalpha():
                continue
            new_number += n
        return float(new_number)

    @staticmethod
    def convert_int(number):
        new_number = ''
        for n in number:
            if not n.isnumeric():
                continue
            new_number += n
        return int(new_number)

    @staticmethod
    def format_date(date):
        new_date = datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d')
        new_date = datetime.strptime(new_date, '%Y-%m-%d').date()
        return new_date

    @staticmethod
    def format_cpf_cnpj(cpf_cnpj):
        new_cpf_cnpj = ''
        for number in cpf_cnpj:
            try:
                int(number)
                new_cpf_cnpj += number
            except Exception as e:
                ...
        return new_cpf_cnpj

    def create_obj(self):
        obj = ObjectTest(
            ORIGINADOR=self.originador,
            DOC_ORIGINADOR=self.doc_originador,
            CEDENTE=self.cedente,
            DOC_CEDENTE=self.doc_cedente,
            CCB=self.ccb,
            ID_EXTERNO=self.id,
            CLIENTE=self.cliente,
            CPF_CNPJ=self.cpf_cnpj,
            ENDERECO=self.endereco,
            CEP=self.cep,
            CIDADE=self.cidade,
            UF=self.uf,
            VALOR_DO_EMPRESTIMO=self.valor_do_emprestimo,
            VALOR_PARCELA=self.parcela_valor,
            TOTAL_PARCELAS=self.total_parcela,
            PARCELA=self.parcela,
            DATA_DE_EMISSAO=self.data_emissao,
            DATA_DE_VENCIMENTO=self.data_vencimento,
            PRECO_DE_AQUISICAO=self.preco_aquisicao
        )
        return obj
