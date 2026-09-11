class WelpError(Exception):
    """Base class for Welp errors."""

class ConfigurationError(WelpError):
    """Invalid or missing configuration."""

class ProviderError(WelpError):
    """Blockchain provider failure."""

class UnsupportedChainError(WelpError):
    """Unknown chain."""
