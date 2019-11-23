`pyparse-nfebr`` - Parse em Notas Fiscais Eletronicas Brasileiras
################################################################


Description
***********

Lê os nós de xml de notas fiscais eletronicas brasileiras


Requirements
************

::

    Python 3
    xmltodict==0.12.0


Environment:
************

::

    linux


Install:
########

::

    pip install pyparse-nfebr


Usage
#####


>>> from parse_nfe.bas import parse_nf
>>> parse_nf.set_xml(arquivo_xml)


id (Propriedade)
*********************
Retorna o id da Nota Fiscal

|

Sintaxe:

- parse_nf.id

|

*Exemplo:*

>>> print (parse_nf.id)


----

lide (Método)
*********************
Retorna um dicionário com o nó ide da Nota.

|

sintaxe:

- parse_nf.ide,

*Exemplo:*

>>> print(parse_nf.ide)


:Authors:
    Sidon Duarte,
    Luan Fernandes

:Version: 0.0.1 of 2019/11/23