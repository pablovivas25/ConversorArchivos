from fastapi import FastAPI, Request,UploadFile,File,Form,HTTPException
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.conversion_rules import CONVERSION_RULES
from app.services.conversion_service import ConversionService
from app.utils.file_utils import save_upload_file

app = FastAPI(title="File Converter Web")

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/formats/{input_format}")
def get_available_formats(input_format: str):
    input_format = input_format.lower()

    if input_format not in CONVERSION_RULES:
        return {"input": input_format, "outputs": []}

    return {
        "input": input_format,
        "outputs": CONVERSION_RULES[input_format]
    }
@app.post("/convert")
async def convertir_file(
 file: UploadFile = File(...),
    target_format: str = Form(...)
):
    input_ext = file.filename.split(".")[-1].lower()

    input_path = save_upload_file(file)

    output_path = ConversionService.convert(
        input_path=input_path,
        input_ext=input_ext,
        target_format=target_format
    )

    return FileResponse(
        output_path,
        filename=f"archivo_convertido.{target_format}",
        media_type="application/octet-stream"
    )

