def int_input(ledtext):
   while True:
    try:
        inmatning = int(input(ledtext))
        return inmatning
    except ValueError:
        print("Det där var inget giltigt heltal. Försök igen.")


def float_input(ledtext):
    while True:
        try:
            inmatning = float(input(ledtext))
            return inmatning
        except ValueError:
            print("Det där var inget giltigt floattal. Försök igen.")
