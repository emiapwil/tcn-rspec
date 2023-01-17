from lark import Lark
import cmd

class Shell(cmd.Cmd):
    prompt = "> "

    def set_parser(self, parser):
        self.parser = parser

    def do_ci(self, argline):
        t = parser.parse(argline)
        print(t.pretty())

    def do_c(self, argline):
        with open(argline, 'r') as f:
            t = parser.parse(f.read())
            print(t.pretty())

    def do_exit(self, argline):
        return True

if __name__ == '__main__':
    import sys

    lark_file = sys.argv[1]
    with open(lark_file, 'r') as f:
        parser = Lark(f.read())

    if len(sys.argv) == 1:
        shell = Shell()
        shell.set_parser(parser)
        shell.cmdloop()
    else:
        for spec in sys.argv[2:]:
            with open(spec, 'r') as f:
                t = parser.parse(f.read())
                print(t.pretty())
