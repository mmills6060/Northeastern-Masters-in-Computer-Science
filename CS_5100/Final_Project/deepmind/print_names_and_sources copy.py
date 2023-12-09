import io
import sys



def _all_problems(filenames):
  """Iterates through all ContestProblems in filenames."""
  for filename in filenames:
    with open(filename, 'rb') as f:
      reader = io.BufferedReader(f)
      for serialized_problem in reader:
        problem = contest_problem_pb2.ContestProblem()
        problem.ParseFromString(serialized_problem)
        yield problem


def _print_names_and_sources(filenames):
  """Prints the names and sources of all ContestProblems in filenames."""
  for problem in _all_problems(filenames):
    print(
        contest_problem_pb2.ContestProblem.Source.Name(problem.source),
        problem.name)


if __name__ == '__main__':
  _print_names_and_sources(sys.argv[1:])
