from utils.text_extractor import text_extractor

async def get_text (file=None,text=None):
    if file:
        file_bytes = await file.read()
        return text_extractor(
            file_bytes,
            file.filename,
            # file.content_type
        )

    return text 