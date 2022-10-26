def get_methods():
    credito = ['MASTER CREDITO','MASTERCARD CREDITO ', 'VISA CREDITO ', 'ELO CREDITO ', 'HIPERCARD ', 'AMERICAN EXPRESS ']
    debito = ['MASTER DEBITO ', 'MASTERCARD DEBITO', 'ELO DEBITO ', 'VISA DEBITO ', 'ELECTRON ']
    dinheiro = ['DINHEIRO ']
    pix = ['PIX']
    ifood = ['IFOOD ']
    americanas = ['AMERICANAS DELIVERY ']
    voucher = ['ALELO REFEICAO ','VOUCHER FUNCIONARIO ', 'VOUCHER CORTERSIA ',
           'VOUCHER LATAM ', 'VOUCHER AZUL ']
    
    result = {"credito":credito, "debito":debito, 'dinheiro':dinheiro, 'pix':pix, 'ifood':ifood, 'americanas':americanas, "voucher":voucher}
    return result

# TODO transformar em um dicionário
