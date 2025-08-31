from pydantic import BaseModel
from cforma import StructFormatter


# 1. Define your Pydantic model
class UserProfile(BaseModel):
    name: str
    age: int


# 2. Convert it to a schema for your LLM
llm_schema = StructFormatter.ingest(
    schemaName="UserProfileSchema",
    schemaDescription="A schema for a user profile.",
    schemaObject=UserProfile,
)

# 3. Use `llm_schema` in your API call
# response = client.chat.completions.create(..., extra_body={"response_format": llm_schema})
