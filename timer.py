import datetime

t1 = datetime.datetime.now()
import subprocess

subprocess.run(args=["dist/qt.exe"])
t2 = datetime.datetime.now()
duration = t2 - t1

import rich
rich.print(f"[green]program tooked [red]{duration.total_seconds()}[/red]s[/green]")
