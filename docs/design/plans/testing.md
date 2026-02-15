# Testing

Testing is the number one priority of v11. With the rise of automated tools like Claude for generating code, it is paramount that we are able to test our games in a completely autonomous way.

Testing is done in English, not other languages. We are not responsible for translations into other languages at this time and only implement our games in English.

For testing, we use [Pytest](https://pypi.org/project/pytest/) and implement three types of test:

There are three main kind of test:
* Unit Test; test a function independently to see its output
* Play Test; test an entire game (usually), playing it from start to finish with bot users and making sure all the messages are correct for each user. For a gameplay test, no actions are called other than start(), then the game is ticked, saved and reloaded at each tick. This rigorously makes sure persistence is working correctly.
* Integration Test; test large chunks of server code at once to make sure pieces work together
