from ninja import Schema, ModelSchema

from wagtail.images.models import Image
from wagtail.documents.models import Document # Video 대신 사용
from typing import List

import traceback
import os
import re


class ErrorSchema(Schema):
    message: str


class BoolScema(Schema):
    result: bool


class ImageSchema(ModelSchema):

    class Config:
        model = Image
        model_fields = ['id', 'title', 'file']


class DocumentSchema(ModelSchema):

    class Config:
        model = Document
        model_fields = ['id', 'title', 'file']


class IdSchema(Schema):
    id_list: List


pattern_module_path = re.compile(r'File ".*[\\/]site-packages(.*)"')
error_schema_dict = {404: ErrorSchema, 500: ErrorSchema}


def handle_exception(exception: Exception):
    """
    API 요청 핸들링 시 예외 처리를 자동으로 해주는 함수

    Return
    ========
    >>> return 404, {'message': str }
    >>> return 500, {'message': str }

    `message`: 에러 정보, (에러 위치는 프로젝트 폴더에서부터 표시)

    Usage
    ========
        자동 예외 처리를 할 API 핸들링 함수의 @router의 response 인자로 **error_schema_dict 추가

        >>> response={200: SomeSchema, **error_schema_dict}
        >>> handle_exception(Exception)
    """
    message = ''
    
    # hiding full path
    for line in traceback.format_exc().splitlines(): 
        line = pattern_module_path.sub(r'File "~\1"', line).replace(rf'{os.getcwd()}', '~')
        message += line + '\n' 

    status = 404 if 'does not exist' in str(exception) else 500
    
    return status, {'message': message}
