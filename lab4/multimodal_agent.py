
import os
import subprocess

import av
import numpy as np
import torch
from PIL import Image
from scipy.io.wavfile import write
from transformers import (
    BlipProcessor,
    BlipForQuestionAnswering,
    BlipForConditionalGeneration,
    VitsModel,
    AutoTokenizer,
    pipeline,
)
# 1. tuhuurumj

device = "cpu"  # Intel Mac дээр CPU ашиглана
device_index = -1

print("Ашиглаж буй төхөөрөмж:", device)

# 2. zagwar achaallah

VQA_MODEL = "Salesforce/blip-vqa-base"
CAPTION_MODEL = "Salesforce/blip-image-captioning-base"
WHISPER_MODEL = "openai/whisper-tiny"
TTS_MODEL = "facebook/mms-tts-eng"

print("\n[1/4] Зураг асуулт-хариултын загвар...")
vqa_processor = BlipProcessor.from_pretrained(VQA_MODEL)
vqa_model = BlipForQuestionAnswering.from_pretrained(VQA_MODEL)
vqa_model.eval()

print("\n[2/4] Зураг тайлбарлах загвар...")
caption_processor = BlipProcessor.from_pretrained(CAPTION_MODEL)
caption_model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base",
    use_safetensors=True
)
caption_model.eval()

print("\n[3/4] Англи дуу таних загвар...")
speech_recognizer = pipeline(
    "automatic-speech-recognition",
    model=WHISPER_MODEL,
    device=device_index,
)

print("\n[4/4] Англи дуу хоолойн загвар...")
tts_tokenizer = AutoTokenizer.from_pretrained(TTS_MODEL)
tts_model = VitsModel.from_pretrained(TTS_MODEL)
tts_model.eval()

print("\nБүх загвар ачаалагдлаа.")

# 3. zurag tailbarlah


def describe_image(image_path):
    try:
        if not os.path.isfile(image_path):
            return "Error: Image file not found."

        with Image.open(image_path) as img:
            image = img.convert("RGB")

        inputs = caption_processor(
            image,
            return_tensors="pt"
        )

        with torch.no_grad():
            output = caption_model.generate(
                **inputs,
                max_new_tokens=60,
                num_beams=4
            )

        description = caption_processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return description.strip()

    except Exception as error:
        return f"Image description error: {error}"

# 4. zurgiin asuultad hariulah

def answer_image_question(image_path, question):
    try:
        if not os.path.isfile(image_path):
            return "Error: Image file not found."

        with Image.open(image_path) as img:
            image = img.convert("RGB")

        inputs = vqa_processor(
            image,
            question,
            return_tensors="pt"
        )

        with torch.no_grad():
            output = vqa_model.generate(
                **inputs,
                max_new_tokens=40
            )

        answer = vqa_processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return answer.strip()

    except Exception as error:
        return f"Image question error: {error}"

# 5. asuult ni tailbarlah asuult mun eseh

def is_description_request(question):
    text = question.lower()

    keywords = [
        "describe",
        "description",
        "explain the image",
        "explain this image",
        "what is in this image",
        "what can you see",
        "tell me about this picture",
        "зураг тайлбар",
        "зургийг дүрсэл",
        "дүрсэлж",
        "тайлбарлана уу",
        "zurag",
        "tailbar",
        "dursel",
    ]

    return any(word in text for word in keywords)


def multimodal_agent(image_path, question=None, audio_path=None):
    if audio_path:
        question = transcribe_audio(audio_path)

        if question.startswith("Error:"):
            return question

        print("\nRecognized question:", question)

    if not question or not question.strip():
        return "Error: Please enter a question."

    # zurag tailbarlah huselt bol caption zagwar ashiglan
    if is_description_request(question):
        return describe_image(image_path)

    # busad asuultig zagwart butsaana
    return answer_image_question(image_path, question)

# 6. audiog 16 kHz mono bolgon unshih (FFmpeg хэрэглэхгүй)

def load_audio_without_ffmpeg(audio_path):
    chunks = []

    with av.open(audio_path) as container:
        if not container.streams.audio:
            raise ValueError("No audio stream found.")

        stream = container.streams.audio[0]

        resampler = av.AudioResampler(
            format="fltp",
            layout="mono",
            rate=16000
        )

        for frame in container.decode(stream):
            converted_frames = resampler.resample(frame)

            if converted_frames:
                for converted in converted_frames:
                    chunks.append(
                        converted.to_ndarray().reshape(-1)
                    )

        remaining = resampler.resample(None)

        if remaining:
            for converted in remaining:
                chunks.append(
                    converted.to_ndarray().reshape(-1)
                )

    if not chunks:
        raise ValueError("No audio data could be read.")

    return np.concatenate(chunks).astype(np.float32)


# ==================================================
# 7. duunaas asuult tanih
# ==================================================

def transcribe_audio(audio_path):
    try:
        if not os.path.isfile(audio_path):
            return "Error: Audio file not found."

        audio = load_audio_without_ffmpeg(audio_path)

        result = speech_recognizer({
            "raw": audio,
            "sampling_rate": 16000
        })

        return result["text"].strip()

    except Exception as error:
        return f"Error: Audio transcription failed: {error}"


# 8. angli heleer textiig unshih
def speak_english(text):
    try:
        if not text or not text.strip():
            return

        # bogino uguulber tohiromjtoi
        text = text.strip()

        inputs = tts_tokenizer(
            text,
            return_tensors="pt"
        )

        with torch.no_grad():
            waveform = tts_model(**inputs).waveform[0]

        audio = waveform.cpu().numpy().astype(np.float32)

        output_path = os.path.abspath("agent_explanation.wav")

        write(
            output_path,
            tts_model.config.sampling_rate,
            audio
        )

        print("Speech file saved:", output_path)

        # macOS-iin suurilsan audio togluulagch
        subprocess.run(
            ["afplay", output_path],
            check=False
        )

    except Exception as error:
        print("Speech generation error:", error)


# 9. undsen programm

if __name__ == "__main__":
    print("\n=== MULTIMODAL AGENT ===")
    print("1 - Text + Image")
    print("2 - Speech + Image")

    mode = input("Choose mode (1/2): ").strip()

    image_path = input(
        "Enter the full image path: "
    ).strip().strip("'\"")

    if not os.path.isfile(image_path):
        answer = "Error: Image file not found."

    elif mode == "1":
        question = input(
            "Enter your question in English: "
        ).strip()

        answer = multimodal_agent(
            image_path,
            question=question
        )

    elif mode == "2":
        audio_path = input(
            "Enter the full audio file path: "
        ).strip().strip("'\"")

        answer = multimodal_agent(
            image_path,
            audio_path=audio_path
        )

    else:
        answer = "Error: Please choose 1 or 2."

    print("\nAI answer:", answer)

    if answer and not answer.startswith("Error:"):
        speak_english(answer)
        
# eregtei hunii zurag
# /Users/bq/Desktop/Screen Shot 2026-09-25 at 18.11.33.png 

# emegtei hunii zurag 
# /Users/bq/Downloads/IMG_6430.jpeg

# zurag yu haragdaj bn we voice helber
# /Users/bq/Downloads/B. Dorj Street 8.m4a 

# Please describe and explain the image.
# /Users/bq/Downloads/B. Dorj Street 15.m4a 
