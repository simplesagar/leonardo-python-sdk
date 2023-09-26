"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UploadDatasetImageFromGenRequestBody:
    r"""Query parameters to be provided in the request body as a JSON object"""
    generated_image_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generatedImageId') }})
    r"""The ID of the image to upload to the dataset."""
    




@dataclasses.dataclass
class UploadDatasetImageFromGenRequest:
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'datasetId', 'style': 'simple', 'explode': False }})
    r"""The ID of the dataset to upload the image to."""
    request_body: UploadDatasetImageFromGenRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Query parameters to be provided in the request body as a JSON object"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UploadDatasetImageFromGen200ApplicationJSONDatasetGenUploadOutput:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UploadDatasetImageFromGen200ApplicationJSON:
    r"""Responses for POST /datasets/{datasetId}/upload/gen"""
    upload_dataset_image_from_gen: Optional[UploadDatasetImageFromGen200ApplicationJSONDatasetGenUploadOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uploadDatasetImageFromGen'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class UploadDatasetImageFromGenResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    upload_dataset_image_from_gen_200_application_json_object: Optional[UploadDatasetImageFromGen200ApplicationJSON] = dataclasses.field(default=None)
    r"""Responses for POST /datasets/{datasetId}/upload/gen"""
    

