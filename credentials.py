AZURE_OAI_ENDPOINT="https://fghgfh.openai.azure.com/"
AZURE_OAI_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
AZURE_OAI_DEPLOYMENT="gpt-35-turbo-16k"
AZURE_SEARCH_ENDPOINT="https://fghgfh.openai.azure.com/openai/deployments/gpt-35-turbo-16k/chat/completions?api-version=2023-03-15-preview"
AZURE_SEARCH_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
AZURE_SEARCH_INDEX="margies-index"


\*

Update the configuration values to include:

The endpoint and a key from the Azure OpenAI resource you created (available on the Keys and Endpoint page for your Azure OpenAI resource in the Azure portal)

The deployment name you specified for your model deployment (available in the Deployments page in Azure AI Studio).

The endpoint for your search service (the Url value on the overview page for your search resource in the Azure portal).

A key for your search resource (available in the Keys page for your search resource in the Azure portal - you can use either of the admin keys)

The name of the search index (which should be margies-index).

Save the configuration file.

  */
