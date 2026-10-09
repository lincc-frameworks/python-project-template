Development Guide Files
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

Development guide files are markdown files that can be used by both humans and AI agents to provide guidance on development practices within a project. They can explain high level design decisions, help ensure consistency, and describe the best practices used throughout the project. When used in combination with AI agents, these files can both optimize the development workflow (by providing overviews) and assist in maintaining high code quality standards.

Developers should extend this file and add information as the project progresses to capture the current state of both the code and the best practices.


Common Sections
-------------------------------------------------------------------------------

We recommend including sections on the following topics:

- Overview of the project, including how it is structured, its main components, and how it will be used.
- Design "North Stars" (key guiding principles for the project's development)
- How to set up the development environment
- How to run tests and linting (common commands)
- Repository structure (especially for projects with subdirectories)
- Coding standards and style guidelines
- Project specific considerations such as default units.

Default Information
-------------------------------------------------------------------------------

The default DEVELOPMENT_GUIDE.md file is generated with recommendations and principles corresponding to the Python Project Template.

For example, the default "North Stars" provided are:
- Correctness is the Top Priority.
- Code should be modular and use a few consistent APIs.
- Make Easy Things Easy, Hard Things Possible.
- Code should follow a standard format.
- Code should be documented.

Developers should edit any of the information in the DEVELOPMENT_GUIDE.md file to reflect their design goals and philosophy.
