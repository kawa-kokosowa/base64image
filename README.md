# base64image

[![PyPi](https://img.shields.io/pypi/v/base64image.svg)](https://pypi.python.org/pypi/base64image)

Base64-encoded images for HTML data URIs.

`pip install base64image`

## Examples

```
from base64image import Base64Image
b64_image = Base64Image.from_file("wowo.png")
image_element = '<img src="%s">' % base64_image

base64_image = Base64Image.from_base64_image_string("...")
pil_image = base64_image.get_pil_image()

base64_image = Base64Image.from_url("http://example.org/haha.jpg")
base64_image.to_file("haha.jpg")

base64_image.image_format
base64_image.base64_image_string
base64_image.image_string
``
