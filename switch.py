#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/rab_common/switch.py
# @DATE: 2023/08/17 周四
# @TIME: 20:29:54
#
# @DESCRIPTION: 开始控制器


import os
# 涉及到路径问题的导入
try:
    from external.rab_common import config as external_rab_common_config
except Exception as e:
    import config as external_rab_common_config


# Switch 相关配置
SWITCH_CONFIG = external_rab_common_config.CONFIG["external"]["rab_common"]["switch"]


def get_base():
    """
    @description: 获取基础启动开关
    @param {type}
    @return: 基础路径
    """
    return SWITCH_CONFIG["base"]

def get_optional():
    """
    @description: 获取可选启动开关
    @param {type}
    @return: 可选路径
    """
    return SWITCH_CONFIG["optional"]
