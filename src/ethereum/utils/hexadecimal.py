"""
Utility Functions For Hexadecimal Strings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..contents:: Table of Contents
    :backlinks: none
    :local:

Introduction
------------

Hexadecimal strings specific utility functions used in this specification.
"""
from ethereum.base_types import U256, Bytes, Bytes8, Bytes32, Uint
from ethereum.crypto import Hash32
from ethereum.frontier.eth_types import Address, Bloom, Root


def has_hex_prefix(hex_string: str) -> bool:
    """
    Check if a hex string starts with hex prefix (0x).

    Parameters
    ----------
    hex_string :
        The hexadecimal string to be checked for presence of prefix.

    Returns
    -------
    has_prefix : `bool`
        Boolean indicating whether the hex string has 0x prefix.
    """
    return hex_string.startswith("0x")


def remove_hex_prefix(hex_string: str) -> str:
    """
    Remove 0x prefix from a hex string if present. This function returns the
    passed hex string if it isn't prefixed with 0x.

    Parameters
    ----------
    hex_string :
        The hexadecimal string whose prefix is to be removed.

    Returns
    -------
    modified_hex_string : `str`
        The hexadecimal string with the 0x prefix removed if present.
    """
    if has_hex_prefix(hex_string):
        return hex_string[len("0x") :]

    return hex_string


def hex_to_bytes(hex_string: str) -> Bytes:
    """
    Convert hex string to bytes.

    Parameters
    ----------
    hex_string :
        The hexadecimal string to be converted to bytes.

    Returns
    -------
    byte_stream : `bytes`
        Byte stream corresponding to the given hexadecimal string.
    """
    return bytes.fromhex(remove_hex_prefix(hex_string))


def hex_to_bytes8(hex_string: str) -> Bytes8:
    """
    Convert hex string to 8 bytes.

    Parameters
    ----------
    hex_string :
        The hexadecimal string to be converted to 8 bytes.

    Returns
    -------
    8_byte_stream : `bytes`
        8-byte stream corresponding to the given hexadecimal string.
    """
    return Bytes8(bytes.fromhex(remove_hex_prefix(hex_string).rjust(16, "0")))


def hex_to_bytes32(hex_string: str) -> Bytes32:
    """
    Convert hex string to 32 bytes.

    Parameters
    ----------
    hex_string :
        The hexadecimal string to be converted to 32 bytes.

    Returns
    -------
    32_byte_stream : `bytes`
        32-byte stream corresponding to the given hexadecimal string.
    """
    return Bytes32(bytes.fromhex(remove_hex_prefix(hex_string).rjust(64, "0")))


def hex_to_hash(hex_string: str) -> Hash32:
    """
    Convert hex string to hash32 (32 bytes).

    Parameters
    ----------
    hex_string :
        The hexadecimal string to be converted to hash32.

    Returns
    -------
    hash : `Hash32`
        32-byte stream obtained from the given hexadecimal string.
    """
    return Hash32(bytes.fromhex(remove_hex_prefix(hex_string)))


def hex_to_root(hex_string: str) -> Root:
    """
    Convert hex string to trie root.

    Parameters
    ----------
    hex_string :
        The hexadecimal string to be converted to trie root.

    Returns
    -------
    root : `Root`
        Trie root obtained from the given hexadecimal string.
    """
    return Root(bytes.fromhex(remove_hex_prefix(hex_string)))


def hex_to_bloom(hex_string: str) -> Bloom:
    """
    Convert hex string to bloom.

    Parameters
    ----------
    hex_string :
        The hexadecimal string to be converted to bloom.

    Returns
    -------
    bloom : `Bloom`
        Bloom obtained from the given hexadecimal string.
    """
    return Bloom(bytes.fromhex(remove_hex_prefix(hex_string)))


def hex_to_address(hex_string: str) -> Address:
    """
    Convert hex string to Address (20 bytes).

    Parameters
    ----------
    hex_string :
        The hexadecimal string to be converted to Address.

    Returns
    -------
    address : `Address`
        The address obtained from the given hexadecimal string.
    """
    return Address(bytes.fromhex(remove_hex_prefix(hex_string).rjust(40, "0")))


def hex_to_uint(hex_string: str) -> Uint:
    """
    Convert hex string to Uint.

    Parameters
    ----------
    hex_string :
        The hexadecimal string to be converted to Uint.

    Returns
    -------
    converted : `Uint`
        The unsigned integer obtained from the given hexadecimal string.
    """
    return Uint(int(remove_hex_prefix(hex_string), 16))


def hex_to_u256(hex_string: str) -> U256:
    """
    Convert hex string to U256.

    Parameters
    ----------
    hex_string :
        The hexadecimal string to be converted to U256.

    Returns
    -------
    converted : `U256`
        The U256 integer obtained from the given hexadecimal string.
    """
    return U256(int(remove_hex_prefix(hex_string), 16))