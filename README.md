# Validate email-id using python

###########################################################
Python code using re (regular expression) module in python
use "import re"
###########################################################

A valid email address is required to sign up for an xMatters trial user account. A valid email address consists of an email prefix and an email domain, both in acceptable formats.

The prefix appears to the left of the @ symbol.

The domain appears to the right of the @ symbol.

For example, in the address example@mail.com, "example" is the email prefix, and "mail.com" is the email domain.


Acceptable email prefix format:
  Allowed characters: letters (a-z), numbers, underscores, periods, and dashes.
  An underscore, period, or dash must be followed by one or more letter or number.

Acceptable email domain formats
  Allowed characters: letters, numbers, dashes.
  The last portion of the domain must be at least two characters, for example: .com, .org, .cc
