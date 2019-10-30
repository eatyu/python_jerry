#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time


class MyThread(threading.Thread):
    # 这个箭头只是提示该函数 输入参数 和 返回值 的数据类型
    # 方便程序员阅读代码的。
    def run(self) -> None:
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)


def main():
    print("Start main threading")

    # 创建三个线程
    threads = [MyThread() for i in range(3)]
    # 启动三个线程
    for t in threads:
        t.start()

    print("\nEnd Main threading")


if __name__ == '__main__':
    main()
