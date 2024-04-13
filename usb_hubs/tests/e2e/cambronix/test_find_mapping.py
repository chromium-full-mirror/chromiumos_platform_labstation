# Copyright 2024 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
# pylint: disable=import-error
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=R0801
# When pylint supports proto better remove
# pylint: disable=no-member

import sys
from unittest.mock import call

import pytest
from usb_hubs.cambrionix.find_mapping import main


class TestFindMapping:
    def test_find_mapping_no_cambrionix(
        self, monkeypatch, mock_host_with_no_cambrionix, capfd
    ):
        mock_host_with_no_cambrionix()

        with monkeypatch.context() as patch:
            patch.setattr(sys, "argv", ["find-cambrionix-mapping"])

            with pytest.raises(SystemExit) as pytest_wrapped_e:
                main()
            out, unused_err = capfd.readouterr()
            assert ("No single Cambrionix hub detected.\n") == out
            assert SystemExit == pytest_wrapped_e.type

    def test_find_mapping_cambrionix(
        self, monkeypatch, mock_host_with_one_cambrionix, capfd
    ):
        host = mock_host_with_one_cambrionix()

        with monkeypatch.context() as patch:
            patch.setattr(sys, "argv", ["find-cambrionix-mapping"])
            main()
            out, unused_err = capfd.readouterr()
            host.mock_open.assert_called_once_with(
                "/usr/local/tmp/usb_hub_mapping.yaml", "w", encoding="utf-8"
            )
            write_calls = [
                call("1"),
                call(":"),
                call(" "),
                call("a"),
                call("\n"),
                call("2"),
                call(":"),
                call(" "),
                call("b"),
                call("\n"),
                call("3"),
                call(":"),
                call(" "),
                call("c"),
                call("\n"),
                call("4"),
                call(":"),
                call(" "),
                call("d"),
                call("\n"),
                call("5"),
                call(":"),
                call(" "),
                call("e"),
                call("\n"),
                call("6"),
                call(":"),
                call(" "),
                call("f"),
                call("\n"),
                call("7"),
                call(":"),
                call(" "),
                call("g"),
                call("\n"),
                call("8"),
                call(":"),
                call(" "),
                call("h"),
                call("\n"),
                call("9"),
                call(":"),
                call(" "),
                call("i"),
                call("\n"),
                call("10"),
                call(":"),
                call(" "),
                call("j"),
                call("\n"),
                call("11"),
                call(":"),
                call(" "),
                call("k"),
                call("\n"),
                call("12"),
                call(":"),
                call(" "),
                call("l"),
                call("\n"),
                call("13"),
                call(":"),
                call(" "),
                call("m"),
                call("\n"),
                call("14"),
                call(":"),
                call(" "),
                call("n"),
                call("\n"),
                call("15"),
                call(":"),
                call(" "),
                call("o"),
                call("\n"),
            ]
            host.mock_open().write.assert_has_calls(calls=write_calls, any_order=False)
            assert ("") == out

    def test_find_mapping_multiple_cambrionix(
        self, monkeypatch, mock_host_with_multiple_cambrionix, capfd
    ):
        mock_host_with_multiple_cambrionix()

        with monkeypatch.context() as patch:
            patch.setattr(sys, "argv", ["find-cambrionix-mapping"])

            with pytest.raises(SystemExit) as pytest_wrapped_e:
                main()
            out, unused_err = capfd.readouterr()
            assert (
                "More than 1 cambrionix hub found panic !!\nNo single Cambrionix hub detected.\n"
            ) == out
            assert SystemExit == pytest_wrapped_e.type
