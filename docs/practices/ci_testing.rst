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
   5. Expand "List dependencies"
   6. Cut'n'paste the list to a file, e.g. "pass.txt"
2. Find a failed run.
   1. From the "Unit test smoke test" page, find the first red check
   2. Pick a python versioned build
   3. Expand "List dependencies"
   4. Cut'n'paste the list to a file, e.g. "fail.txt"
3. Diff those lists
   1. e.g. ``diff pass.txt fail.txt``
   2. Or use an online diff tool like https://www.diffchecker.com/

Smoke test notifications
-------------------------------------------------------------------------------

The smoke test is only useful if someone notices that the test has failed, and 
looks into the nature of the failure. This can be tricky with github, as a 
worfklow failure will, by default, only notify the maintainer who added the
workflow file to the repo.

The template supports two types of notifications: email or slack. If you 
choose slack, some additional configuration is necessary.

Create a Slack App
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You'll need to create a Slack app. It's not as scary as it sounds!
It will have certain permissions to post to particular channels, and will have
an associated webhook URL that we'll use to send messages from GitHub to the app. 

See `Slack's official documentation <https://api.slack.com/start/quickstart>`_ 
for setting up an app. We really only need steps 1 and 5, summarized below:

- `Step 1 <https://api.slack.com/start/quickstart#creating>`_: Create an app
  from scratch. The ``App Name`` you select here will appear in the slack
  notificationw we create later, so use something descriptive enough, like:

   - <my project> Slack Bot
   - <my project> CI Reporter

- `Step 5 <https://api.slack.com/start/quickstart#webhooks>`_: Add a new
  webhook and you'll give it permission to post to a specific slack channel.
  Copy the webook URL.

Github workflow step to post to webhook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now you'll need to configure each project repo to send slack messages.

In your project repo create a new repo secret:
  - "Settings"
  - "Secrets and variables" > "Actions"
  - "Repository Secrets" > "New repository secret"
  - Name: ``SLACK_WEBHOOK_URL``
  - Secret: paste the URL that was copied in the previous step
  - "Add secret"

There is a stage in the end of the ``smoke_test.yml`` file that will
send failure alerts to the slack channel.

An example can be found in the `rail project <https://github.com/LSSTDESC/rail/blob/main/.github/workflows/smoke-test.yml#L45-L82>`_