import random
def is_valid_pin(pin: str) -> bool:
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return False

    if "0123456789".find(pin) != -1:
        return False

    return True

def generate_pin() -> str:
    while True:
        pin = str(random.randint(0, 9999)).zfill(4)
        if is_valid_pin(pin):
            return pin

if __name__ == "__main__":
    new_pin = generate_pin()
    print(f"Сгенерированный ПИН-код: {new_pin}")
