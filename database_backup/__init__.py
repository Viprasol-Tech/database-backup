"""
database-backup - Backup databases automatically

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import DatabaseBackup, backup, process, main

__all__ = ["DatabaseBackup", "backup", "process", "main"]
