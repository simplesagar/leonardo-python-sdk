"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import job_status as shared_job_status
from ...models.shared import sd_generation_schedulers as shared_sd_generation_schedulers
from ...models.shared import sd_generation_style as shared_sd_generation_style
from ...models.shared import sd_versions as shared_sd_versions
from ...models.shared import variation_type as shared_variation_type
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import List, Optional


@dataclasses.dataclass
class GetGenerationByIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The ID of the generation to return."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetGenerationByIDGeneratedImageVariationGeneric:
    r"""columns and relationships of \\"generated_image_variation_generic\\" """
    UNSET='__SPEAKEASY_UNSET__'
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is GetGenerationByIDGeneratedImageVariationGeneric.UNSET }})
    status: Optional[shared_job_status.JobStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the current task."""
    transform_type: Optional[shared_variation_type.VariationType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transformType'), 'exclude': lambda f: f is None }})
    r"""The type of variation."""
    url: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is GetGenerationByIDGeneratedImageVariationGeneric.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GeneratedImages:
    r"""columns and relationships of \\"generated_images\\" """
    UNSET='__SPEAKEASY_UNSET__'
    fantasy_avatar: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fantasyAvatar'), 'exclude': lambda f: f is GeneratedImages.UNSET }})
    r"""If fantasyAvatar feature was used."""
    generated_image_variation_generics: Optional[List[GetGenerationByIDGeneratedImageVariationGeneric]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generated_image_variation_generics'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is GeneratedImages.UNSET }})
    image_to_video: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageToVideo'), 'exclude': lambda f: f is GeneratedImages.UNSET }})
    r"""If it is an image to video generation."""
    like_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('likeCount'), 'exclude': lambda f: f is None }})
    motion: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('motion'), 'exclude': lambda f: f is GeneratedImages.UNSET }})
    r"""If generation is of motion type."""
    motion_mp4_url: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('motionMP4URL'), 'exclude': lambda f: f is GeneratedImages.UNSET }})
    r"""The URL of the motion MP4."""
    motion_model: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('motionModel'), 'exclude': lambda f: f is GeneratedImages.UNSET }})
    r"""The name of the motion model."""
    motion_strength: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('motionStrength'), 'exclude': lambda f: f is GeneratedImages.UNSET }})
    r"""The motion strength."""
    nsfw: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nsfw'), 'exclude': lambda f: f is None }})
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetGenerationByIDLoras:
    r"""Element used for the generation."""
    UNSET='__SPEAKEASY_UNSET__'
    ak_uuid: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('akUUID'), 'exclude': lambda f: f is GetGenerationByIDLoras.UNSET }})
    r"""Unique identifier for the element. Elements can be found from the List Elements endpoint."""
    base_model: Optional[shared_sd_versions.SdVersions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('baseModel'), 'exclude': lambda f: f is None }})
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models"""
    description: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is GetGenerationByIDLoras.UNSET }})
    r"""Description for the element"""
    name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is GetGenerationByIDLoras.UNSET }})
    r"""Name of the element"""
    url_image: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('urlImage'), 'exclude': lambda f: f is GetGenerationByIDLoras.UNSET }})
    r"""URL of the element image"""
    weight_default: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weightDefault'), 'exclude': lambda f: f is GetGenerationByIDLoras.UNSET }})
    r"""Default weight for the element"""
    weight_max: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weightMax'), 'exclude': lambda f: f is GetGenerationByIDLoras.UNSET }})
    r"""Maximum weight for the element"""
    weight_min: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weightMin'), 'exclude': lambda f: f is GetGenerationByIDLoras.UNSET }})
    r"""Minimum weight for the element"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerationElements:
    r"""This table captures the elements that are applied to Generations."""
    UNSET='__SPEAKEASY_UNSET__'
    id: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is GenerationElements.UNSET }})
    lora: Optional[GetGenerationByIDLoras] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lora'), 'exclude': lambda f: f is GenerationElements.UNSET }})
    r"""Element used for the generation."""
    weight_applied: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weightApplied'), 'exclude': lambda f: f is GenerationElements.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetGenerationByIDGenerations:
    r"""columns and relationships of \\"generations\\" """
    UNSET='__SPEAKEASY_UNSET__'
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'exclude': lambda f: f is None }})
    generated_images: Optional[List[GeneratedImages]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generated_images'), 'exclude': lambda f: f is None }})
    generation_elements: Optional[List[GenerationElements]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generation_elements'), 'exclude': lambda f: f is None }})
    guidance_scale: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('guidanceScale'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    image_height: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageHeight'), 'exclude': lambda f: f is None }})
    image_width: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageWidth'), 'exclude': lambda f: f is None }})
    inference_steps: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inferenceSteps'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    init_strength: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initStrength'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    model_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    negative_prompt: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('negativePrompt'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    photo_real: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('photoReal'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    r"""If photoReal feature was used."""
    photo_real_strength: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('photoRealStrength'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    r"""Depth of field of photoReal used. 0.55 is low, 0.5 is medium, and 0.45 is high. Default is 0.55."""
    preset_style: Optional[shared_sd_generation_style.SdGenerationStyle] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('presetStyle'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    r"""The style to generate images with. When photoReal is enabled, refer to the Guide section for a full list. When alchemy is disabled, use LEONARDO or NONE. When alchemy is enabled, use ANIME, CREATIVE, DYNAMIC, ENVIRONMENT, GENERAL, ILLUSTRATION, PHOTOGRAPHY, RAYTRACED, RENDER_3D, SKETCH_BW, SKETCH_COLOR, or NONE."""
    prompt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt'), 'exclude': lambda f: f is None }})
    prompt_magic: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptMagic'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    r"""If prompt magic was used."""
    prompt_magic_strength: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptMagicStrength'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    r"""Strength of prompt magic used."""
    prompt_magic_version: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptMagicVersion'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    r"""Version of prompt magic used."""
    public: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public'), 'exclude': lambda f: f is None }})
    scheduler: Optional[shared_sd_generation_schedulers.SdGenerationSchedulers] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduler'), 'exclude': lambda f: f is None }})
    r"""The scheduler to generate images with. Defaults to EULER_DISCRETE if not specified."""
    sd_version: Optional[shared_sd_versions.SdVersions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sdVersion'), 'exclude': lambda f: f is None }})
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models"""
    seed: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is GetGenerationByIDGenerations.UNSET }})
    status: Optional[shared_job_status.JobStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the current task."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetGenerationByIDResponseBody:
    r"""Responses for GET /generations/{id}"""
    UNSET='__SPEAKEASY_UNSET__'
    generations_by_pk: Optional[GetGenerationByIDGenerations] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generations_by_pk'), 'exclude': lambda f: f is GetGenerationByIDResponseBody.UNSET }})
    r"""columns and relationships of \\"generations\\" """
    



@dataclasses.dataclass
class GetGenerationByIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[GetGenerationByIDResponseBody] = dataclasses.field(default=None)
    r"""Responses for GET /generations/{id}"""
    

