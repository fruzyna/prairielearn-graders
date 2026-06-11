#!/bin/bash

DATA_DIR="/grade/data"
RESULTS_DIR="/grade/results"
COURSE_DIR="/grade/serverFilesCourse"
STUDENT_DIR="/grade/student"
TESTS_DIR="/grade/tests"
GRADER_DIR="/grader"

# move tests and submitted code into framework
cp -r $TESTS_DIR $GRADER_DIR/src/test/java
cp $STUDENT_DIR/*.java $GRADER_DIR/src/main/java/org/wildstang/po27/subsystem/

python3 grade-subsystem.py "$RESULTS_DIR/results.json" "$TESTS_DIR/tests.json"
