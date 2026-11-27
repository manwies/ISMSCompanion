# SPDX-License-Identifier: AGPL-3.0-only
"""Tests for the security exception hierarchy."""

import pytest

from ismscompanion.core.security import exceptions


@pytest.mark.parametrize("name", exceptions.__all__)
def test_exports_derive_from_crypto_error(name: str) -> None:
    exception_class = getattr(exceptions, name)
    assert issubclass(exception_class, exceptions.CryptoError)


def test_all_lists_every_public_exception() -> None:
    public = {
        name
        for name, obj in vars(exceptions).items()
        if isinstance(obj, type) and issubclass(obj, Exception)
    }
    assert public == set(exceptions.__all__)


def test_base_class_catches_specific_errors() -> None:
    with pytest.raises(exceptions.CryptoError):
        raise exceptions.DecryptionError("authentication failed")
