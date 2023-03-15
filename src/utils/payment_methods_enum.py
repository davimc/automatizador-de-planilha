
def get_methods():
    credito = ['MASTER CREDITO ','MASTERCARD CREDITO ','MAESTRO CREDITO ','VISA CREDITO ','ELO CREDITO ','HIPERCARD ','AMERICAN EXPRESS ']
    debito = ['MASTER DEBITO ','MASTERCARD DEBITO ','MAESTRO DEBITO ','ELO DEBITO ','VISA DEBITO ','ELECTRON ']
    dinheiro = ['DINHEIRO ']
    pix = ['PIX ']
    ifood = ['IFOOD ']
    voucher = ['ALELO REFEICAO ','VOUCHER FUNCIONARIO ','VOUCHER CORTESIA ',
           'VOUCHER LATAM ','VOUCHER AZUL ']
    
    result = {"credito":credito, "debito":debito, 'dinheiro':dinheiro, 'pix':pix, 'ifood':ifood, "voucher":voucher}
    return result
