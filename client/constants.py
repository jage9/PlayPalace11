"""Shared client constants."""

USERNAME_MIN_LENGTH = 3
USERNAME_MAX_LENGTH = 32
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 128

USERNAME_LENGTH_HINT = f"Usernames must be {USERNAME_MIN_LENGTH}-{USERNAME_MAX_LENGTH} characters."
PASSWORD_LENGTH_HINT = f"Passwords must be {PASSWORD_MIN_LENGTH}-{PASSWORD_MAX_LENGTH} characters."
DEFAULT_CREDENTIAL_HINT = (
    f"Default credential policy: usernames {USERNAME_MIN_LENGTH}-{USERNAME_MAX_LENGTH} chars, "
    f"passwords {PASSWORD_MIN_LENGTH}-{PASSWORD_MAX_LENGTH} chars (server admins may override)."
)
