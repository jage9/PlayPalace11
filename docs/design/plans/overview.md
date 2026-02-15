# PlayPalace V11; Overview
The intention in this file is to outline the main design decisions we are considering in the development of PlayPalace V11, and why we have made those decisions.

For further clarification or information on each component of v11, please see its respective file.

# Background And History
The first online version of PlayPalace was v9, which was further improved and updated until v10.

The client for this version will be re-used in v11; I see no problem with this. It is built in Python with wx as a UI, and it works pretty well for everything we need it to do.

There are a few reasons I want to do v11, and they are:
* V10 had no automated testing whatsoever. This was a big problem, especially considering we make extensive use of AI to help us code faster. See testing.md for our plans to solve this.
* In v10, games were designed with coroutines as a deep part of the simulation. This makes the code flow more linearly, but the fact of the matter is: most games do not actually flow linearly at all. Consequences and solutions to this problem are outlined in simulation.md
* v10 had no localization at all. This isn't something I absolutely need, but code-wise it's not a hard problem to solve if you do things right - so we're solving it in v11. See messages-and-localization.md
* v10 had no persistence whatsoever. This is something I intend on solving in v11, as it's also a fairly trivial problem if you code things right. see persistence.md
* v10 had a lot of features in the core when they ought to have been in the games themselves. This is still an unsolved problem that we need to discuss before v11 can start!
* v10 did not have a standard UI system, beyond menus (which themselves were riddled with issues). That's not good enough, and I have lots of ideas for how to solve it in v11, *while* sticking to our traditional menu-based system. See ui.md
