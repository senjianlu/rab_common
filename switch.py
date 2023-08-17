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
try:
    from external.rab_common import logger as external_rab_common_logger
except Exception as e:
    import logger as external_rab_common_logger


# Switch 相关配置
SWITCH_CONFIG = external_rab_common_config.CONFIG["external"]["rab_common"]["switch"]
# 日志记录
LOGGER = external_rab_common_logger.LOGGER


def get_base():
    """
    @description: 获取基础启动开关
    @param {type}
    @return: 基础路径
    """
    return SWITCH_CONFIG["base"]

def check_base(index: int, switch_name: str, switch_desc: str):
    """
    @description: 检查基础启动开关
    @param {type}
    @return: 基础路径
    """
    # 1. 检查是否存在
    if switch_name not in get_base():
        # 红色字体
        LOGGER.error("\033[31m === 基础功能 {} 错误：未知的开关 {}！ === \033[0m".format(index, switch_name))
        return False
    # 2. 检查是否开启
    if not get_base()[switch_name]:
        LOGGER.info("\033[30;47m === 基础功能 {} 关闭：无需{}！ === \033[0m".format(index, switch_desc))
        return False
    # 3. 返回
    LOGGER.info("\033[32;47m === 基础功能 {} 开启：开始{}... === \033[0m".format(index, switch_desc))
    return True

def get_optional():
    """
    @description: 获取可选启动开关
    @param {type}
    @return: 可选路径
    """
    return SWITCH_CONFIG["optional"]

def check_optional(index: int, switch_name: str, switch_desc: str):
    """
    @description: 检查可选启动开关
    @param {type}
    @return: 可选路径
    """
    # 1. 检查是否存在
    if switch_name not in get_optional():
        # 红色字体
        LOGGER.error("\033[31m === 可选功能 {} 错误：未知的开关 {}！ === \033[0m".format(index, switch_name))
        return False
    # 2. 检查是否开启
    if not get_optional()[switch_name]:
        LOGGER.info("\033[30m === 可选功能 {} 关闭：无需{}！ === \033[0m".format(index, switch_desc))
        return False
    # 3. 返回
    LOGGER.info("\033[32m === 可选功能 {} 开启：开始{}... === \033[0m".format(index, switch_desc))
    return True


# 单体测试
if __name__ == "__main__":
    pass