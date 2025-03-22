from typing import Any
from mcp.server.fastmcp import FastMCP
# import mcp.types as types

mcp = FastMCP("prompts")

@mcp.prompt()
def bedtime_story(subject: str) -> str:
    if subject == "":
        message = "Tell me a sci-fi bedtime story"
    else:
        message = f"Tell me a bedtime story about {subject}"

    return message

# mcp = Server("prompts")

# PROMPTS = {
#     "bedtime-story": types.Prompt(
#         name="bedtime-story",
#         description="Read a bedtime story",
#         arguments=[
#             types.PromptArgument(
#                 name="subject",
#                 description="Subject that story should be about",
#                 required=False
#             )
#         ]
#     )
# }

# @mcp.list_prompts()
# async def list_prompts() -> list[types.Prompt]:
#     return list(PROMPTS.values())

# @mcp.get_prompt()
# async def get_prompt(
#     name: str,
#     arguments: dict[str, str] | None = None
# ) -> types.GetPromptResult:
#     if name not in PROMPTS:
#         raise ValueError(f"The following prompt could not be found: {name}")
    
#     if name == "bedtime-story":
#         subject = arguments.get("subject") if arguments else ""

#     if subject == "":
#         messageText = "Tell me a sci-fi bedtime story"
#     else:
#         messageText = f"Tell me a bedtime story about {subject}"

#     return types.GetPromptResult(
#         messages=[
#             types.PromptMessage(
#                 role="user",
#                 content=types.TextContent(
#                     type="text",
#                     text=messageText
#                 )
#             )
#         ]
#     )

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')