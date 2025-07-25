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
from watchtowr_api_sdk.models.paginated_point_of_interest import PaginatedPointOfInterest

from watchtowr_api_sdk.api_client import ApiClient, RequestSerialized
from watchtowr_api_sdk.api_response import ApiResponse
from watchtowr_api_sdk.rest import RESTResponseType


class PointsOfInterestApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_list_points_of_interest(
        self,
        page: Annotated[Optional[StrictFloat], Field(description="The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.")] = None,
        page_size: Annotated[Optional[StrictFloat], Field(description="The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.")] = None,
        created_from: Annotated[Optional[datetime], Field(description="Filter points of interest created after a given date and time.")] = None,
        created_to: Annotated[Optional[datetime], Field(description="Filter points of interest created before a given date and time.")] = None,
        updated_from: Annotated[Optional[datetime], Field(description="Filter points of interest updated after a given date and time.")] = None,
        updated_to: Annotated[Optional[datetime], Field(description="Filter points of interest updated before a given date and time.")] = None,
        discovered_date_order: Annotated[Optional[StrictStr], Field(description="Order points of interest by their discovery date.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Search Points of Interest by name or URL.")] = None,
        types: Annotated[Optional[StrictStr], Field(description="Filter by a comma separated list of types.")] = None,
        has_finding: Annotated[Optional[StrictBool], Field(description="Filter points of interest that have findings.")] = None,
        start_date: Annotated[Optional[datetime], Field(description="Filter points of interest by start date.")] = None,
        end_date: Annotated[Optional[datetime], Field(description="Filter points of interest by end date.")] = None,
        asset_statuses: Annotated[Optional[StrictStr], Field(description="Filter points of interest by a comma separated list of asset statuses.")] = None,
        business_unit_ids: Annotated[Optional[StrictStr], Field(description="Filter points of interest by a comma separated list of business unit IDs.")] = None,
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
    ) -> PaginatedPointOfInterest:
        """List Points of Interest

        List all discovered Points of Interest assets, ordered by discovery date.

        :param page: The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.
        :type page: float
        :param page_size: The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.
        :type page_size: float
        :param created_from: Filter points of interest created after a given date and time.
        :type created_from: datetime
        :param created_to: Filter points of interest created before a given date and time.
        :type created_to: datetime
        :param updated_from: Filter points of interest updated after a given date and time.
        :type updated_from: datetime
        :param updated_to: Filter points of interest updated before a given date and time.
        :type updated_to: datetime
        :param discovered_date_order: Order points of interest by their discovery date.
        :type discovered_date_order: str
        :param search: Search Points of Interest by name or URL.
        :type search: str
        :param types: Filter by a comma separated list of types.
        :type types: str
        :param has_finding: Filter points of interest that have findings.
        :type has_finding: bool
        :param start_date: Filter points of interest by start date.
        :type start_date: datetime
        :param end_date: Filter points of interest by end date.
        :type end_date: datetime
        :param asset_statuses: Filter points of interest by a comma separated list of asset statuses.
        :type asset_statuses: str
        :param business_unit_ids: Filter points of interest by a comma separated list of business unit IDs.
        :type business_unit_ids: str
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

        _param = self._get_list_points_of_interest_serialize(
            page=page,
            page_size=page_size,
            created_from=created_from,
            created_to=created_to,
            updated_from=updated_from,
            updated_to=updated_to,
            discovered_date_order=discovered_date_order,
            search=search,
            types=types,
            has_finding=has_finding,
            start_date=start_date,
            end_date=end_date,
            asset_statuses=asset_statuses,
            business_unit_ids=business_unit_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedPointOfInterest",
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
    def get_list_points_of_interest_with_http_info(
        self,
        page: Annotated[Optional[StrictFloat], Field(description="The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.")] = None,
        page_size: Annotated[Optional[StrictFloat], Field(description="The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.")] = None,
        created_from: Annotated[Optional[datetime], Field(description="Filter points of interest created after a given date and time.")] = None,
        created_to: Annotated[Optional[datetime], Field(description="Filter points of interest created before a given date and time.")] = None,
        updated_from: Annotated[Optional[datetime], Field(description="Filter points of interest updated after a given date and time.")] = None,
        updated_to: Annotated[Optional[datetime], Field(description="Filter points of interest updated before a given date and time.")] = None,
        discovered_date_order: Annotated[Optional[StrictStr], Field(description="Order points of interest by their discovery date.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Search Points of Interest by name or URL.")] = None,
        types: Annotated[Optional[StrictStr], Field(description="Filter by a comma separated list of types.")] = None,
        has_finding: Annotated[Optional[StrictBool], Field(description="Filter points of interest that have findings.")] = None,
        start_date: Annotated[Optional[datetime], Field(description="Filter points of interest by start date.")] = None,
        end_date: Annotated[Optional[datetime], Field(description="Filter points of interest by end date.")] = None,
        asset_statuses: Annotated[Optional[StrictStr], Field(description="Filter points of interest by a comma separated list of asset statuses.")] = None,
        business_unit_ids: Annotated[Optional[StrictStr], Field(description="Filter points of interest by a comma separated list of business unit IDs.")] = None,
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
    ) -> ApiResponse[PaginatedPointOfInterest]:
        """List Points of Interest

        List all discovered Points of Interest assets, ordered by discovery date.

        :param page: The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.
        :type page: float
        :param page_size: The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.
        :type page_size: float
        :param created_from: Filter points of interest created after a given date and time.
        :type created_from: datetime
        :param created_to: Filter points of interest created before a given date and time.
        :type created_to: datetime
        :param updated_from: Filter points of interest updated after a given date and time.
        :type updated_from: datetime
        :param updated_to: Filter points of interest updated before a given date and time.
        :type updated_to: datetime
        :param discovered_date_order: Order points of interest by their discovery date.
        :type discovered_date_order: str
        :param search: Search Points of Interest by name or URL.
        :type search: str
        :param types: Filter by a comma separated list of types.
        :type types: str
        :param has_finding: Filter points of interest that have findings.
        :type has_finding: bool
        :param start_date: Filter points of interest by start date.
        :type start_date: datetime
        :param end_date: Filter points of interest by end date.
        :type end_date: datetime
        :param asset_statuses: Filter points of interest by a comma separated list of asset statuses.
        :type asset_statuses: str
        :param business_unit_ids: Filter points of interest by a comma separated list of business unit IDs.
        :type business_unit_ids: str
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

        _param = self._get_list_points_of_interest_serialize(
            page=page,
            page_size=page_size,
            created_from=created_from,
            created_to=created_to,
            updated_from=updated_from,
            updated_to=updated_to,
            discovered_date_order=discovered_date_order,
            search=search,
            types=types,
            has_finding=has_finding,
            start_date=start_date,
            end_date=end_date,
            asset_statuses=asset_statuses,
            business_unit_ids=business_unit_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedPointOfInterest",
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
    def get_list_points_of_interest_without_preload_content(
        self,
        page: Annotated[Optional[StrictFloat], Field(description="The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.")] = None,
        page_size: Annotated[Optional[StrictFloat], Field(description="The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.")] = None,
        created_from: Annotated[Optional[datetime], Field(description="Filter points of interest created after a given date and time.")] = None,
        created_to: Annotated[Optional[datetime], Field(description="Filter points of interest created before a given date and time.")] = None,
        updated_from: Annotated[Optional[datetime], Field(description="Filter points of interest updated after a given date and time.")] = None,
        updated_to: Annotated[Optional[datetime], Field(description="Filter points of interest updated before a given date and time.")] = None,
        discovered_date_order: Annotated[Optional[StrictStr], Field(description="Order points of interest by their discovery date.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Search Points of Interest by name or URL.")] = None,
        types: Annotated[Optional[StrictStr], Field(description="Filter by a comma separated list of types.")] = None,
        has_finding: Annotated[Optional[StrictBool], Field(description="Filter points of interest that have findings.")] = None,
        start_date: Annotated[Optional[datetime], Field(description="Filter points of interest by start date.")] = None,
        end_date: Annotated[Optional[datetime], Field(description="Filter points of interest by end date.")] = None,
        asset_statuses: Annotated[Optional[StrictStr], Field(description="Filter points of interest by a comma separated list of asset statuses.")] = None,
        business_unit_ids: Annotated[Optional[StrictStr], Field(description="Filter points of interest by a comma separated list of business unit IDs.")] = None,
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
        """List Points of Interest

        List all discovered Points of Interest assets, ordered by discovery date.

        :param page: The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.
        :type page: float
        :param page_size: The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.
        :type page_size: float
        :param created_from: Filter points of interest created after a given date and time.
        :type created_from: datetime
        :param created_to: Filter points of interest created before a given date and time.
        :type created_to: datetime
        :param updated_from: Filter points of interest updated after a given date and time.
        :type updated_from: datetime
        :param updated_to: Filter points of interest updated before a given date and time.
        :type updated_to: datetime
        :param discovered_date_order: Order points of interest by their discovery date.
        :type discovered_date_order: str
        :param search: Search Points of Interest by name or URL.
        :type search: str
        :param types: Filter by a comma separated list of types.
        :type types: str
        :param has_finding: Filter points of interest that have findings.
        :type has_finding: bool
        :param start_date: Filter points of interest by start date.
        :type start_date: datetime
        :param end_date: Filter points of interest by end date.
        :type end_date: datetime
        :param asset_statuses: Filter points of interest by a comma separated list of asset statuses.
        :type asset_statuses: str
        :param business_unit_ids: Filter points of interest by a comma separated list of business unit IDs.
        :type business_unit_ids: str
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

        _param = self._get_list_points_of_interest_serialize(
            page=page,
            page_size=page_size,
            created_from=created_from,
            created_to=created_to,
            updated_from=updated_from,
            updated_to=updated_to,
            discovered_date_order=discovered_date_order,
            search=search,
            types=types,
            has_finding=has_finding,
            start_date=start_date,
            end_date=end_date,
            asset_statuses=asset_statuses,
            business_unit_ids=business_unit_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedPointOfInterest",
            '401': "Unauthorized",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_list_points_of_interest_serialize(
        self,
        page,
        page_size,
        created_from,
        created_to,
        updated_from,
        updated_to,
        discovered_date_order,
        search,
        types,
        has_finding,
        start_date,
        end_date,
        asset_statuses,
        business_unit_ids,
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
            
        if discovered_date_order is not None:
            
            _query_params.append(('discoveredDateOrder', discovered_date_order))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if types is not None:
            
            _query_params.append(('types', types))
            
        if has_finding is not None:
            
            _query_params.append(('hasFinding', has_finding))
            
        if start_date is not None:
            if isinstance(start_date, datetime):
                _query_params.append(
                    (
                        'startDate',
                        start_date.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('startDate', start_date))
            
        if end_date is not None:
            if isinstance(end_date, datetime):
                _query_params.append(
                    (
                        'endDate',
                        end_date.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('endDate', end_date))
            
        if asset_statuses is not None:
            
            _query_params.append(('assetStatuses', asset_statuses))
            
        if business_unit_ids is not None:
            
            _query_params.append(('businessUnitIds', business_unit_ids))
            
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
            resource_path='/api/client/points-of-interest/list',
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


