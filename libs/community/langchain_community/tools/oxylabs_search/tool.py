"""Tool for the Oxylabs Search API."""

import json
from typing import Optional, Type

from langchain_core.callbacks import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

from langchain_community.utilities.oxylabs_search import OxylabsSearchAPIWrapper


class OxylabsSearchQueryInput(BaseModel):
    """Input for the OxylabsSearch tool."""

    query: str = Field(description="query to retrieve on Oxylabs Search API")
    geo_location: str = Field(
        default="California,United States",
        description="Geographic location for the search;"
        " adjust if location-specific information is requested.",
    )


class OxylabsSearchRun(BaseTool):
    """Tool that queries a Oxylabs instance."""

    name: str = "oxylabs_search"
    description: str = (
        "A meta search engine."
        "Ideal for situations where you need to answer questions about current events,"
        "facts, products, recipes, local information, and other topics "
        "that can be explored via web browsing. "
        "The input should be a search query and, if applicable,"
        " a geo_location string to enhance result accuracy. "
        "The output is a compiled, formatted summary of query results. "
    )
    args_schema: Type[BaseModel] = OxylabsSearchQueryInput  # type: ignore

    def _run(
        self,
        query: str,
        geo_location: Optional[str] = "",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""

        parameters = {"geo_location": geo_location}
        wrapper_ = OxylabsSearchAPIWrapper(params=parameters)

        return wrapper_.run(query)

    async def _arun(
        self,
        query: str,
        geo_location: Optional[str] = "",
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""

        parameters = {"geo_location": geo_location}
        wrapper_ = OxylabsSearchAPIWrapper(params=parameters)

        return await wrapper_.arun(query)


class OxylabsSearchResults(BaseTool):
    """Tool that queries a Oxylabs instance and gets back json."""

    name: str = "oxylabs_search_results"
    description: str = (
        "A meta search engine."
        "Ideal for situations where you need to answer questions about current events,"
        "facts, products, recipes, local information, and other topics "
        "that can be explored via web browsing. "
        "The input should be a search query and, if applicable,"
        " a geo_location string to enhance result accuracy. "
        "The output is a JSON array of response page objects. "
    )
    args_schema: Type[BaseModel] = OxylabsSearchQueryInput  # type: ignore

    def _run(
        self,
        query: str,
        geo_location: Optional[str] = "",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""

        parameters = {"geo_location": geo_location}
        wrapper_ = OxylabsSearchAPIWrapper(params=parameters)

        return json.dumps(wrapper_.results(query))

    async def _arun(
        self,
        query: str,
        geo_location: Optional[str] = "",
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""

        parameters = {"geo_location": geo_location}
        wrapper_ = OxylabsSearchAPIWrapper(params=parameters)

        return json.dumps(await wrapper_.aresults(query))
