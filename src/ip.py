import argparse
from sys import argv

from PIL import Image

from src.filters.blur import BlurFilter
from src.filters.rotate import RotateFilter
from src.filters.transform import Transform


def parse_args(raw_args=None):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Image Pipeline for basic image processing.',
                                     usage='Set an input and output image, and any combination of filters '
                                          'to apply to the image.'
                                          'For example, to rotate an image by 90 degrees, expand the '
                                          'image to fit the rotated image,'
                                          'and then apply a box blur with a radius of 5, you would run '
                                          'the following command:'
                                          ' python ip.py -r 90 -e True -b 5 -i input.png -o output.png')

    parser.add_argument('-b', '--blur-box', type=int, help='Blur image by radius.')
    parser.add_argument('-e', '--expand', action='store_true', help='Expand image to fit rotated image.')
    parser.add_argument('-g', '--blur-gaussian', type=int, help='Blur image by radius.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input image.')
    parser.add_argument('-o', '--output', type=str, default='output.png', help='Output image.')
    parser.add_argument('-r', '--rotate', type=int, help='Rotate image by angle.')
    parser.add_argument('-x', '--x-trans', type=int, default=0, help='Translate image by x-axis.')
    parser.add_argument('-y', '--y-trans', type=int, default=0, help='Translate image by y-axis.')
    parser.add_argument('-s', '--scale', type=float, help='Scale image by x and y.')
    return parser.parse_args(raw_args)


if __name__ == '__main__':
    args = parse_args(argv[1:])

    with Image.open(args.input) as image:
        if args.rotate:
            image = RotateFilter().rotate(image, args.rotate, args.expand)
        if args.blur_box:
            image = BlurFilter().box_blur(image, args.blur_box)
        if args.blur_gaussian:
            image = BlurFilter().gaussian_blur(image, args.blur_gaussian)
        if args.x_trans or args.y_trans:
            image = Transform().translate(image, args.x_trans, args.y_trans)
        if args.scale:
            image = Transform().scale(image, args.scale)

        image.save(args.output)
