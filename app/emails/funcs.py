from mailjet_rest import Client


mailjet = Client(auth=("93756b68ede318c14f2b66e96dae6d15", "810ee18740518f7902cbf67a945d9b04"), version='v3.1')
def send_email(dest:str, dest_name:str, codigo_2af:str):
    data = {
        "Messages": [
            {
                "From": {
                    "Email": "tuitroper@gmail.com",
                    "Nome": "2auth project"
                },
                "To": [
                    {
                        'Email': dest,
                        "Name": dest_name
                    }
                ],
                "Subject": f"{dest_name}Seu codigo de autenticação de dois fatores para login",
                "TextPart": f"{dest_name} para logar copie este codigo  ( {codigo_2af} ) ",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    return result.status_code, result.json()


def send_email_boas_vindas(dest:str, dest_name:str, link:str):
    data = {
        "Messages": [
            {
                "From": {
                    "Email": "tuitroper@gmail.com",
                    "Nome": "2auth project"
                },
                "To": [
                    {
                        'Email': dest,
                        "Name": dest_name
                    }
                ],
                "Subject": f"{dest_name} Seja bem vindo a nossa plataforma!",
                "TextPart": f"Para verificar sua conta clique nesete link {link}",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    return result.status_code, result.json()