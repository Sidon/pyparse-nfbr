# Parse em Notas Fiscais Eletrônicas Brasileiras

### Descrição
- Lê os nós de xml de notas fiscais eletrônicas brasileiras

### Requerimentos

>`Python=>=3.6`
>`xmltodict==0.12.0`

### Sistemas

> `Linux`
> `Windows`
> `Mac`

### Instalação
> `pip install pyparse-nfebr`

#### Exemplo

```python
from parse_nfe.bas import parse_nf

parse = parse_nf.set_xml(arquivo_xml)
print(parse_nf.id)
```
### Funções

|  Nome               |               Retorno                           | Tipo     |
| :------------------ |:----------------------------------------------- |:--------:|
| `id()`              |*id da Nota Fiscal.*                             | int      |
| `ide()`             |*Informações de identificação*                   | dict     |
| `emitente()`        |*Informações do imitente*                        | dict     |
| `destinatario()`    |*Informações do destinatário*                    | list     |
|`det_itens()`        |*Produto(s) contidos na nota.*                   | dict     |
| `total()`           |*Todos valores da nota*                          | dict     |
|`transportadora()`   |*Informações de transporte*                      | dict     |
| `cobranca()`        |*Informações sobre cobrança*                     | dict     |
|`det_pagamento()`    |*Meio de pagamento e valor da soma.*             | dict     |
| `info_adicionais()` |*Informações Complementares*                     | string   |
|`tec_responsavel()`  |*Técnico Responsável.*                           | dict     |
| `assinatura()`      |*Assinatura digital da nota*                     | dict     | 
|`protocolo()`        |*Número de protocolo,chave e status nota.*       | string   |
	
### Autores:

[Sidon Duarte](https://github.com/Sidon) | [Luan Fernandes](https://github.com/souluanf)
