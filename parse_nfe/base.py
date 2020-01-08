import xmltodict


class _Parse:

    def __init__(self):
        self._nf = None

    def set_xml(self, xml):
        try:
            self._nf = xmltodict.parse(xml)
        except:
            print('Erro no parse do arquivo')

        if self._nf['nfeProc'].get('nfeProc'):
            self._nf = self._nf['nfeProc']

    def id(self):
        return self._nf['nfeProc']['NFe']['infNFe']['@Id']

    def ide(self):
        return self._nf['nfeProc']['NFe']['infNFe']['ide']

    def emitente(self):
        return self._nf['nfeProc']['NFe']['infNFe']['emit']

    def ender_emit(self):
        return self._nf['nfeProc']['NFe']['infNFe']['emit']['enderEmit']

    def destinatario(self):
        return self._nf['nfeProc']['NFe']['infNFe']['dest']

    def det_itens(self):
        if type(self._nf['nfeProc']['NFe']['infNFe']['det']) != type([]):
            return [self._nf['nfeProc']['NFe']['infNFe']['det']]
        else:
            return self._nf['nfeProc']['NFe']['infNFe']['det']

    def total(self):
        return self._nf['nfeProc']['NFe']['infNFe']['total']['ICMSTot']

    def transp(self):
        return self._nf['nfeProc']['NFe']['infNFe']['transp']

    def fatura(self):
        if not self._nf['nfeProc']['NFe']['infNFe'].get('cobr'):
            return None
        return self._nf['nfeProc']['NFe']['infNFe']['cobr']['fat']

    def duplicata(self):
        if self._nf['nfeProc']['NFe']['infNFe'].get('cobr') is None:
            return None

        if self._nf['nfeProc']['NFe']['infNFe']['cobr'].get('dup'):
            if type(self._nf['nfeProc']['NFe']['infNFe']['cobr']['dup']) != type([]):
                return [self._nf['nfeProc']['NFe']['infNFe']['cobr']['dup']]
            else:
                return self._nf['nfeProc']['NFe']['infNFe']['cobr']['dup']

    def det_pagamento(self):

        if self._nf['nfeProc']['NFe']['infNFe'].get('pag') is None:
            return None

        if type(self._nf['nfeProc']['NFe']['infNFe']['pag']['detPag']) != type([]):
            return [self._nf['nfeProc']['NFe']['infNFe']['pag']['detPag']]
        else:
            return self._nf['nfeProc']['NFe']['infNFe']['pag']['detPag']

    def info_adicionais(self):
        if self._nf['nfeProc']['NFe']['infNFe'].get('infAdic') is None:
            return None
        return self._nf['nfeProc']['NFe']['infNFe']['infAdic']['infCpl']

    def tec_responsavel(self):
        return self._nf['nfeProc']['NFe']['infNFe']['infRespTec']

    def assinatura(self):
        return self._nf['nfeProc']['NFe']['Signature']

    def protocolo(self):
        return self._nf['nfeProc']['protNFe']


parse_nf = _Parse()
