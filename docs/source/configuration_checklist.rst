Configuring a new project
===============================================================================

So you've created a new python project from the template! Great!

Now let's get other services linked up to your new project to make the most of
what the template and open source CI has to offer!

Configure your GitHub repository for safety and security
-------------------------------------------------------------------------------

* Consider setting up branch protection rules.

  * `GitHub Instructions for protected branches <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-pull-request-reviews-before-merging>`_
  * This will help ensure your code is always ready to deploy by running all tests
    pass to merging into the ``main`` branch.

* Enable ``dependabot`` for your new repository

  * `GitHub Instructions for dependabot <https://docs.github.com/en/code-security/getting-started/securing-your-repository#managing-dependabot-security-updates>`_
  * There are several different features that ``dependabot`` offers to keep your dependencies
    up to date and your code secure. It's as easy as clicking a checkbox to get started.

* Add another GitHub user as an administrator on your repository

  * `GitHub Instructions for repo access <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository>`_
  * It's just a good idea - like having a spare set of keys for your Lamborghini.

Configure your GitHub repository for convenience
-------------------------------------------------------------------------------

There are several convenient options in GitHub that are not enabled by default.
We find ourselves setting these options on all our development repositories, and 
list them here for reference.

In your repo, "Settings" tab, "General" page, scroll down to the "Pull Requests" 
section:

* Check **"Allow squash merging"**. This lets you combine several intermediate
  commits on a development branch into a single merge into main. The merge
  history will stay cleaner.
* Check **"Allow auto-merge"**. This lets you set a pull request to automatically
  merge when all required reviews and status criteria is met. This can be
  great when working with folks in other time zones - you don't need to be 
  around to merge your change once it's ready.
* Check **"Automatically delete head branches"**. If you're working in development
  branches and only merging in to main with pull requests (which you should do!), 
  your repo may quickly fill up with stale development branches. With
  this feature enabled, your development branches will be automatically deleted
  once the pull requests are merged into main.


Get the most out of this template
-------------------------------------------------------------------------------

- `Finish setting up benchmarks <https://lincc-ppt.readthedocs.io/en/latest/practices/ci_benchmarking.html#set-up>`_
- `Set up smoke test email notifications <https://lincc-ppt.readthedocs.io/en/latest/practices/ci_testing.html#email-notifications>`_
- `Set up smoke test slack notifications <https://lincc-ppt.readthedocs.io/en/latest/practices/ci_testing.html#slack-notifications>`_
- `Set up code coverage with codecov <https://lincc-ppt.readthedocs.io/en/latest/practices/code_coverage.html#how-to-manage>`_
- `Set up a PyPI package <https://lincc-ppt.readthedocs.io/en/latest/practices/pypi.html#set-up>`_
- `Set up a conda-forge package <https://lincc-ppt.readthedocs.io/en/latest/practices/conda.html#set-up>`_
- `Connect your project to ReadTheDocs <https://lincc-ppt.readthedocs.io/en/latest/practices/sphinx.html#how-to-get-started-with-readthedocs>`_

Still have questions?
-------------------------------------------------------------------------------

:doc:`/source/contact`