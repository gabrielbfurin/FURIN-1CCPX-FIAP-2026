from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    status = input("Estado do fluxo de vendas: ")

    # validar os dados
    # modelar os dados, para isso, vamos usar o modulo - "model.py"
    model_lead(name, email, status)

    # com os dados modelados, preciso enviar para o JSON
    # vou usar o control para enviar o dicionario do lead
    control.create_lead(model_lead(name, email, status))

    print("Lead adicionado!")

def list_leads():
    leads = control.read_leads()

    print(f"## | {"Nome":<10} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead['Name']:<10} | {lead['email']}")

def search_leads():
    query = input("Buscar por: ").strip()

    if not query:
        print("Consulta vazia")
        return

    # com a query digitada (busca)... preciso enviar para o control
    # o control ira comparar a query com os dados do leads.json
    # e ira retornar os resultados

    leads_found = control.read_leads_research(query)

    print(f"## | {"Nome":<10} | E-mail")
    for i, lead in leads_found:
        print(f"{i:02d} | {lead['Name']:<10} | {lead['email']}")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possivel exportar.")
    else:
        print("Exportado para {path_csv}")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar Lead")
        print("[2] Listar Leads")
        print("[3] Buscar (nome/email)")
        print("[4] Exportar para CSV")
        print("[0] Sair do programa")

        opt = input("\nEscolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção invalida")

if __name__ == "__main__":
    main()