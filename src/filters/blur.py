from PIL import ImageFilter


class BlurFilter:
    def __init__(self, image):
        self._image = image

    def box_blur(self, radius):
        """Box blur filter.
        Args: image (PIL.Image):
        Image to be filtered.
        radius (int): Radius of the box blur.
        Returns: PIL.Image: Filtered image.
        """
        return self._image.filter(ImageFilter.BoxBlur(radius))
