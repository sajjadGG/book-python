Enum Built-in
=============


http.HTTPStatus
---------------
>>> from http import HTTPStatus

>>> HTTPStatus(200).name
'OK'
>>>
>>> HTTPStatus(404).name
'NOT_FOUND'
>>>
>>> HTTPStatus(500).name
'INTERNAL_SERVER_ERROR'
>>>
>>> HTTPStatus(418).name
'IM_A_TEAPOT'


http.HTTPMethod
---------------
* Since 3.11:

>>> from http import HTTPMethod

>>> HTTPMethod.GET
<HTTPMethod.GET>
>>>
>>> HTTPMethod.GET == 'GET'
True
>>>
>>> HTTPMethod.GET.value
'GET'
>>>
>>> HTTPMethod.GET.description
'Retrieve the target.'
>>>
>>> list(HTTPMethod)  # doctest: +NORMALIZE_WHITESPACE
[<HTTPMethod.CONNECT>,
 <HTTPMethod.DELETE>,
 <HTTPMethod.GET>,
 <HTTPMethod.HEAD>,
 <HTTPMethod.OPTIONS>,
 <HTTPMethod.PATCH>,
 <HTTPMethod.POST>,
 <HTTPMethod.PUT>,
 <HTTPMethod.TRACE>]


.. todo:: Assignments
