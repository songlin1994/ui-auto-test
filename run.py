
"""
运行用例集：
    python3 run.py
# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'
"""

import pytest

from Common import Log
from Common import Shell
# from Conf import Config

if __name__ == '__main__':
    # conf = Config.Config()
    log = Log.MyLog()

    shell = Shell.Shell()

    xml_report_path = './Report/xml/'
    html_report_path = './Report/html/'


    pytest.main(['-s', '-q', '--alluredir',xml_report_path,'./TestCase/mall'])

    cmd = "allure generate %s -o %s --clean"%(xml_report_path,html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise
