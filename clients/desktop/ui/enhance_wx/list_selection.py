"""Selection options shared by the enhanced wx controls."""

from enum import Enum


class FocusAfterDelete(Enum):
    """Where to move focus after deleting an item."""

    PREVIOUS = "previous"
    NEXT = "next"


__all__ = ["FocusAfterDelete"]
