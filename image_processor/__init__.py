from PIL import Image, ImageFilter

def resize_image(image_path, output_path, size):
    """Redimensiona a imagem para o tamanho especificado."""
    with Image.open(image_path) as img:
        img = img.resize(size)
        img.save(output_path)
        print(f"Imagem redimensionada salva em {output_path}")

def convert_to_grayscale(image_path, output_path):
    """Converte a imagem para escala de cinza."""
    with Image.open(image_path) as img:
        img = img.convert("L")
        img.save(output_path)
        print(f"Imagem convertida para escala de cinza salva em {output_path}")

def apply_blur_filter(image_path, output_path, radius=5):
    """Aplica um filtro de desfoque à imagem."""
    with Image.open(image_path) as img:
        img = img.filter(ImageFilter.GaussianBlur(radius))
        img.save(output_path)
        print(f"Imagem com filtro de desfoque salva em {output_path}")
      from .processing import resize_image, convert_to_grayscale, apply_blur_filter

__all__ = ['resize_image', 'convert_to_grayscale', 'apply_blur_filter']

