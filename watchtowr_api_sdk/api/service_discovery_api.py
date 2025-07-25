# coding: utf-8

"""
    Complete watchTowr Platform API Documentation

    The watchTowr Client API combining all watchTowr Platform APIs into a single comprehensive reference, including:       * Continuous Assurance API       * Adversary Sight API       * Intelligence API       * Platform API 

    The version of the OpenAPI document: 1.0
    Contact: support@watchTowr.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import datetime
from pydantic import Field, StrictBool, StrictFloat, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from watchtowr_api_sdk.models.paginated_service_listing import PaginatedServiceListing

from watchtowr_api_sdk.api_client import ApiClient, RequestSerialized
from watchtowr_api_sdk.api_response import ApiResponse
from watchtowr_api_sdk.rest import RESTResponseType


class ServiceDiscoveryApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_list_service_listing(
        self,
        page: Annotated[Optional[StrictFloat], Field(description="The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.")] = None,
        page_size: Annotated[Optional[StrictFloat], Field(description="The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.")] = None,
        include_closed_port: Annotated[Optional[StrictBool], Field(description="Include listings with closed ports.")] = None,
        include_no_service: Annotated[Optional[StrictBool], Field(description="Include listings without a service")] = None,
        created_from: Annotated[Optional[datetime], Field(description="Filter services created after a given date and time.")] = None,
        created_to: Annotated[Optional[datetime], Field(description="Filter services created before a given date and time.")] = None,
        updated_from: Annotated[Optional[datetime], Field(description="Filter services updated after a given date and time.")] = None,
        updated_to: Annotated[Optional[datetime], Field(description="Filter services updated before a given date and time.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Search services by IP address.")] = None,
        countries: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated subject countries that they're related to.")] = None,
        technology: Annotated[Optional[StrictStr], Field(description="Filter services by technology name.")] = None,
        ports: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated port/protocols.")] = None,
        port_numbers: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated ports.")] = None,
        port_types: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated transport layer protocols (e.g. UDP/TCP).")] = None,
        port_services: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated services.")] = None,
        service_type_ids: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated service type IDs.")] = None,
        business_unit_ids: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated business unit IDs they're related to.")] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="Sort services.")] = None,
        order_by: Annotated[Optional[StrictStr], Field(description="Order services.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PaginatedServiceListing:
        """List Services

        List all discovered service assets, ordered by last seen date.

        :param page: The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.
        :type page: float
        :param page_size: The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.
        :type page_size: float
        :param include_closed_port: Include listings with closed ports.
        :type include_closed_port: bool
        :param include_no_service: Include listings without a service
        :type include_no_service: bool
        :param created_from: Filter services created after a given date and time.
        :type created_from: datetime
        :param created_to: Filter services created before a given date and time.
        :type created_to: datetime
        :param updated_from: Filter services updated after a given date and time.
        :type updated_from: datetime
        :param updated_to: Filter services updated before a given date and time.
        :type updated_to: datetime
        :param search: Search services by IP address.
        :type search: str
        :param countries: Filter services by a list of comma separated subject countries that they're related to.
        :type countries: str
        :param technology: Filter services by technology name.
        :type technology: str
        :param ports: Filter services by a list of comma separated port/protocols.
        :type ports: str
        :param port_numbers: Filter services by a list of comma separated ports.
        :type port_numbers: str
        :param port_types: Filter services by a list of comma separated transport layer protocols (e.g. UDP/TCP).
        :type port_types: str
        :param port_services: Filter services by a list of comma separated services.
        :type port_services: str
        :param service_type_ids: Filter services by a list of comma separated service type IDs.
        :type service_type_ids: str
        :param business_unit_ids: Filter services by a list of comma separated business unit IDs they're related to.
        :type business_unit_ids: str
        :param sort_by: Sort services.
        :type sort_by: str
        :param order_by: Order services.
        :type order_by: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_list_service_listing_serialize(
            page=page,
            page_size=page_size,
            include_closed_port=include_closed_port,
            include_no_service=include_no_service,
            created_from=created_from,
            created_to=created_to,
            updated_from=updated_from,
            updated_to=updated_to,
            search=search,
            countries=countries,
            technology=technology,
            ports=ports,
            port_numbers=port_numbers,
            port_types=port_types,
            port_services=port_services,
            service_type_ids=service_type_ids,
            business_unit_ids=business_unit_ids,
            sort_by=sort_by,
            order_by=order_by,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedServiceListing",
            '401': "Unauthorized",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_list_service_listing_with_http_info(
        self,
        page: Annotated[Optional[StrictFloat], Field(description="The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.")] = None,
        page_size: Annotated[Optional[StrictFloat], Field(description="The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.")] = None,
        include_closed_port: Annotated[Optional[StrictBool], Field(description="Include listings with closed ports.")] = None,
        include_no_service: Annotated[Optional[StrictBool], Field(description="Include listings without a service")] = None,
        created_from: Annotated[Optional[datetime], Field(description="Filter services created after a given date and time.")] = None,
        created_to: Annotated[Optional[datetime], Field(description="Filter services created before a given date and time.")] = None,
        updated_from: Annotated[Optional[datetime], Field(description="Filter services updated after a given date and time.")] = None,
        updated_to: Annotated[Optional[datetime], Field(description="Filter services updated before a given date and time.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Search services by IP address.")] = None,
        countries: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated subject countries that they're related to.")] = None,
        technology: Annotated[Optional[StrictStr], Field(description="Filter services by technology name.")] = None,
        ports: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated port/protocols.")] = None,
        port_numbers: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated ports.")] = None,
        port_types: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated transport layer protocols (e.g. UDP/TCP).")] = None,
        port_services: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated services.")] = None,
        service_type_ids: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated service type IDs.")] = None,
        business_unit_ids: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated business unit IDs they're related to.")] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="Sort services.")] = None,
        order_by: Annotated[Optional[StrictStr], Field(description="Order services.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PaginatedServiceListing]:
        """List Services

        List all discovered service assets, ordered by last seen date.

        :param page: The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.
        :type page: float
        :param page_size: The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.
        :type page_size: float
        :param include_closed_port: Include listings with closed ports.
        :type include_closed_port: bool
        :param include_no_service: Include listings without a service
        :type include_no_service: bool
        :param created_from: Filter services created after a given date and time.
        :type created_from: datetime
        :param created_to: Filter services created before a given date and time.
        :type created_to: datetime
        :param updated_from: Filter services updated after a given date and time.
        :type updated_from: datetime
        :param updated_to: Filter services updated before a given date and time.
        :type updated_to: datetime
        :param search: Search services by IP address.
        :type search: str
        :param countries: Filter services by a list of comma separated subject countries that they're related to.
        :type countries: str
        :param technology: Filter services by technology name.
        :type technology: str
        :param ports: Filter services by a list of comma separated port/protocols.
        :type ports: str
        :param port_numbers: Filter services by a list of comma separated ports.
        :type port_numbers: str
        :param port_types: Filter services by a list of comma separated transport layer protocols (e.g. UDP/TCP).
        :type port_types: str
        :param port_services: Filter services by a list of comma separated services.
        :type port_services: str
        :param service_type_ids: Filter services by a list of comma separated service type IDs.
        :type service_type_ids: str
        :param business_unit_ids: Filter services by a list of comma separated business unit IDs they're related to.
        :type business_unit_ids: str
        :param sort_by: Sort services.
        :type sort_by: str
        :param order_by: Order services.
        :type order_by: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_list_service_listing_serialize(
            page=page,
            page_size=page_size,
            include_closed_port=include_closed_port,
            include_no_service=include_no_service,
            created_from=created_from,
            created_to=created_to,
            updated_from=updated_from,
            updated_to=updated_to,
            search=search,
            countries=countries,
            technology=technology,
            ports=ports,
            port_numbers=port_numbers,
            port_types=port_types,
            port_services=port_services,
            service_type_ids=service_type_ids,
            business_unit_ids=business_unit_ids,
            sort_by=sort_by,
            order_by=order_by,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedServiceListing",
            '401': "Unauthorized",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_list_service_listing_without_preload_content(
        self,
        page: Annotated[Optional[StrictFloat], Field(description="The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.")] = None,
        page_size: Annotated[Optional[StrictFloat], Field(description="The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.")] = None,
        include_closed_port: Annotated[Optional[StrictBool], Field(description="Include listings with closed ports.")] = None,
        include_no_service: Annotated[Optional[StrictBool], Field(description="Include listings without a service")] = None,
        created_from: Annotated[Optional[datetime], Field(description="Filter services created after a given date and time.")] = None,
        created_to: Annotated[Optional[datetime], Field(description="Filter services created before a given date and time.")] = None,
        updated_from: Annotated[Optional[datetime], Field(description="Filter services updated after a given date and time.")] = None,
        updated_to: Annotated[Optional[datetime], Field(description="Filter services updated before a given date and time.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Search services by IP address.")] = None,
        countries: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated subject countries that they're related to.")] = None,
        technology: Annotated[Optional[StrictStr], Field(description="Filter services by technology name.")] = None,
        ports: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated port/protocols.")] = None,
        port_numbers: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated ports.")] = None,
        port_types: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated transport layer protocols (e.g. UDP/TCP).")] = None,
        port_services: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated services.")] = None,
        service_type_ids: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated service type IDs.")] = None,
        business_unit_ids: Annotated[Optional[StrictStr], Field(description="Filter services by a list of comma separated business unit IDs they're related to.")] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="Sort services.")] = None,
        order_by: Annotated[Optional[StrictStr], Field(description="Order services.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List Services

        List all discovered service assets, ordered by last seen date.

        :param page: The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.
        :type page: float
        :param page_size: The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.
        :type page_size: float
        :param include_closed_port: Include listings with closed ports.
        :type include_closed_port: bool
        :param include_no_service: Include listings without a service
        :type include_no_service: bool
        :param created_from: Filter services created after a given date and time.
        :type created_from: datetime
        :param created_to: Filter services created before a given date and time.
        :type created_to: datetime
        :param updated_from: Filter services updated after a given date and time.
        :type updated_from: datetime
        :param updated_to: Filter services updated before a given date and time.
        :type updated_to: datetime
        :param search: Search services by IP address.
        :type search: str
        :param countries: Filter services by a list of comma separated subject countries that they're related to.
        :type countries: str
        :param technology: Filter services by technology name.
        :type technology: str
        :param ports: Filter services by a list of comma separated port/protocols.
        :type ports: str
        :param port_numbers: Filter services by a list of comma separated ports.
        :type port_numbers: str
        :param port_types: Filter services by a list of comma separated transport layer protocols (e.g. UDP/TCP).
        :type port_types: str
        :param port_services: Filter services by a list of comma separated services.
        :type port_services: str
        :param service_type_ids: Filter services by a list of comma separated service type IDs.
        :type service_type_ids: str
        :param business_unit_ids: Filter services by a list of comma separated business unit IDs they're related to.
        :type business_unit_ids: str
        :param sort_by: Sort services.
        :type sort_by: str
        :param order_by: Order services.
        :type order_by: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_list_service_listing_serialize(
            page=page,
            page_size=page_size,
            include_closed_port=include_closed_port,
            include_no_service=include_no_service,
            created_from=created_from,
            created_to=created_to,
            updated_from=updated_from,
            updated_to=updated_to,
            search=search,
            countries=countries,
            technology=technology,
            ports=ports,
            port_numbers=port_numbers,
            port_types=port_types,
            port_services=port_services,
            service_type_ids=service_type_ids,
            business_unit_ids=business_unit_ids,
            sort_by=sort_by,
            order_by=order_by,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedServiceListing",
            '401': "Unauthorized",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_list_service_listing_serialize(
        self,
        page,
        page_size,
        include_closed_port,
        include_no_service,
        created_from,
        created_to,
        updated_from,
        updated_to,
        search,
        countries,
        technology,
        ports,
        port_numbers,
        port_types,
        port_services,
        service_type_ids,
        business_unit_ids,
        sort_by,
        order_by,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if include_closed_port is not None:
            
            _query_params.append(('includeClosedPort', include_closed_port))
            
        if include_no_service is not None:
            
            _query_params.append(('includeNoService', include_no_service))
            
        if created_from is not None:
            if isinstance(created_from, datetime):
                _query_params.append(
                    (
                        'created_from',
                        created_from.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('created_from', created_from))
            
        if created_to is not None:
            if isinstance(created_to, datetime):
                _query_params.append(
                    (
                        'created_to',
                        created_to.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('created_to', created_to))
            
        if updated_from is not None:
            if isinstance(updated_from, datetime):
                _query_params.append(
                    (
                        'updated_from',
                        updated_from.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('updated_from', updated_from))
            
        if updated_to is not None:
            if isinstance(updated_to, datetime):
                _query_params.append(
                    (
                        'updated_to',
                        updated_to.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('updated_to', updated_to))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if countries is not None:
            
            _query_params.append(('countries', countries))
            
        if technology is not None:
            
            _query_params.append(('technology', technology))
            
        if ports is not None:
            
            _query_params.append(('ports', ports))
            
        if port_numbers is not None:
            
            _query_params.append(('portNumbers', port_numbers))
            
        if port_types is not None:
            
            _query_params.append(('portTypes', port_types))
            
        if port_services is not None:
            
            _query_params.append(('portServices', port_services))
            
        if service_type_ids is not None:
            
            _query_params.append(('serviceTypeIds', service_type_ids))
            
        if business_unit_ids is not None:
            
            _query_params.append(('businessUnitIds', business_unit_ids))
            
        if sort_by is not None:
            
            _query_params.append(('sortBy', sort_by))
            
        if order_by is not None:
            
            _query_params.append(('orderBy', order_by))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/client/service-listing/list',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


