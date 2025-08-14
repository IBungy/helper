import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file
from call_function import call_function, available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

def main():
    if len(sys.argv) < 2:
        print("Error: No prompt provided")
        sys.exit(1)
    else:
        verbose = "--verbose" in sys.argv
        prompt_args = []
        for arg in sys.argv[1:]:
            if not arg.startswith("--"):
                prompt_args.append(arg)
        user_prompt = " ".join(prompt_args)
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
        if verbose:
            print(f"User prompt: {user_prompt}")
        response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),)
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        if response.function_calls:
            for function_call in response.function_calls:
                function_response = call_function(function_call, verbose=verbose)
                if function_response and \
                    function_response.parts and \
                    len(function_response.parts) > 0 and \
                    function_response.parts[0].function_response and \
                    function_response.parts[0].function_response.response:
                        result_dict = function_response.parts[0].function_response.response
                        if 'result' in result_dict:
                            print(result_dict['result'])
                        else:
                            print(result_dict)
                else:
                    raise Exception("Malformed function response: expected .parts[0].function_response.response")
        else:
            print(response.text)

        if verbose:
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
