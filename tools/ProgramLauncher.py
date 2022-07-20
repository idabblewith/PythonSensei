# Copyright (c) 2022 Jarid Prince

from days.day_001.main import day_001
from days.day_002.main import day_002
from days.day_003.main import day_003
from days.day_004.main import day_004
from days.day_005.main import day_005
from days.day_006.main import day_006
from days.day_007.main import day_007
from days.day_008.main import day_008
from days.day_009.main import day_009
from days.day_010.main import day_010
import os, sys, traceback, re


class ProgramLauncher():
    def __init__(self, misc):
        self.misc = misc
        self.DAYS = [day_001, day_002, day_003, day_004, day_005, day_006, day_007, day_008, day_009, day_010]
        self.program_id = None
        self.selected = None

# , day21, day22, day23, day24, day25, day26, day27, day28, day29, day30, day31, day32, day33, day34, day35, day36, day37, day38, day39, day40, day41, day42, day43, day44, day45, day46, day47, day48, day49, day50, day51, day52, day53, day54, day55, day56, day57, day58, day59, day60, day61, day62, day63, day64, day65, day66, day67, day68, day69, day70, day71, day72, day73, day74, day75, day76, day77, day78, day79, day80, day81, day82, day83, day84, day85, day86, day87, day88, day89, day90, day91, day92, day93, day94, day95, day96, day97, day98, day99, day100
    def set_program(self, program):
        self.program_id = int(program)
        self.selected = f'day{str(program)}'


    def launch(self):
        print(f'SELECTED: {self.selected}')
        print(f'ID: {str(self.program_id)}')
        try:
            print(f'{self.DAYS[self.program_id - 1]}')
            self.DAYS[self.program_id - 1]()
        except KeyboardInterrupt:
            self.misc.nls("Exiting...")
            sys.exit()
        except Exception as e:
            self.misc.cls()
            self.misc.nls(f"{'*'*20} ERR! {'*'*20}\n")

            dir_path = os.path.dirname(os.path.realpath(__file__))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # excdata = (traceback.extract_tb(exc_tb))
            # excdata = (traceback.print_stack())

            tbLines = traceback.format_exception(*sys.exc_info())
            f = '\n'
            # print(tbLines)
            for l in tbLines[:-1]:
                if l == 'Traceback (most recent call last):\n':
                    #  or l == '  File "D:\\dev\\py100\\tools\\ProgramLauncher.py", line 122, in launch\n    self.DAYS[self.program_id - 1]()\n'
                    pass
                else:
                    l = str(l)
                    l.lstrip().rstrip().replace('\n', '#\n').replace(' ', '')
                    # print(l)

                    f+=l
            f.lstrip().rstrip().replace('\n', 'giggity')
            raw = re.sub(r'File \"D:\\dev\\py100\\tools\\days\\day_0\d+','', f)
            raw = re.sub(r'\\main.py\", ','',raw)
            raw = re.sub(r', in day_0\d+',' in main',raw)
            raw = re.sub(r'\\files\\','',raw)
            raw = re.sub(r'.py\",',' @',raw)

            print(f'{self.misc.bcolors.FAIL}FROM DIRECTORY:\t\t {dir_path}\{fname}@{exc_tb.tb_lineno}{self.misc.bcolors.ENDC}\n')
            print(f'{self.misc.bcolors.FAIL}INFO:\n{raw}{self.misc.bcolors.ENDC}\n')
            print(f"{self.misc.bcolors.HEADER}{exc_type.__name__.upper()}:\t\t {exc_obj}{self.misc.bcolors.ENDC}\n")

