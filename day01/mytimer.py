import time as t


class MyTimer:
    #开始计时
    def start(self):
        self.start = t.localtime()
        print('开始计时')

    # 停止计时
    def stop(self):
        self.stop = t.localtime()
        print('停止计时')
