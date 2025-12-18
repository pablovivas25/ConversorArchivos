import os
from app.converters.convert import convert_csv_to_json

class ConversionService:
    
    @staticmethod
    def convert(input_path: str, input_ext: str, target_format: str) -> str:
        base_path = os.path.splitext(input_path)[0]

        if input_ext == "csv" and target_format == "json":
            output_path = f"{base_path}.json"
            convert_csv_to_json(input_path, output_path)

        return output_path