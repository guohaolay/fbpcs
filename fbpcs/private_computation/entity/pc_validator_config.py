#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict


from dataclasses import dataclass
from typing import Dict, Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class PCValidatorConfig:
    region: str
    pc_pre_validator_enabled: bool = True

    def __str__(self) -> str:
        # pyre-ignore
        return self.to_json()
