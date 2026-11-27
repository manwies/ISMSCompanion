# SPDX-License-Identifier: AGPL-3.0-only
"""Tests for the cryptographic configuration module."""

from dataclasses import FrozenInstanceError

import pytest

from ismscompanion.core.security.crypto_config import (
    CryptoConfig,
    crypto_config,
    validate_config,
)


def test_validate_config_accepts_defaults() -> None:
    validate_config()


def test_defaults_meet_owasp_minimums() -> None:
    assert crypto_config.PBKDF2_ITERATIONS >= 600_000
    assert crypto_config.ARGON2_MEMORY_COST >= 65536
    assert crypto_config.ARGON2_TIME_COST >= 2
    assert crypto_config.MIN_PASSWORD_LENGTH >= 12


def test_key_and_nonce_sizes() -> None:
    assert crypto_config.SALT_SIZE == 32
    assert crypto_config.AES_KEY_SIZE == 32
    assert crypto_config.CHACHA_KEY_SIZE == 32
    assert crypto_config.AES_NONCE_SIZE == 12
    assert crypto_config.CHACHA_NONCE_SIZE == 12


@pytest.mark.parametrize(
    ("attribute", "weak_value", "message"),
    [
        ("PBKDF2_ITERATIONS", 599_999, "PBKDF2 iterations too low"),
        ("ARGON2_MEMORY_COST", 65535, "Argon2 memory cost too low"),
        ("ARGON2_TIME_COST", 1, "Argon2 time cost too low"),
    ],
)
def test_validate_config_rejects_weak_parameters(
    monkeypatch: pytest.MonkeyPatch, attribute: str, weak_value: int, message: str
) -> None:
    monkeypatch.setattr(CryptoConfig, attribute, weak_value)
    with pytest.raises(ValueError, match=message):
        validate_config()


@pytest.mark.parametrize(
    ("attribute", "minimum"),
    [
        ("PBKDF2_ITERATIONS", 600_000),
        ("ARGON2_MEMORY_COST", 65536),
        ("ARGON2_TIME_COST", 2),
    ],
)
def test_validate_config_accepts_exact_minimums(
    monkeypatch: pytest.MonkeyPatch, attribute: str, minimum: int
) -> None:
    monkeypatch.setattr(CryptoConfig, attribute, minimum)
    validate_config()


def test_config_instance_is_immutable() -> None:
    with pytest.raises(FrozenInstanceError):
        crypto_config.SALT_SIZE = 16  # type: ignore[misc]
