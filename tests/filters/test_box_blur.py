from src.filters.blur import BlurFilter
from PIL import Image, ImageFilter


def test_box_blur():
    """Test box blur filter."""
    image = Image.open('tests/images/swatches.png')
    result = BlurFilter(image).box_blur(5)
    assert image.filter(ImageFilter.BoxBlur(5)) == result
    # result.save('tests/images_out/swatches_box_blur.png')
