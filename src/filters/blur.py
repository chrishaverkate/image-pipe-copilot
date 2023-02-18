from PIL import ImageFilter


class BlurFilter:
    def box_blur(self, image, radius):
        """Box blur filter.
        Args: image (PIL.Image):
        Image to be filtered.
        radius (int): Radius of the box blur.
        Returns: PIL.Image: Filtered image.
        """
        return image.filter(ImageFilter.BoxBlur(radius))

    def gaussian_blur(self, image, radius):
        """Gaussian blur filter.
        Args: image (PIL.Image):
        Image to be filtered.
        radius (int): Radius of the gaussian blur.
        Returns: PIL.Image: Filtered image.
        """
        return image.filter(ImageFilter.GaussianBlur(radius))
