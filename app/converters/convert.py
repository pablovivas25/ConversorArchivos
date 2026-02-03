import pandas as pd

def convert_csv_to_json(input_path: str, output_path: str):
    df = pd.read_csv(
        input_path,
        encoding="latin1",      
        sep=",",
        on_bad_lines="skip"    
    )

    df.to_json(
        output_path,
        orient="records",
        indent=4,
        force_ascii=False      
    )


def convert_json_to_csv(input_path: str, output_path: str) -> None:
   
    df = pd.read_json(input_path)

    df.to_csv(output_path, index=False)


def convert_csv_to_xlsx(input_path: str, output_path: str) -> None:
    try:
        df = pd.read_csv(
            input_path,
            encoding="utf-8",
            sep=",",
            on_bad_lines="skip"
        )
    except UnicodeDecodeError:
        df = pd.read_csv(
            input_path,
            encoding="latin1",
            sep=",",
            on_bad_lines="skip"
        )

    df.to_excel(output_path, index=False)
