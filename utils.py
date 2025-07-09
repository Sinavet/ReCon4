SUPPORTED_EXTS = ('.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tiff', '.heic', '.heif')
MAX_SIZE_MB = 400
MAX_SIZE_BYTES = MAX_SIZE_MB * 1024 * 1024

def filter_large_files(uploaded_files, st=None):
    filtered = []
    for f in uploaded_files:
        f.seek(0, 2)
        size = f.tell()
        f.seek(0)
        if size > MAX_SIZE_BYTES:
            if st:
                st.error(f"Файл {f.name} превышает {MAX_SIZE_MB} МБ и не будет обработан.")
        else:
            filtered.append(f)
    return filtered 