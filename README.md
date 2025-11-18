# Homework 
- Name: Cristhian Alvarenga

## Question 1) Define the following unit, integration, regression tests and when you would use each?

 - Unit test: A unit test is a test that verifies a small piece of code. Something like a single function, class, or method.
We use unit tests during development to make sure that individual components work like they’re supposed to.

- Integration test: The integration test verifies that multiple parts of a system work together correctly. 
We use integration tests to confirm two or more components, like a function that calls another function.

- Regression test: The regression test is written to catch specific bugs that may have been found previously and fixed, 
making sure that the bug doesn’t reappear in future code changes. We use regression tests immediately after fixing a bug.

## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is. 

Pytest discovery by default looks for files that start with test_ or end with _test.py in the current directory and subdirectories. 
Within those files pytest looks for a function that starts with test_. Classes also must start with Test and contain methods that start with test_. 
Thats how pytest automatically finds and runs our tests. 

Fixtures are functions that pytest runs before our actual test functions. They are used to set up a baseline state
 for the test environment. This is for reusability and to help manage setup/teardown logic. 
