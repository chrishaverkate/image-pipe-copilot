
class RotateFilter():

    def rotate(self, image, angle, expand=False):
        """Rotate filter.
        Args: image (PIL.Image):
        Image to be filtered.
        angle (int): Angle of the rotation.
        expand (bool): Expand image to fit rotated image.
        Returns: PIL.Image: Filtered image.
        """
        return image.rotate(angle, expand=expand)