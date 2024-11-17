import pywhatkit as kit

# Insira o número de telefone no formato internacional
numero_telefone = "+5516997788161"  # Exemplo para o Brasil
mensagem = "Olá! Esta é uma mensagem automática enviada com Python! Ps: Eu te amo S2"
horario_hora = 15  # Hora do envio (formato 24 horas)
horario_minuto = 47  # Minuto do envio
 
 # enviar sem esperar um horário específico
kit.sendwhatmsg_instantly("+5511999999999", "Mensagem enviada instantaneamente!")

 # enviar mensagns para um grupo: Use ID do grupo do WhatsAPP Web
kit.sendwhatmsg_to_group("ID_DO_GRUPO", "Mensagem para o grupo", 15, 45)


try:
    # Enviar mensagem
    kit.sendwhatmsg(numero_telefone, mensagem, horario_hora, horario_minuto)
    print("Mensagem enviada com sucesso!")
except Exception as e:
    print(f"Erro ao enviar mensagem: {e}")
