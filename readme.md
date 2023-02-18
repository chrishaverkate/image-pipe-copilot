# Overview
I wanted a basic project to experiment with GitHub Copilot.

Most of the code written was generated, however I needed to fix and
coerce several parts. 

I also found it very distracting to have Copilot on while typing this readme.
It had *NO* idea what I was trying to say.

# Usage
## Install Requirements
`pip install -r requirements.txt`

## Running
The Image Pipe can be run using `ip.py`

### Examples
1. Rotate 30 degrees and scale up 2x  
`python -m src.ip -i tests/images/swatches.png -o tests/images_out/playing.png  -r 30 -s 2`
2. Rotate and expand the canvas  
`python -m src.ip -i tests/images/swatches.png -o tests/images_out/playing.png  -r 45 -e`
3. Rotate, translate up and left, and add box blue
4. `python -m src.ip -i tests/images/swatches.png -o tests/images_out/playing.png  -r 45 -x 100 -y 50 -b 1`
