"""
"""

from langchain_community.utilities.oxylabs_search import OxylabsSearchAPIWrapper
from langchain_community.tools.oxylabs_search import OxylabsSearchRun, OxylabsSearchResults



def test_oxylabs_search_call() -> None:
    """Test simple call to Oxylabs Search API."""
    oxylabs_search_tool = OxylabsSearchRun(wrapper=OxylabsSearchAPIWrapper())  # type: ignore[call-arg]

    output = oxylabs_search_tool.invoke("Python programming language")

    assert oxylabs_search_tool.name == "oxylabs_search"

    assert "high-level, general-purpose programming language" in output
    assert "extensions" in output
    assert ".py" in output
    assert "Guido van Rossum" in output
    assert isinstance(output, str)


def test_oxylabs_search_results_call() -> None:
    """Test simple results call to Oxylabs Search API."""
    oxylabs_search_tool = OxylabsSearchResults(wrapper=OxylabsSearchAPIWrapper())  # type: ignore[call-arg]

    output = oxylabs_search_tool.invoke("Python programming language")

    assert oxylabs_search_tool.name == "oxylabs_search_results"

    assert "high-level, general-purpose programming language" in output
    assert "extensions" in output
    assert ".py" in output
    assert "Guido van Rossum" in output
    assert isinstance(output, str)