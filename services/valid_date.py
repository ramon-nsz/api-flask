from datetime import datetime


def valid_date(data_nascimento):
    #Valida se a data fornecida está no formato 'YYYY/MM/DD'.
    try:
        # Tenta converter a string para um objeto datetime no formato 'YYYY/MM/DD'
        return datetime.strptime(data_nascimento, '%Y-%m-%d')
    except ValueError:
        return None  # Retorna None se o formato estiver errado