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

from pydantic import Field, StrictFloat, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from watchtowr_api_sdk.models.paginated_client_finding_retest_history import PaginatedClientFindingRetestHistory

from watchtowr_api_sdk.api_client import ApiClient, RequestSerialized
from watchtowr_api_sdk.api_response import ApiResponse
from watchtowr_api_sdk.rest import RESTResponseType


class FindingRetestHistoryApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_list_finding_retest_history(
        self,
        page: Annotated[Optional[StrictFloat], Field(description="The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.")] = None,
        page_size: Annotated[Optional[StrictFloat], Field(description="The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.")] = None,
        business_unit_ids: Annotated[Optional[StrictStr], Field(description="Filter assets by a list of comma separated business unit IDs that the asset is related to.")] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="Sort by field")] = None,
        sort_order: Annotated[Optional[StrictStr], Field(description="Sort order")] = None,
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
    ) -> PaginatedClientFindingRetestHistory:
        """List Finding Retest History

        List all finding retest history entries, ordered by creation date.

        :param page: The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.
        :type page: float
        :param page_size: The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.
        :type page_size: float
        :param business_unit_ids: Filter assets by a list of comma separated business unit IDs that the asset is related to.
        :type business_unit_ids: str
        :param sort_by: Sort by field
        :type sort_by: str
        :param sort_order: Sort order
        :type sort_order: str
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

        _param = self._get_list_finding_retest_history_serialize(
            page=page,
            page_size=page_size,
            business_unit_ids=business_unit_ids,
            sort_by=sort_by,
            sort_order=sort_order,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedClientFindingRetestHistory",
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
    def get_list_finding_retest_history_with_http_info(
        self,
        page: Annotated[Optional[StrictFloat], Field(description="The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.")] = None,
        page_size: Annotated[Optional[StrictFloat], Field(description="The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.")] = None,
        business_unit_ids: Annotated[Optional[StrictStr], Field(description="Filter assets by a list of comma separated business unit IDs that the asset is related to.")] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="Sort by field")] = None,
        sort_order: Annotated[Optional[StrictStr], Field(description="Sort order")] = None,
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
    ) -> ApiResponse[PaginatedClientFindingRetestHistory]:
        """List Finding Retest History

        List all finding retest history entries, ordered by creation date.

        :param page: The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.
        :type page: float
        :param page_size: The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.
        :type page_size: float
        :param business_unit_ids: Filter assets by a list of comma separated business unit IDs that the asset is related to.
        :type business_unit_ids: str
        :param sort_by: Sort by field
        :type sort_by: str
        :param sort_order: Sort order
        :type sort_order: str
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

        _param = self._get_list_finding_retest_history_serialize(
            page=page,
            page_size=page_size,
            business_unit_ids=business_unit_ids,
            sort_by=sort_by,
            sort_order=sort_order,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedClientFindingRetestHistory",
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
    def get_list_finding_retest_history_without_preload_content(
        self,
        page: Annotated[Optional[StrictFloat], Field(description="The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.")] = None,
        page_size: Annotated[Optional[StrictFloat], Field(description="The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.")] = None,
        business_unit_ids: Annotated[Optional[StrictStr], Field(description="Filter assets by a list of comma separated business unit IDs that the asset is related to.")] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="Sort by field")] = None,
        sort_order: Annotated[Optional[StrictStr], Field(description="Sort order")] = None,
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
        """List Finding Retest History

        List all finding retest history entries, ordered by creation date.

        :param page: The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.
        :type page: float
        :param page_size: The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.
        :type page_size: float
        :param business_unit_ids: Filter assets by a list of comma separated business unit IDs that the asset is related to.
        :type business_unit_ids: str
        :param sort_by: Sort by field
        :type sort_by: str
        :param sort_order: Sort order
        :type sort_order: str
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

        _param = self._get_list_finding_retest_history_serialize(
            page=page,
            page_size=page_size,
            business_unit_ids=business_unit_ids,
            sort_by=sort_by,
            sort_order=sort_order,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedClientFindingRetestHistory",
            '401': "Unauthorized",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_list_finding_retest_history_serialize(
        self,
        page,
        page_size,
        business_unit_ids,
        sort_by,
        sort_order,
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
            
        if business_unit_ids is not None:
            
            _query_params.append(('businessUnitIds', business_unit_ids))
            
        if sort_by is not None:
            
            _query_params.append(('sortBy', sort_by))
            
        if sort_order is not None:
            
            _query_params.append(('sortOrder', sort_order))
            
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
            resource_path='/api/client/finding-retest-history/list',
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


