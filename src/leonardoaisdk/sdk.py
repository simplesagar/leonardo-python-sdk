"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .dataset import Dataset
from .element import Element
from .generation import Generation
from .initimage import InitImage
from .model import Model
from .sdkconfiguration import SDKConfiguration
from .user import User
from .variation import Variation
from leonardoaisdk import utils
from leonardoaisdk._hooks import SDKHooks
from leonardoaisdk.models import shared
from typing import Callable, Dict, Optional, Union

class LeonardoAiSDK:
    r"""Rest Endpoints: Leonardo.Ai API OpenAPI specification."""
    dataset: Dataset
    element: Element
    generation: Generation
    init_image: InitImage
    user: User
    model: Model
    variation: Variation

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 bearer_auth: Union[str, Callable[[], str]],
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[utils.RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param bearer_auth: The bearer_auth required for authentication
        :type bearer_auth: Union[str, Callable[[], str]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if callable(bearer_auth):
            def security():
                return shared.Security(bearer_auth = bearer_auth())
        else:
            security = shared.Security(bearer_auth = bearer_auth)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server_idx,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration._hooks = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.dataset = Dataset(self.sdk_configuration)
        self.element = Element(self.sdk_configuration)
        self.generation = Generation(self.sdk_configuration)
        self.init_image = InitImage(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
        self.model = Model(self.sdk_configuration)
        self.variation = Variation(self.sdk_configuration)
