from datetime import date
from datetime import datetime

def date_para_str(data: date) -> str:
    return data.strftime('%d/%n/%Y')

def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%n/%Y')

def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'