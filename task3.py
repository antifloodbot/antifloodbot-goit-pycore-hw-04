import re

def normalize_phone(phone_number: str) -> str:

    phone_number = re.sub(r"[^\d+]", "", phone_number)

    if phone_number.startswith("+"):
        if phone_number.startswith("+380"):
            return phone_number
        return phone_number

    if phone_number.startswith("380"):
        return f"+{phone_number}"

    return f"+38{phone_number}"