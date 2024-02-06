Code Coverage
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

Code coverage is a metric of how much source code is exercised by your unit test
suite. This can be a good indicator of where you need to add more unit tests, and
keeping your coverage number high can give you some confidence that your code
is correct, and stays correct over time.

How to manage
-------------------------------------------------------------------------------

The GitHub workflow that runs when a new commit is pushed to a pull request, 
will automatically run unit tests and output code coverage into an xml file. 
To easily see if code coverage is changing as a result of new work, you should 
install the GitHub app, Codecov.

* Go to the Codecov app page - https://github.com/apps/codecov
* Click "Configure"
* Select your repository and follow the instructions

On your Codecov repository click "Settings" and under "Tokens" copy the value of
`CODECOV_TOKEN`. Add it as a secret on your GitHub repository and you're all set!

Future pull requests and commits will now include code coverage information. Neato!
