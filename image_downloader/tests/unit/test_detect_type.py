# Copyright 2024 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

import pytest

from image_downloader.tests.fixtures.mock_system import (
    VALID_DRIVE,
    INVALID_DRIVE,
    VALID_LOCAL_BIN,
)


from image_downloader.image_downloader import ImageDownloader
from image_downloader.image_downloader import ImageDownloaderException


class TestCheckUSBStick:
    def test_working_drive(self, monkeypatch, mock_system):

        mock_system()
        downloader = ImageDownloader(VALID_DRIVE, VALID_LOCAL_BIN)
        downloader._check_usb_stick()

    def test_no_drive(self, monkeypatch, mock_system):

        mock_system()
        downloader = ImageDownloader(INVALID_DRIVE, VALID_LOCAL_BIN)
        with pytest.raises(ImageDownloaderException) as pytest_wrapped_e:
            downloader._check_usb_stick()


class TestIsPartitionOf:
    def test_is_partition_of_sd_drive(self):
        assert ImageDownloader._is_partition_of("/dev/sda", "/dev/sda") is True
        assert ImageDownloader._is_partition_of("/dev/sda1", "/dev/sda") is True
        assert ImageDownloader._is_partition_of("/dev/sda12", "/dev/sda") is True
        assert ImageDownloader._is_partition_of("/dev/sdaa", "/dev/sda") is False
        assert ImageDownloader._is_partition_of("/dev/sdaa1", "/dev/sda") is False
        assert ImageDownloader._is_partition_of("/dev/sdb", "/dev/sda") is False

    def test_is_partition_of_nvme_drive(self):
        assert ImageDownloader._is_partition_of("/dev/nvme0n1", "/dev/nvme0n1") is True
        assert ImageDownloader._is_partition_of("/dev/nvme0n1p1", "/dev/nvme0n1") is True
        assert ImageDownloader._is_partition_of("/dev/nvme0n1p10", "/dev/nvme0n1") is True
        assert ImageDownloader._is_partition_of("/dev/nvme0n10", "/dev/nvme0n1") is False
        assert ImageDownloader._is_partition_of("/dev/nvme0n10p1", "/dev/nvme0n1") is False

