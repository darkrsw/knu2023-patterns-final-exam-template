# KNU 2023 Design Patterns Final Exam: Detecting all `Builder` patterns.

Your submission must satisfy the following requirements:

* R1. Shall initialize your assignment repository from the url of GitHub Classroom.
* R2. Write your `detector.py` in the repository.
* R3. Test your `detector.py` by using `pytest`.
* R4. You need to let your TA know your repository URL and your student ID together via Slack.
* R5. Check out `test_analyzer1.py` to figure out the output format.
* R6. Assume that there are **NO** overloaded methods and anonymous classes.
* R7. Assume that there are nested directories in the input path.
* R8. The function `collect_uninvoked_methods(...)` takes a path of a directory containing multiple Python source code files, and produces a map. The keys of the map are class names of `Builder` patterns, and the values are a map of `builder methods` and `build methods`, whose values are non-empty sets.
* R9. The key properties of builder patterns include: (1) at least two member methods returning its own types, and (2) at least one member method without any parameters, which returns a certain type.
* Refer to the shape of `Builder` patterns here: https://refactoring.guru/design-patterns/builder
 

## Note:

* N1. `pytest` (based on `test_analyzer1.py`) is just for validating your program. The final grading will be made by other test cases.
* N2. Submissions via GitHub Classroom will only be accepted. Submissions via LMS or any other means are not accepted.
* N3. DO NOT change files in this repository except for `invoke_analyzer.py`. Adding new files are allowed.
* N4. Late submissions after 2:45pm are *NOT* allowed.
