
import torch
from PIL import Image
from transformers import (
    VisionEncoderDecoderModel,
    ViTImageProcessor,
    AutoTokenizer
)

MODEL_NAME = "nlpconnect/vit-gpt2-image-captioning"

# Загвар, процессор, tokenizer ачаалах
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Ашиглаж буй төхөөрөмж:", device)

model = VisionEncoderDecoderModel.from_pretrained(MODEL_NAME)
processor = ViTImageProcessor.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model.to(device)
model.eval()


def describe_image(image_path):
    try:
        image = Image.open(image_path).convert("RGB")

        inputs = processor(
            images=image,
            return_tensors="pt"
        )

        pixel_values = inputs["pixel_values"].to(device)

        with torch.no_grad():
            output_ids = model.generate(
                pixel_values,
                max_length=32,
                num_beams=4
            )

        caption = tokenizer.decode(
            output_ids[0],
            skip_special_tokens=True
        )

        return caption

    except (OSError, ValueError) as error:
        return f"Зураг боловсруулахад алдаа гарлаа: {error}"


# Туршилт
image_path = input("Зургийн файлын замыг оруулна уу: ")
result = describe_image(image_path)

print("Зургийн тайлбар:", result)
