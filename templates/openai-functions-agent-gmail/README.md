# OpenAI Functions Agent - Gmail

This template implements a simple agent using OpenAI function calling imports directly from [langchain-core](https://pypi.org/project/langchain-core/) and [`langchain-community`](https://pypi.org/project/langchain-community/).

This template creates an agent that uses OpenAI function calling to communicate its decisions on what actions to take. 

This example creates an agent that can optionally look up information on the internet using Tavily's search engine.

## Environment Setup

The following environment variables need to be set:

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

Create a [`credentials.json`](https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application) file containing your OAuth client ID from Gmail. To customize authentication, see the [Customize Auth](#customize-auth) section below.

_*Note:* The first time you run this app, it will force you to go through a user authentication flow._

## Usage

To use this package, you should first have the LangChain CLI installed:

```shell
pip install -U langchain-cli
```

To create a new LangChain project and install this as the only package, you can do:

```shell
langchain app new my-app --package openai-functions-agent-gmail
```

If you want to add this to an existing project, you can just run:

```shell
langchain app add openai-functions-agent-gmail
```

And add the following code to your `server.py` file:
```python
from openai_functions_agent import agent_executor as openai_functions_agent_chain

add_routes(app, openai_functions_agent_chain, path="/openai-functions-agent-gmail")
```

(Optional) Let's now configure LangSmith. 
LangSmith will help us trace, monitor and debug LangChain applications. 
LangSmith is currently in private beta, you can sign up [here](https://smith.langchain.com/). 
If you don't have access, you can skip this section

```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

If you are inside this directory, then you can spin up a LangServe instance directly by:

```shell
langchain serve
```

This will start the FastAPI app with a server is running locally at 
[http://localhost:8000](http://localhost:8000)

We can see all templates at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
We can access the playground at [http://127.0.0.1:8000/openai-functions-agent-gmail/playground](http://127.0.0.1:8000/openai-functions-agent/playground)  

We can access the template from code with:

```python
from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/openai-functions-agent-gmail")
```

## Customize Auth

```
from langchain.tools.gmail.utils import build_resource_service, get_gmail_credentials

# Can review scopes here https://developers.google.com/gmail/api/auth/scopes
# For instance, readonly scope is 'https://www.googleapis.com/auth/gmail.readonly'
credentials = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="credentials.json",
)
api_resource = build_resource_service(credentials=credentials)
toolkit = GmailToolkit(api_resource=api_resource)
```