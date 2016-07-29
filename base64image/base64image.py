"""Tools for working with base64-encoded
images for data-src in HTML.

"""

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

import base64
import imghdr
from io import BytesIO

from PIL import Image


class ImageFormats:
    """These map to both imghdr results
    and the value for data uri.

    """

    PNG = "png"
    JPEG = "jpeg"
    GIF = "gif"


class Base64Image(object):

    def __init__(self, image_string):
        """

        Arguments:
            image_string (str): Generally the result of
                .read()'ing something in binary mode.

        """

        self.image_string = image_string
        self.base64_image_string = base64.b64encode(image_string)
        self.image_format = self._detect_image_format(image_string)

    def __str__(self):
        """Just what you need for img src.

        Returns:
            str: data URI for this base64 image.

        """

        data_uri = ("data:image/%s;base64,%s"
                    % (self.image_format, self.base64_image_string))
        return data_uri

    @staticmethod
    def _detect_image_format(image_string):
        """

        Arguments:
            image_string (str): A non-encoded read()
                result (string).

        Returns:
            ImageFormats constant.

        Raises:
            NotImplementedError: If the type detected
                is not supported/in the ImageFormats
                enumeration.

        Note:
            Instead of directly returning the result,
            we return an attribute lookup from ImageFormats,
            which is probably the same exact value, but
            lets us control what's NotImplementedError.

        """

        imghdr_result = imghdr.what('', h=image_string)

        try:
            image_format = getattr(ImageFormats, imghdr_result.upper())
        except AttributeError as e:
            raise NotImplementedError("No support for %s" % e.message)

        if image_format is None:
            raise ValueError("Invalid image provided.")

        return image_format

    @classmethod
    def from_base64_image_string(cls, base64_image_string):
        """Useful for both create a Base64Image from a base64
        image string AND validating that a provided string is
        indeed a a true base64 image (or ValueError is raised).

        Arguments:
            base64_image_string: This string will be checked
                if it is a valid image once decoded from b64.

        Raises:
            ValueError: If provided string is not a
                proper base64 encoded image string.

        Returns:
            Base64Image

        """

        image_string = base64.b64decode(base64_image_string)
        self._detect_image_format(image_string)
        return cls(image_string)

    @classmethod
    def from_file(cls, file_path):

        with open(file_path, "rb") as image_file:
            image_string = image_file.read()

        return cls(image_string)

    @classmethod
    def from_uri(cls, uri):
        file_data = urllib2.urlopen(uri)
        image_string = file_data.read()
        return cls(image_string)

    def to_file(self, file_name):
        """

        Arguments:
            file_name (str): File name to save
                this base64 image to.

        Returns:
            None

        """

        pil_image = self.get_pil_image()
        pil_image.save(file_name, self.image_format.upper())

    def get_pil_image(self):
        return Image.open(BytesIO(self.image_string))
