import sys
from collections import OrderedDict

from knack import CLI, ArgumentsContext, CLICommandsLoader
from knack.commands import CommandGroup

# get creds from env
# if the person is not capable of doing that
# they should not be using this tool

def abc_str(length=3):
    import string
    return string.ascii_lowercase[:length]


class MyCommandsLoader(CLICommandsLoader):
    def load_command_table(self, args):
        with CommandGroup(self, 'abc', '__main__#{}') as g:
            g.command('str', 'abc_str')
        return OrderedDict(self.command_table)

    def load_arguments(self, command):
        with ArgumentsContext(self, 'abc str') as ac:
            ac.argument('length', type=int)
        super(MyCommandsLoader, self).load_arguments(command)


mycli = CLI(cli_name='mycli', commands_loader_cls=MyCommandsLoader)
exit_code = mycli.invoke(sys.argv[1:])
sys.exit(exit_code)

# $ python mycli.py abc str
# "abc"

# $ python mycli.py abc str --length 5
# "abcde"

# $ python mycli.py abc str --length 100
# "abcdefghijklmnopqrstuvwxyz"
