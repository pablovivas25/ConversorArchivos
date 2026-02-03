import os
from app.converters.convert import convert_csv_to_json,convert_json_to_csv,convert_csv_to_xlsx

class ConversionService:
    
    @staticmethod
    def convert(input_path: str, input_ext: str, target_format: str) -> str:
        base_path = os.path.splitext(input_path)[0]

        if input_ext == "csv" and target_format == "json":
            output_path = f"{base_path}.json"
            convert_csv_to_json(input_path, output_path)
        elif input_ext == "json" and target_format == "csv":
            output_path = f"{base_path}.csv"
            convert_json_to_csv(input_path, output_path)
        elif input_ext=="csv" and target_format=="xlsx":
            output_path = input_path.rsplit(".", 1)[0] + f".{target_format}"
            convert_csv_to_xlsx(input_path, output_path)


        return output_path