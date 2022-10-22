import base64
import binascii

import pydantic


class TemplateUpload(pydantic.BaseModel):
    templates: list[str]

    @pydantic.validator("templates")
    @classmethod
    def templates_are_valid_base64(cls, value: list[str]):
        for index, image in enumerate(value):
            try:
                base64.b64decode(image, validate=True)
            except binascii.Error as error:
                raise ValueError(
                    f"image at index {index} is not a valid base64 string; {error}"
                ) from error

        return value
