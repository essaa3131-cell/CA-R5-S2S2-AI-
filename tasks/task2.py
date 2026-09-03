import re


def process_email(email):
    if email.count("@") != 1:
        return "Invalid email"

    username, domain_part = email.split("@")

    if "." not in domain_part:
        return "Invalid email"

    domain_name = domain_part.rsplit(".", 1)[0]

    if email.endswith(".com"):
        domain_type = "Commercial Domain"
    elif email.endswith(".edu"):
        domain_type = "Educational Domain"
    else:
        domain_type = "Other Domain"

    return username, domain_name, domain_type


def decode_message(msg):
    raw_words = re.findall(r"[a-zA-Z0-9]+", msg)
    text_words = [w for w in raw_words if not w.isdigit()]

    word1 = text_words[0][::-1].capitalize()
    word2 = text_words[1]

    vowel_map = {"1": "E", "O": "U", "E": "A", "U": "O"}
    word2_clean = "".join(vowel_map.get(ch, ch) for ch in word2)

    return f"{word1} {word2_clean}"


email_info = process_email("Amit_ml@gmail.edu")
print(email_info)

print(decode_message("###!!@mocleW EPGTO!!!6789"))
print(decode_message("&&&$gnirts PLIO!!@1234"))
print(decode_message("##$$$@!yalpstcejorp EPUVT****9887"))