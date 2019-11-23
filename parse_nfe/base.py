import xmltodict

class _Parse:

    def set_xml(self, xml):
        try:
            self._nf = xmltodict.parse(xml)
        except:
            print('Erro no parse do arquivo')

    def id(self):
        return self._nf['nfeProc']['NFe']['infNFe']['@Id']

    def ide(self):
        return self._nf['nfeProc']['NFe']['infNFe']['ide']

    def emitente(self):
        return self._nf['nfeProc']['NFe']['infNFe']['emit']

    def destinatario(self):
        return self._nf['nfeProc']['NFe']['infNFe']['dest']

    def det_itens(self):
        return self._nf['nfeProc']['NFe']['infNFe']['det']

    def total(self):
        return self._nf['nfeProc']['NFe']['infNFe']['total']

    def transportadora(self):
        return self._nf['nfeProc']['NFe']['infNFe']['transp']

    def cobranca(self):
        return self._nf['nfeProc']['NFe']['infNFe']['cobr']

    def det_pagamento(self):
        return self._nf['nfeProc']['NFe']['infNFe']['pag']

    def info_adicionais(self):
        return self._nf['nfeProc']['NFe']['infNFe']['infAdic']

    def tec_responsavel(self):
        return self._nf['nfeProc']['NFe']['infNFe']['infRespTec']

    def assinatura(self):
        return self._nf['nfeProc']['NFe']['Signature']
    
    def protocolo(self):
        return self._nf['nfeProc']['protNFe']


parse_nf = _Parse()