from sqlalchemy import create_engine, Column, VARCHAR, DATE, DECIMAL, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ

engine = create_engine(
    f'mysql+pymysql://{environ["USER_DB"]}:{environ["PSW_DB"]}@{environ["HOST_DB"]}:{environ["PORT_DB"]}/{environ["NAME_DB"]}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class ObjectTest(Base):
    __tablename__ = 'teste_backend'

    ID_CESSAO = Column(INTEGER, primary_key=True)
    ORIGINADOR = Column(VARCHAR(250), nullable=False)
    DOC_ORIGINADOR = Column(INTEGER, nullable=False)
    CEDENTE = Column(VARCHAR(250), nullable=False)
    DOC_CEDENTE = Column(INTEGER, nullable=False)
    CCB = Column(INTEGER, nullable=False)
    ID_EXTERNO = Column(INTEGER, nullable=False)
    CLIENTE = Column(VARCHAR(250), nullable=False)
    CPF_CNPJ = Column(VARCHAR(50), nullable=False)
    ENDERECO = Column(VARCHAR(250), nullable=False)
    CEP = Column(VARCHAR(50), nullable=False)
    CIDADE = Column(VARCHAR(250), nullable=False)
    UF = Column(VARCHAR(50), nullable=False)
    VALOR_DO_EMPRESTIMO = Column(DECIMAL(10, 2), nullable=False)
    VALOR_PARCELA = Column(DECIMAL(10, 2), nullable=False)
    TOTAL_PARCELAS = Column(INTEGER, nullable=False)
    PARCELA = Column(INTEGER, nullable=False)
    DATA_DE_EMISSAO = Column(DATE, nullable=False)
    DATA_DE_VENCIMENTO = Column(DATE, nullable=False)
    PRECO_DE_AQUISICAO = Column(DECIMAL(10, 2), nullable=False)


def add_and_commit_db(list_obj):
    session.add_all(list_obj)
    session.commit()
