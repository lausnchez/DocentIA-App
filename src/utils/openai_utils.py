import os
import fitz # pymupdf

from dotenv import load_dotenv

#load environment variables
load_dotenv()

# Config variables
OPENAI_APIKEY = os.getenv("OPENAI_APIKEY")


