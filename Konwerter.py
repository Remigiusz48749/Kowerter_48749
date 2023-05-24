import sys
import json
import yaml


def xml_to_json(xml_path, json_path):
    try:
        # krok6
        data = 0  # zła kolejność tasków dla mojego rozwiązania...
        # krok3
        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)
    except:
        print("Coś poszło nie tak. Twój plik może być uszkodzony")


def json_to_xml(json_path, xml_path):
    try:
        with open(json_path, "r") as file:
            data = json.load(file)
        # nie zakończone
    except:
        print("Coś poszło nie tak. Twój plik może być uszkodzony")


def json_to_yaml(json_path, yaml_path):
    try:
        with open(json_path, "r") as file:
            data = json.load(file)
        #nie zakończone
    except:
        print("Coś poszło nie tak. Twój plik może być uszkodzony")


def yaml_to_json(yaml_path, json_path):
    try:
        #krok4
        with open(yaml_path, "r") as file:
            data = yaml.safe_load(file)
        #krok3
        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)
    except:
        print("Coś poszło nie tak. Twój plik może być uszkodzony")


def main():
    if len(sys.argv) != 3:
        print("Sposób użycia: program.exe pathFile1.x pathFile2.y")
        print("gdzie x i y to jeden z formatów .xml, .json i .yml (.yaml)")
        return

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    if in_path.endswith(".xml") and out_path.endswith(".json"):
        xml_to_json(in_path, out_path)
        print("Konwersja zakończona pomyślnie.")
    elif in_path.endswith(".json") and out_path.endswith(".xml"):
        json_to_xml(in_path, out_path)
        print("Konwersja zakończona pomyślnie.")
    elif in_path.endswith(".json") and out_path.endswith(".yml"):
        json_to_yaml(in_path, out_path)
        print("Konwersja zakończona pomyślnie.")
    elif in_path.endswith(".yml") and out_path.endswith(".json"):
        yaml_to_json(in_path, out_path)
        print("Konwersja zakończona pomyślnie.")
    else:
        print("""Nieobsługiwany format pliku wejściowego i/lub wyjściowego.
        Obsługiwane formaty to: .xml, .json i .yml (.yaml).
        Upewnij się, że podałeś poprawne rozszerzenia plików i spróbuj ponownie.
        Przykładowe wywołanie programu:
        Konwerter.exe plik_wejsciowy.xml plik_wyjsciowy.json
        """)


if __name__ == "__main__":
    main()