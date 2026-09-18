from datetime import date

def model_lead(nome, email, status):
    return {
            "Name": nome,
            "email": email,
            "status": status,
            "created": date.today().isoformat()
        }