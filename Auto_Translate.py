# Practise
myDict = {
    "Fellowship": "شرکت",
    "Blessings": "رحمت",
    "Ham": "بستی",
    "Disciplines": "مضامین",
    "CMB": "مجھے واپس کال کرو",
    "Unbinding": "اکڑ باز",
    "Tragic": "المیہ",
    "Instroke": "اندرونی چوٹ",
    "Scathe": "اذیت",
    "Squirm": "بل کھانا",
    "Tying": "باندھنا",
    "Undesigning": "بے ریا",
    "Complainant": "فریادی",
    "Numerator": "گنتی کرنے والا",
    "Surmising": "گمان",
    "Geometries": "ہندسہ",
    "ILBL8": "میں تھوڑا دیر سے آئوں گا",
    "Answerable": "جواب دہ",
    "Penance": "کفارہ",
}
def translate_dictionary(var):
    print("Welcome to Arsdale Dictionary")
    print("Options are ", var.keys())
    a = input("Enter a English work:\n")
    while True:
        if a != myDict:
            print("Please write word which will be show on options")
            a = input("Enter the work you want to translate:  ")
            print(var.get(a))
    else:
        print(var.get())

print(translate_dictionary(myDict))