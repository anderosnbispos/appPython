# data e hora
# - Como recuperar a data atual
# - Como trabalhar com a data, alterando sua formatação
# - Como gerar um horário (TIME)
# - Retornar data e hora atual (DATETIME)
# - Atlerar formação do DATETIME
# - Realizar soma e subtração de datas com TIMEDELTA

# importa biblioteca
from datetime import date, time, datetime, timedelta

# data atual (date)
def trabalhando_com_date():
    dt = date.today()
    dt_str = dt.strftime('%A %d-%m-%Y')
    print(type(dt))
    print(type(dt_str))
    print(dt.strftime('%A %d-%m-%Y'))

#trabalhando com time
def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))
    print(type(horario))
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

#trablhando com datetime
def trabalhando_com_datetime():
    data_atual = datetime.now()
    data_hoje = datetime.today()
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_hoje.weekday())
    print(data_hoje.day)
    print(data_hoje.month)
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada.strftime(('%c')))
    data_string = '01/01/2021'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)

def trabalhando_com_timedelta():
    data_string = '01/01/2021'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(type(data_convertida))
    data_hoje = datetime.today()
    print(data_hoje)
    nova_data = data_hoje + timedelta(days=30, hours=1, minutes=15)
    print(nova_data)

# teste das tuplas, assunto de outra aula
def teste_tupla():
    tupla = (1, 12, 10, 14)
    print(tupla[1])


if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    # trabalhando_com_datetime()
    # teste_tupla()
    trabalhando_com_timedelta()