import pytesseract
from PIL import Image
import schedule
import time

def perform_ocr(image_path, output_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)

    with open(output_path, 'w') as file:
        file.write(text)

    print("OCR completed. Text saved to", output_path)

def run_ocr_scheduler():
    image_path = "ex.tiff"
    output_path = "answer.txt"

    perform_ocr(image_path, output_path)

# Initial OCR execution
run_ocr_scheduler()

# Schedule OCR every 6 hours
schedule.every(6).hours.do(run_ocr_scheduler)

# Keep the script running to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
