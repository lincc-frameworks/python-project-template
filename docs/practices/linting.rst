Linting
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

Linting is a form of static program checking, meaning that it analyzes code without running it.

A linter checks code for code errors, violations of some agreed-upon coding standards, or gives its opinion on code smells. A "code smell" is when something isn't exactly **wrong**, but could be an indicator that your code is inefficient or could be refactored to be cleaner.

When code is reliably run through a linter, then code reviewers can assume that the code they're looking at adheres to that agreed-upon coding standard. 
A code reviewer won't be distracted by improper spacing, and can focus their reviewing effort on the meat of the code.

There are two main linters suggested by this template: pylint and black. While they have a lot of the same opinions, we recommend picking a single standard for your project and sticking to it. If some folks use one linter, this may cause undue churn in your source files as each developer creates some formatting changes each time they touch a file (and then another developer undoes them the next time they touch the same file).


How to modify/remove
-------------------------------------------------------------------------------

TODO