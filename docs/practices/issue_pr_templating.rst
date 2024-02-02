Issue and Pull Request Templates
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

Issues and Pull Requests form the core of developer-community communication
regarding identified problems/requested features and their implementation in
a given software package. The main function of templates, is to provide
guidelines on the content of these, usually focused on ensuring a given
user/developer provides enough context in a given issue/pull request (PR) for 
others to understand the motivation and technical details.

Issue Templates
-------------------------------------------------------------------------------

Issue templates are highly customizable, and it's often appropriate to have
multiple available to users to promote better organization of common issue
types. By default, the python-project-template provides three base templates

- **general-issue-template**: A general issue template for issues that don't 
fit into other categories
- **bug-report-template**: A template specific to identifying bugs within the
package
- **feature-request-template**: A template for requesting new features of the
package

A user will be prompted to choose between these templates any time they attempt
to create a new issue in the repository. You may add to new templates to this 
list as additional common issue themes become clear in your project.

Modifying using the Github Web-Interface
...............................................................................
Github offers native support for adding and modifying issue templates directly
in it's web-interface. This is done within the settings menu, and Github has a
straightforward guide on how to access this interface, 
`here <https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository>`

Changing Template Ordering
...............................................................................
The ordering of issue templates is controlled by alpha-numeric names of the
template files themselves. To best control ordering, it's recommended to prefix
the template files with a number (e.g. ``0-first_template.md``, 
``1-second_template.md``, etc.). This is also covered in it's own section of
the `github issue templating guide <https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#changing-the-order-of-templates>`.

.. note::
    The issue template files can be found in the ``.github/ISSUE_TEMPLATE`` 
    subdirectory of your repository.

Pull Request Template
-------------------------------------------------------------------------------

A pull request template is used to pre-populate any submitted PRs to the
repository. By default, the python-project-template provides a single template
to the project (located at ``.github/pull_request_template.md``). This template
provides generic fields for:

- **Change Description**: Prompt for overview of what the PR changes
- **Solution Description**: Prompt for technical details of the solution
- **Code Quality**: Checkboxes to verify that the PR adheres to the coding
standards of the repository

As well as a set of additional project and issue-specific fields. This template
only serves as an initial framework, and you should feel free to modify this as
you see fit by directly modifying the template file.