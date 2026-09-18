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
        print(f"{i:02d} | {lead['nome']:<10} | {lead['email']}")



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