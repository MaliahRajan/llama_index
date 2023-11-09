# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from llama_index.ingestion.client.core.datetime_utils import serialize_datetime

from .text_node import TextNode


class EvalQuestionResult(pydantic.BaseModel):
    """
    Schema for the result of an eval question execution.
    """

    question_id: str = pydantic.Field(
        description="The ID of the question that was executed."
    )
    pipeline_id: str = pydantic.Field(
        description="The ID of the pipeline that the question was executed against."
    )
    retrieved_nodes: typing.List[TextNode] = pydantic.Field(
        description="The nodes retrieved by the pipeline for the given question."
    )
    answer: str = pydantic.Field(description="The answer to the question.")
    eval_metrics: typing.Dict[str, typing.Any] = pydantic.Field(
        description="The eval metrics for the question."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}