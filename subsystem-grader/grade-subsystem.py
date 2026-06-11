from subprocess import run, PIPE
from json import dump, load
from pathlib import Path
from sys import argv

# arguments:
# - results file location (/grade/results/results.json)
# - tests description file (/grade/tests/tests.json)
results_file = Path(argv[1])
tests_file = Path(argv[2])

tests = []
if tests_file.exists():
    with open(tests_file, 'r') as f:
        tests = load(f)

earned_points = 0
max_points = 1

# build the framework including tests, but don't run tests
build_result = run(['./gradlew', '--configuration-cache', 'build', 'testClasses', '-x', 'test'], stdout=PIPE)
print('Build', 'PASS' if build_result.returncode == 0 else 'FAIL')

# build test description
build = {
    'name': 'Build robot code',
    'description': 'Ensure the robot code compiles with your changes.',
    'max_points': 1,
    'output': build_result.stdout.decode()
}

# use return code to determine if the build passed
if build_result.returncode == 0:
    build['points'] = 1
    build['message'] = 'Build passed'
    earned_points += 1
else:
    build['points'] = 0
    build['message'] = 'Build failed'

# run each test already described in the tests_file
for test in tests:
    max_points += 1
    test_result = run(['./gradlew', '--configuration-cache', 'test', '--tests', test['id']], stdout=PIPE)
    print(test['id'], 'PASS' if test_result.returncode == 0 else 'FAIL')
    test['output'] = test_result.stdout.decode()

    # use return code to determine if the build passed
    if test_result.returncode == 0:
        test['points'] = 1
        test['message'] = 'Test passed'
        earned_points += 1
    else:
        test['points'] = 0
        test['message'] = 'Test failed'

# add the compilation test after parsing test list
tests.insert(0, build)

# build test results object
score = earned_points / max_points
results = {
    "gradable": True,
    "score": score,
    "message": "Code graded successfully",
    "output": "",
    "tests": tests
}
print(results)

# create the results directory
results_file.parent.mkdir(parents=True, exist_ok=True)

# write test results to results_file
with open(results_file, 'w') as f:
    dump(results, f)

print(f'Total score: {int(100 * score)}%')
