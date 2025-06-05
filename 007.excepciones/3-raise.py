
# raise
emails = ["dani@example.com", "alan@example.com", "aroa@example.com"]


def validate_email(email):
    if email in emails:
        raise Exception("Email ya registrado")
    else:
        print("Email válido")


try:
    validate_email("alan@example.com")
except Exception as e:
    print("Error capturado")

print("fin")