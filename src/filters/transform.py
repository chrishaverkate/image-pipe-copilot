from PIL import Image


class Transform():
    def translate(self, image, x, y):
        """Translate filter.
        Args: x (int): X-axis translation.
        y (int): Y-axis translation.
        Returns: PIL.Image: Filtered image.
        """
        return image.transform(image.size, Image.AFFINE, (1, 0, x, 0, 1, y))

    def scale(self, image, percent):
        """Scale filter.
        Args: percent (float): Percent to scale image.
        Returns: PIL.Image: Filtered image.
        """
        size = (int(image.size[0] * percent), int(image.size[1] * percent))
        return image.resize(size, resample=Image.BICUBIC)
