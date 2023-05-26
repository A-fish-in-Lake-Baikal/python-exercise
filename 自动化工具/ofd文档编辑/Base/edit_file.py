# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : .py
# @software: pycharm
import asyncio
class EditFile(object):
    def __init__(self):
        pass

    def OpenFile(self,path):
        async def read_file(path):
            async with open(path, 'r') as file:
                content = await file.read()
                print(content)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(read_file('example.txt'))