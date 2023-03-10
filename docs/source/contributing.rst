Contributing to the template
===============================================================================

Find (or make) a new GitHub issue
-------------------------------------------------------------------------------

Add yourself as the assignee on an existing issue so that we know who's working on what. ( If you're not actively working on an issue, unassign yourself 😉 )

If there isn't an issue for the work you want to do, please create one and include a description - it's just polite.

You can reach the team with bug reports, feature requests, and general inquiries by creating a new GitHub issue.

Create a branch
-------------------------------------------------------------------------------

It is preferable that you create a new branch with a name like ``issue/##/<short-description>``. GitHub makes it pretty easy to associate branches and tickets, but it's nice when it's in the name.

Testing the template
-------------------------------------------------------------------------------

Testing can be tricky. The current best way is to clone this repository locally, and use Copier to generate a test project locally, then verify your expected results.

Copier will look for git tags to determine which version of the template to use. You probably don't want to create new tags while you're working on the template. Create a test project using the following command to let Copier know to use the latest local version.

.. code-block:: bash

    >> copier --vcs-ref HEAD </local/path/to/template> </test/project/directory>

Notes:

1. Any changes to the template will need to be committed (not pushed) to be picked up by Copier.
2. If there's an opportunity for introducing an automated test, please take it.
3. This project has some automated testing, to ensure that the template can hydrate a reasonable output project - feel free to extend that if it's reasonable.
4. See the `Copier documentation <https://copier.readthedocs.io/en/latest/generating/#regenerating-a-project>`_ for more information.


Create your PR
-------------------------------------------------------------------------------

Please use PR best practices, and get someone to review your code.

Optional - Release a new version
-------------------------------------------------------------------------------

Once your PR is merged you should create a new release to make your changes available. 
GitHub's `instructions <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository>`_ for doing so are here. 
Use your best judgement when incrementing the version. i.e. is this a major, minor, or patch fix.