import weaviate

# Initialize client with authentication
auth_config = weaviate.AuthApiKey(api_key="xMdAWWpeYckcgBMYzF55Wsi2jHNZVYkSRzI1")
client = weaviate.Client(
    url="https://jobqezyor6kqgxnsyp2aag.c0.us-west3.gcp.weaviate.cloud",
    auth_client_secret=auth_config
)

# GraphQL query to fetch data from GenAI_Video_Transcript class
query = """
{
  Get {
    GenAI_Video_Transcript {
      gakey
      solution
      chunk
      created_date
      time_frame
    }
  }
}
"""

# Execute the query
result = client.query.raw(query)

# Print the retrieved data
if 'data' in result and 'Get' in result['data'] and 'GenAI_Video_Transcript' in result['data']['Get']:
    for record in result['data']['Get']['GenAI_Video_Transcript']:
            print(record)
else:
    print("No data found in the GenAI_Video_Transcript class.")
