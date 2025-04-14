import asyncio

async def registrar_log(log):
    try:
        with open("logs.txt", "a") as file:
            file.write(log + "\n")
        print("[INFO] Log registrado com sucesso!")
    except Exception as e:
        print(f"[ERRO] Falha ao registrar log: {e}")

async def handle_client(reader, writer, port):
    client_address = writer.get_extra_info('peername')
    log = f"[ALERTA] Conexão detectada na porta {port} de: {client_address}\n"

    try:
        data = await reader.read(1024)
        log += f"[DADOS BRUTOS] Recebido: {data}\n"
    except Exception as e:
        log += f"[ERRO AO RECEBER DADOS]: {e}\n"

    await registrar_log(log)

    response = "Servidor simulado: Acesso negado."
    writer.write(response.encode('utf-8'))
    await writer.drain()
    writer.close()

async def honeypot():
    host = '0.0.0.0'
    ports = [9000]

    banner = """
    ##################################################
    #                                                #
    #                 Sentinela Ativo                #
    #           Monitorando conexões de Rede         #
    #                                                #
    ##################################################
    """
    print(banner)
    print("[INFO] O honeypot está aguardando intrusão...")

    tasks = []
    for port in ports:
        try:
            server = await asyncio.start_server(
                lambda r, w: handle_client(r, w, port),
                host,
                port
            )
            tasks.append(server)
        except Exception as e:
            print(f"[ERRO] Não foi possível iniciar o servidor na porta {port}: {e}")

    await asyncio.gather(*[server.serve_forever() for server in tasks])

# Função para criar o arquivo requirements.txt
def criar_requirements():
    try:
        with open("requirements.txt", "w") as file:
            file.write("asyncio\n")
            file.write("scapy\n")
        print("[INFO] Arquivo requirements.txt criado com sucesso!")
    except Exception as e:
        print(f"[ERRO] Não foi possível criar o arquivo requirements.txt: {e}")

if __name__ == "__main__":
    try:
        criar_requirements()  # Cria o arquivo requirements.txt
        asyncio.run(honeypot())  # Inicia o honeypot
    except KeyboardInterrupt:
        print("\n[INFO] Servidor encerrado pelo usuário.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro: {e}")
