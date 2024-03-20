# Copyright 2024 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

.PHONY: all

all:

SHAREDIR	= /usr/share/cros
SHARE_DEST	= $(DESTDIR)$(SHAREDIR)
SERVOD_UTILS	= servod_utils.sh

install:
	@mkdir -p $(SHARE_DEST)
	install -m 0644 $(SERVOD_UTILS) $(SHARE_DEST)/$(SERVOD_UTILS)
