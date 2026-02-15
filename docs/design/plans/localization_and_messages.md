# messages and localization
PlayPalace v11 has the ability to be translated into other languages.
For translation, we use Mozilla Fluent, which is a high quality localization system

It naturally supports clean separation of things into multiple files. We expect this will make it much easier, as languages don't all have to be in one big file.
We suggest one file for each game, and one file for general UI, though we're willing to change this later as needed.

For the purposes of simplicity, prefer to have _self, _target and _other messages where appropriate, to prevent an insane amount of selector overuse.

We use [fluent-compiler](https://pypi.org/project/fluent-compiler/) with one other related dependency: no built in list formatting, so we use Babel for that (babel.lists.format_list). This supports tons and tons of locales and naturally does the two main list conjunctions (and, or).

Games should never have hard-coded strings in them. Instead, render mesages per-user.

We will not be adding pronouns. You have your singular they, and that's all.

## Locale Maintenance

To ensure all locales remain complete:

- **When adding a new game**: Create the English .ftl file, then run `python3 tools/check_locales.py --fix` to copy it to all languages
- **Verification**: The script `server/tools/check_locales.py` checks locale completeness
- **Automated testing**: `server/tests/test_locale_completeness.py` prevents regressions
- **Documentation**: See `server/locales/README.md` for full details

All locale directories must have identical file sets. If a translation doesn't exist yet, English text serves as a placeholder.
