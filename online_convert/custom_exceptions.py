class Error(Exception):
    """Base class for other exceptions"""
    pass


class TooManyRequests(Error):
    """Raised when too many attempts have been made without successful outputs"""
    pass
