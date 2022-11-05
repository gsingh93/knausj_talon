from talon import Context, Module, actions
from typing import Union

ctx = Context()
mod = Module()
ctx.matches = r"""
tag: user.generic_unix_shell
"""

mod.list("ls_args", "argument mapping for ls command")

ctx.lists["user.ls_args"] = {
    'list': '-l',
    'all': '-a',
}

@mod.action_class
class JoinAction:
    def join_strings(l: Union[str, list[str]], s: str) -> str:
        """Joins the strings using the given separator"""
        return s.join(l)

@ctx.action_class("user")
class Actions:
    # implements the function from generic_terminal.talon for unix shells

    def terminal_change_directory(path: str):
        """Lists change directory"""
        actions.insert(f"cd {path}")
        if path:
            actions.key("enter")

    def terminal_change_directory_root():
        """Root of current drive"""
        actions.insert("cd /")
        actions.key("enter")

    def terminal_clear_screen():
        """Clear screen"""
        actions.insert("clear")
        actions.key("enter")

    def terminal_run_last():
        """Repeats the last command"""
        actions.key("up enter")

    def terminal_rerun_search(command: str):
        """Searches through the previously executed commands"""
        actions.key("ctrl-r")
        actions.insert(command)

    def terminal_kill_all():
        """kills the running command"""
        actions.key("ctrl-c")
        actions.insert("y")
        actions.key("enter")
