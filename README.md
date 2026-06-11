# prairielearn-graders

Custom grader images developed for PrairieLearn

## subsystem-grader

This image has a copy of [systemcore_framework](https://github.com/fruzyna/systemcore_framework) pre-cloned and built.
On execution it copies the student provided files in `/grade/student` to the robot `subsystem` package and the tests in `/grade/tests` to the gradle `src/test/java` directory.
The tests directory should also include a `tests.json` which contains an array of test descriptions like the following example.
```
[
    {
        "id": "TestHelloWorld.testHelloWorld",
        "name": "Hello world test",
        "description": "Test that \"Hello world!\" is returned.",
        "max_points": 1
    }
]
```
The grader then compiles the code with the tests and student answer and reports that as a test result.
Finally, the grader executes each of the specified tests and adds them to the results.

## Building Images

```
podman build -t [tag_name] [image_dir]
```

## Testing Local Images

```
podman run -it -v ./grade:/grade:Z --rm [tag_name]
```
