"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import lcm_generation_style as shared_lcm_generation_style
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PerformAlchemyUpscaleLCMRequestBody:
    r"""Query parameters can also be provided in the request body as a JSON object"""
    UNSET='__SPEAKEASY_UNSET__'
    image_data_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageDataUrl') }})
    r"""Image data used to generate image. In base64 format. Prefix: `data:image/jpeg;base64,`"""
    prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt') }})
    r"""The prompt used to generate images"""
    guidance: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('guidance'), 'exclude': lambda f: f is PerformAlchemyUpscaleLCMRequestBody.UNSET }})
    r"""How strongly the generation should reflect the prompt. Must be a float between 0.5 and 20."""
    height: Optional[int] = dataclasses.field(default=512, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('height'), 'exclude': lambda f: f is PerformAlchemyUpscaleLCMRequestBody.UNSET }})
    r"""The output width of the image. Must be 512, 640 or 1024."""
    refine_creative: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refineCreative'), 'exclude': lambda f: f is PerformAlchemyUpscaleLCMRequestBody.UNSET }})
    r"""Refine creative"""
    refine_strength: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refineStrength'), 'exclude': lambda f: f is PerformAlchemyUpscaleLCMRequestBody.UNSET }})
    r"""Must be a float between 0.5 and 0.9."""
    request_timestamp: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestTimestamp'), 'exclude': lambda f: f is None }})
    seed: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is PerformAlchemyUpscaleLCMRequestBody.UNSET }})
    steps: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('steps'), 'exclude': lambda f: f is PerformAlchemyUpscaleLCMRequestBody.UNSET }})
    r"""The number of steps to use for the generation. Must be between 4 and 16."""
    strength: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('strength'), 'exclude': lambda f: f is PerformAlchemyUpscaleLCMRequestBody.UNSET }})
    r"""Creativity strength of generation. Higher strength will deviate more from the original image supplied in imageDataUrl. Must be a float between 0.1 and 1."""
    style: Optional[shared_lcm_generation_style.LcmGenerationStyle] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('style'), 'exclude': lambda f: f is PerformAlchemyUpscaleLCMRequestBody.UNSET }})
    r"""The style to generate LCM images with."""
    width: Optional[int] = dataclasses.field(default=512, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('width'), 'exclude': lambda f: f is PerformAlchemyUpscaleLCMRequestBody.UNSET }})
    r"""The output width of the image. Must be 512, 640 or 1024."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PerformAlchemyUpscaleLCMLCMGenerationOutput:
    UNSET='__SPEAKEASY_UNSET__'
    api_credit_cost: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiCreditCost'), 'exclude': lambda f: f is PerformAlchemyUpscaleLCMLCMGenerationOutput.UNSET }})
    r"""API credits cost, available for Production API users."""
    generated_image_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generatedImageId'), 'exclude': lambda f: f is None }})
    generation_id: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generationId'), 'exclude': lambda f: f is None }})
    image_data_url: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageDataUrl'), 'exclude': lambda f: f is None }})
    request_timestamp: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestTimestamp'), 'exclude': lambda f: f is None }})
    variation_id: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('variationId'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PerformAlchemyUpscaleLCMResponseBody:
    r"""Responses for POST /lcm-upscale"""
    UNSET='__SPEAKEASY_UNSET__'
    lcm_generation_job: Optional[PerformAlchemyUpscaleLCMLCMGenerationOutput] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lcmGenerationJob'), 'exclude': lambda f: f is PerformAlchemyUpscaleLCMResponseBody.UNSET }})
    



@dataclasses.dataclass
class PerformAlchemyUpscaleLCMResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[PerformAlchemyUpscaleLCMResponseBody] = dataclasses.field(default=None)
    r"""Responses for POST /lcm-upscale"""
    

