import weaviate

auth_config = weaviate.AuthApiKey(api_key="xMdAWWpeYckcgBMYzF55Wsi2jHNZVYkSRzI1")

client = weaviate.Client(url="https://jobqezyor6kqgxnsyp2aag.c0.us-west3.gcp.weaviate.cloud",auth_client_secret=auth_config)

doc_class_schema = {
    "class": "GenAI_Video_Transcript",
    "vectorIndexType": "flat", 
    "vectorIndexConfig": {
        "distance": "cosine"},
    "description": "video transcript data to store document text in the form of chunks and vectors",
    "vectorizer": "text2vec-openai",
     "moduleConfig": {
        "text2vec-openai": {
           "model": "ada",
          "modelVersion": "003",  #// Parameter only applicable for `ada` model family and older
          "model": "text-embedding-3-small",
          "dimensions": 1536,  #// Parameter only applicable for `v3` model family and newer
          "type": "text",
        },
        "generative-openai": {
          "model": "gpt-4-1106-preview",  #// Optional - Defaults to `gpt-3.5-turbo`
          # "resourceName": "<YOUR-RESOURCE-NAME>",  #// For Azure OpenAI - Required
          # "deploymentId": "<YOUR-MODEL-NAME>",  #// For Azure OpenAI - Required
          "temperatureProperty": 0.2,  #// Optional, applicable to both OpenAI and Azure OpenAI
          # "maxTokensProperty": <max_tokens>,  #// Optional, applicable to both OpenAI and Azure OpenAI
          # "frequencyPenaltyProperty": <frequency_penalty>,  #// Optional, applicable to both OpenAI and Azure OpenAI
          # "presencePenaltyProperty": <presence_penalty>,  #// Optional, applicable to both OpenAI and Azure OpenAI
          "topPProperty": 5,  #// Optional, applicable to both OpenAI and Azure OpenAI
        }
      },

    "properties": [
        {
            "name": "gakey", 
            "dataType": ["string"],
            "description": "Unique user key",
        },
                {
            "name": "solution",
            "dataType": ["string"],
            "description": "Name of the solution",
        },
         {
            "name": "chunk",
            "dataType": ["string"],
            "description": "Chunk of document",
        },
         {
            "name": "created_date",
            "dataType": ["string"],
            "description": "date of record/data creation",
        },
        {
            "name": "time_frame",
            "dataType": ["string"],
            "description": "time of record/data creation",
        }
    ]
}
client.schema.create_class(doc_class_schema)