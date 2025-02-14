import sys
import platform
from datetime import datetime, timezone

print("here is python version")
print(sys.version)
print(sys.version_info)


#Using Platform
print("using plaform import")
print(str(platform.python_version_tuple()))

#Current DateTime Display
print("Current date and time : ")
curr_dt = str(datetime.now(timezone.utc))
print(curr_dt)
