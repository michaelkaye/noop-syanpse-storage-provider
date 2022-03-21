import logging

from synapse.logging.context import LoggingContext
from synapse.rest.media.v1.storage_provider import StorageProvider

# Synapse 1.13.0 moved current_context to a module-level function.
try:
    from synapse.logging.context import current_context
except ImportError:
    current_context = LoggingContext.current_context

logger = logging.getLogger("synapse.noopstorage")

class NoopStorageProviderBackend(StorageProvider):
    """
    Args:
        hs (HomeServer)
        config: The config returned by `parse_config`
    """

    def __init__(self, hs, config):
        logger.info("Init noop storage provider")

    def store_file(self, path, file_info):
        """See StorageProvider.store_file"""
        logger.info("Stored file into the void")
	return

    def fetch(self, path, file_info):
        """See StorageProvider.fetch"""
        logger.info("Fetching file from the void")
        return None

    @staticmethod
    def parse_config(config):
        """Called on startup to parse config supplied. This should parse
        the config and raise if there is a problem.
        """
        logger.info("Parsing config for noop storage provider")
        sample = config["sample"]
        result = {
            "sample": sample,
        }
        return result
