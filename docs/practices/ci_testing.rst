Continuous Integration Testing
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

Continuous integration testing is the practice of running a suite of unit tests
against your code base regularly. This should happen whenever new code changes 
are proposed.

There are two main ways this template enables automated unit testing:

1. On all pushes and pull requests. This tests that the new code changes do not 
   cause breakages.
2. A scheduled "smoke test". This primarily tests that upstream dependencies 
   don't introduce breaking changes by pulling those dependencies out of phase 
   with the development cycle.

GitHub workflows are extremely useful, for more information, check out the 
`About workflows <https://docs.github.com/en/actions/using-workflows/about-workflows>`_ page.

How to manage
-------------------------------------------------------------------------------

Notice that this template contains a ``.github/workflows`` directory with a 
``testing-and-coverage.yml`` file. Because of this, any project created from this 
template that uses GitHub as a repository will automatically have CI enabled.

The ``.github/workflows/smoke-test.yml`` file configures the scheduled smoke test.
It uses standard cron notation to start the job at 0645 every day. This time was 
selected to be a little far away from an hour break, when most tests would likely run.

Version culprit
-------------------------------------------------------------------------------

If you want some help tracking down your failures, looking for upstream package
updates is a good place to start. The smoke test has a "List dependencies" stage
that will print out all packages installed through pip and their installed versions.

1. Find the last successful run of the smoke test
   1. github repo -> Actions
   2. "Unit test smoke test"
   3. Scroll until you find a green check
   4. Pick a python versioned build
   6. Cut'n'paste the list to a file, e.g. "pass.txt"
2. Find a failed run.
   1. From the "Unit test smoke test" page, find the first red check
   2. Pick a python versioned build
   4. Cut'n'paste the list to a file, e.g. "fail.txt"
3. Diff those lists
   1. e.g. ``diff pass.txt fail.txt``
   2. Or use an online diff tool like https://www.diffchecker.com/
