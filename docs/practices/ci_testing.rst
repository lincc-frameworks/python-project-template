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