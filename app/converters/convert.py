import pandas as pd

def convert_csv_to_json(input_path: str, output_path: str):
    df = pd.read_csv(
        input_path,
        encoding="latin1",      # ✔️ soporta tildes, ñ, Excel
        sep=",",
        on_bad_lines="skip"     # ✔️ ignora filas rotas
    )

    df.to_json(
        output_path,
        orient="records",
        indent=4,
        force_ascii=False       # ✔️ mantiene caracteres reales
    )