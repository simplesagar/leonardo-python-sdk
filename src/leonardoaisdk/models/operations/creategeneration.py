"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import controlnet_type as shared_controlnet_type
from ..shared import sd_generation_schedulers as shared_sd_generation_schedulers
from ..shared import sd_generation_style as shared_sd_generation_style
from ..shared import sd_versions as shared_sd_versions
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateGenerationRequestBody:
    r"""Query parameters to be provided in the request body as a JSON object"""
    alchemy: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alchemy'), 'exclude': lambda f: f is None }})
    r"""Enable to use Alchemy."""
    contrast_ratio: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contrastRatio'), 'exclude': lambda f: f is None }})
    r"""Contrast Ratio to use with Alchemy."""
    control_net: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('controlNet'), 'exclude': lambda f: f is None }})
    r"""Enable to use ControlNet. Requires an init image to be provided. Requires a model based on SD v1.5"""
    control_net_type: Optional[shared_controlnet_type.ControlnetType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('controlNetType'), 'exclude': lambda f: f is None }})
    r"""The type of ControlNet to use."""
    expanded_domain: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandedDomain'), 'exclude': lambda f: f is None }})
    r"""Enable to use the Expanded Domain feature of Alchemy."""
    guidance_scale: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('guidance_scale'), 'exclude': lambda f: f is None }})
    r"""How strongly the generation should reflect the prompt. 7 is recommended. Must be between 1 and 20."""
    height: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('height'), 'exclude': lambda f: f is None }})
    r"""The height of the images. Must be between 32 and 1024 and be a multiple of 8."""
    high_contrast: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('highContrast'), 'exclude': lambda f: f is None }})
    r"""Enable to use the High Contrast feature of Prompt Magic."""
    high_resolution: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('highResolution'), 'exclude': lambda f: f is None }})
    r"""Enable to use the High Resolution feature of Prompt Magic."""
    image_prompts: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imagePrompts'), 'exclude': lambda f: f is None }})
    image_prompt_weight: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imagePromptWeight'), 'exclude': lambda f: f is None }})
    init_generation_image_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('init_generation_image_id'), 'exclude': lambda f: f is None }})
    r"""The ID of an existing image to use in image2image."""
    init_image_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('init_image_id'), 'exclude': lambda f: f is None }})
    r"""The ID of an Init Image to use in image2image."""
    init_strength: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('init_strength'), 'exclude': lambda f: f is None }})
    r"""How strongly the generated images should reflect the original image in image2image. Must be a float between 0.1 and 0.9."""
    model_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId'), 'exclude': lambda f: f is None }})
    r"""The model ID used for the image generation. If not provided uses sd_version to determine the version of Stable Diffusion to use.

    _Leonardo Creative_: 6bef9f1b-29cb-40c7-b9df-32b51c1f67d3
    _Leonardo Select_: cd2b2a15-9760-4174-a5ff-4d2925057376
    _Leonardo Signature_: 291be633-cb24-434f-898f-e662799936ad
    """
    negative_prompt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('negative_prompt'), 'exclude': lambda f: f is None }})
    r"""The negative prompt used for the image generation"""
    nsfw: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nsfw'), 'exclude': lambda f: f is None }})
    r"""Not Safe For Work Flag."""
    num_images: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_images'), 'exclude': lambda f: f is None }})
    r"""The number of images to generate. Must be between 1 and 8. If either width or height is over 768, must be between 1 and 4."""
    num_inference_steps: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_inference_steps'), 'exclude': lambda f: f is None }})
    r"""The number of inference steps to use for the generation. Must be between 30 and 60."""
    photo_real: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('photoReal'), 'exclude': lambda f: f is None }})
    r"""Enable the photoReal feature"""
    preset_style: Optional[shared_sd_generation_style.SdGenerationStyle] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('presetStyle'), 'exclude': lambda f: f is None }})
    r"""The style to generate images with."""
    prompt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt'), 'exclude': lambda f: f is None }})
    r"""The prompt used to generate images"""
    prompt_magic: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptMagic'), 'exclude': lambda f: f is None }})
    r"""Enable to use Prompt Magic."""
    prompt_magic_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptMagicVersion'), 'exclude': lambda f: f is None }})
    r"""Prompt magic version v2 or v3, for use when promptMagic: true"""
    public: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public'), 'exclude': lambda f: f is None }})
    r"""Whether the generated images should show in the community feed."""
    scheduler: Optional[shared_sd_generation_schedulers.SdGenerationSchedulers] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduler'), 'exclude': lambda f: f is None }})
    r"""The scheduler to generate images with. Defaults to EULER_DISCRETE if not specified."""
    sd_version: Optional[shared_sd_versions.SdVersions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sd_version'), 'exclude': lambda f: f is None }})
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5."""
    seed: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is None }})
    tiling: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiling'), 'exclude': lambda f: f is None }})
    r"""Whether the generated images should tile on all axis."""
    unzoom: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unzoom'), 'exclude': lambda f: f is None }})
    r"""Whether the generated images should be unzoomed."""
    unzoom_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unzoomAmount'), 'exclude': lambda f: f is None }})
    r"""How much the image should be unzoomed."""
    upscale_ratio: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upscaleRatio'), 'exclude': lambda f: f is None }})
    r"""How much the image should be upscaled. (Enterprise Only)"""
    weighting: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weighting'), 'exclude': lambda f: f is None }})
    r"""How much weighting to use for generation."""
    width: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('width'), 'exclude': lambda f: f is None }})
    r"""The width of the images. Must be between 32 and 1024 and be a multiple of 8."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateGeneration200ApplicationJSONSDGenerationOutput:
    generation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generationId'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateGeneration200ApplicationJSON:
    r"""Responses for POST /generations"""
    sd_generation_job: Optional[CreateGeneration200ApplicationJSONSDGenerationOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sdGenerationJob'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class CreateGenerationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_generation_200_application_json_object: Optional[CreateGeneration200ApplicationJSON] = dataclasses.field(default=None)
    r"""Responses for POST /generations"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

