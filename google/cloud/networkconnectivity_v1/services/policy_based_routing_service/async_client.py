# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.networkconnectivity_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

from google.cloud.networkconnectivity_v1.services.policy_based_routing_service import (
    pagers,
)
from google.cloud.networkconnectivity_v1.types import common, policy_based_routing

from .client import PolicyBasedRoutingServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, PolicyBasedRoutingServiceTransport
from .transports.grpc_asyncio import PolicyBasedRoutingServiceGrpcAsyncIOTransport


class PolicyBasedRoutingServiceAsyncClient:
    """Policy-Based Routing allows GCP customers to specify
    flexibile routing policies for Layer 4 traffic traversing
    through the connected service.
    """

    _client: PolicyBasedRoutingServiceClient

    DEFAULT_ENDPOINT = PolicyBasedRoutingServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PolicyBasedRoutingServiceClient.DEFAULT_MTLS_ENDPOINT

    network_path = staticmethod(PolicyBasedRoutingServiceClient.network_path)
    parse_network_path = staticmethod(
        PolicyBasedRoutingServiceClient.parse_network_path
    )
    policy_based_route_path = staticmethod(
        PolicyBasedRoutingServiceClient.policy_based_route_path
    )
    parse_policy_based_route_path = staticmethod(
        PolicyBasedRoutingServiceClient.parse_policy_based_route_path
    )
    common_billing_account_path = staticmethod(
        PolicyBasedRoutingServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        PolicyBasedRoutingServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        PolicyBasedRoutingServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        PolicyBasedRoutingServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        PolicyBasedRoutingServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        PolicyBasedRoutingServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        PolicyBasedRoutingServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        PolicyBasedRoutingServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        PolicyBasedRoutingServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        PolicyBasedRoutingServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PolicyBasedRoutingServiceAsyncClient: The constructed client.
        """
        return PolicyBasedRoutingServiceClient.from_service_account_info.__func__(PolicyBasedRoutingServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PolicyBasedRoutingServiceAsyncClient: The constructed client.
        """
        return PolicyBasedRoutingServiceClient.from_service_account_file.__func__(PolicyBasedRoutingServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return PolicyBasedRoutingServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> PolicyBasedRoutingServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            PolicyBasedRoutingServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(PolicyBasedRoutingServiceClient).get_transport_class,
        type(PolicyBasedRoutingServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, PolicyBasedRoutingServiceTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the policy based routing service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.PolicyBasedRoutingServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = PolicyBasedRoutingServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_policy_based_routes(
        self,
        request: Optional[
            Union[policy_based_routing.ListPolicyBasedRoutesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPolicyBasedRoutesAsyncPager:
        r"""Lists PolicyBasedRoutes in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import networkconnectivity_v1

            async def sample_list_policy_based_routes():
                # Create a client
                client = networkconnectivity_v1.PolicyBasedRoutingServiceAsyncClient()

                # Initialize request argument(s)
                request = networkconnectivity_v1.ListPolicyBasedRoutesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_policy_based_routes(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.networkconnectivity_v1.types.ListPolicyBasedRoutesRequest, dict]]):
                The request object. Request for
                [PolicyBasedRouting.ListPolicyBasedRoutes][] method.
            parent (:class:`str`):
                Required. The parent resource's name.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.networkconnectivity_v1.services.policy_based_routing_service.pagers.ListPolicyBasedRoutesAsyncPager:
                Response for
                [PolicyBasedRouting.ListPolicyBasedRoutes][] method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policy_based_routing.ListPolicyBasedRoutesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_policy_based_routes,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListPolicyBasedRoutesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_policy_based_route(
        self,
        request: Optional[
            Union[policy_based_routing.GetPolicyBasedRouteRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policy_based_routing.PolicyBasedRoute:
        r"""Gets details of a single PolicyBasedRoute.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import networkconnectivity_v1

            async def sample_get_policy_based_route():
                # Create a client
                client = networkconnectivity_v1.PolicyBasedRoutingServiceAsyncClient()

                # Initialize request argument(s)
                request = networkconnectivity_v1.GetPolicyBasedRouteRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_policy_based_route(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.networkconnectivity_v1.types.GetPolicyBasedRouteRequest, dict]]):
                The request object. Request for
                [PolicyBasedRouting.GetPolicyBasedRoute][] method.
            name (:class:`str`):
                Required. Name of the
                PolicyBasedRoute resource to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.networkconnectivity_v1.types.PolicyBasedRoute:
                Policy Based Routes (PBR) are more
                powerful routes that allows GCP
                customers to route their L4 network
                traffic based on not just destination
                IP, but also source IP, protocol and
                more. A PBR always take precedence when
                it conflicts with other types of routes.
                Next id: 19

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policy_based_routing.GetPolicyBasedRouteRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_policy_based_route,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_policy_based_route(
        self,
        request: Optional[
            Union[policy_based_routing.CreatePolicyBasedRouteRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        policy_based_route: Optional[policy_based_routing.PolicyBasedRoute] = None,
        policy_based_route_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new PolicyBasedRoute in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import networkconnectivity_v1

            async def sample_create_policy_based_route():
                # Create a client
                client = networkconnectivity_v1.PolicyBasedRoutingServiceAsyncClient()

                # Initialize request argument(s)
                policy_based_route = networkconnectivity_v1.PolicyBasedRoute()
                policy_based_route.next_hop_ilb_ip = "next_hop_ilb_ip_value"
                policy_based_route.network = "network_value"
                policy_based_route.filter.protocol_version = "IPV4"

                request = networkconnectivity_v1.CreatePolicyBasedRouteRequest(
                    parent="parent_value",
                    policy_based_route=policy_based_route,
                )

                # Make the request
                operation = client.create_policy_based_route(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.networkconnectivity_v1.types.CreatePolicyBasedRouteRequest, dict]]):
                The request object. Request for
                [PolicyBasedRouting.CreatePolicyBasedRoute][] method.
            parent (:class:`str`):
                Required. The parent resource's name
                of the PolicyBasedRoute.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            policy_based_route (:class:`google.cloud.networkconnectivity_v1.types.PolicyBasedRoute`):
                Required. Initial values for a new
                Policy Based Route.

                This corresponds to the ``policy_based_route`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            policy_based_route_id (:class:`str`):
                Optional. Unique id for the Policy
                Based Route to create.

                This corresponds to the ``policy_based_route_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.networkconnectivity_v1.types.PolicyBasedRoute` Policy Based Routes (PBR) are more powerful routes that allows GCP customers
                   to route their L4 network traffic based on not just
                   destination IP, but also source IP, protocol and
                   more. A PBR always take precedence when it conflicts
                   with other types of routes. Next id: 19

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, policy_based_route, policy_based_route_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policy_based_routing.CreatePolicyBasedRouteRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if policy_based_route is not None:
            request.policy_based_route = policy_based_route
        if policy_based_route_id is not None:
            request.policy_based_route_id = policy_based_route_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_policy_based_route,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            policy_based_routing.PolicyBasedRoute,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_policy_based_route(
        self,
        request: Optional[
            Union[policy_based_routing.DeletePolicyBasedRouteRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single PolicyBasedRoute.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import networkconnectivity_v1

            async def sample_delete_policy_based_route():
                # Create a client
                client = networkconnectivity_v1.PolicyBasedRoutingServiceAsyncClient()

                # Initialize request argument(s)
                request = networkconnectivity_v1.DeletePolicyBasedRouteRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_policy_based_route(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.networkconnectivity_v1.types.DeletePolicyBasedRouteRequest, dict]]):
                The request object. Request for
                [PolicyBasedRouting.DeletePolicyBasedRoute][] method.
            name (:class:`str`):
                Required. Name of the
                PolicyBasedRoute resource to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policy_based_routing.DeletePolicyBasedRouteRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_policy_based_route,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("PolicyBasedRoutingServiceAsyncClient",)
