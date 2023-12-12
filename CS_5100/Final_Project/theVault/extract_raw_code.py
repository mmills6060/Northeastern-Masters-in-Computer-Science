from codetext.utils import parse_code
from codetext.parser import PythonParser
import utils
code_snippet = """
def sum2num(a: int, b: int):
  '''
  :param a: first number
  :param b: second number
  '''
  return a + b # result
"""
code_tree = parse_code(code_snippet, 'cpp')

res = process_raw_node(
    tree=code_tree, 
    blob=code_snippet,
    language_parser=PythonParser(),
    metadata={'repo': 'test'}  # Optional
)

# or extrating line

res = get_line_definitions(
    tree=code_tree, 
    blob=code_snippet,
    language_parser=PythonParser(),
    source_metadata={'repo': 'test'}  # Optional
)

