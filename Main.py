MaxAttempt = 3

Personal = {
    "Chris": {"Password": "!Pass1", "Role": "Admin", "Attempts": 0},
    "Tom": {"Password": "!Pass2", "Role": "Editor", "Attempts": 0},
    "Thomas": {"Password": "!Pass3", "Role": "Viewer", "Attempts": 0},
}

Permissions = {
    "Admin": {"View", "Edit", "Manage", "Update"},
    "Editor": {"View", "Edit", "Update"},
    "Viewer": {"View"}
}

NotifUpdates = {
    "Chris": [],
    "Tom": [],
    "Thomas": []
}

def Authentication (InputName, Password):
  if InputName not in Personal:
    print("That name is not valid")
    return False

  User = Personal[InputName]

  if User["Attempts"] >= MaxAttempt:
    print("Too many attempts. Your account is now locked. Contact admin.")
    return False

  if User["Password"] == Password:
    User["Attempts"] = 0
    return True

  else:
    User["Attempts"] += 1
    RemainingAttempts = MaxAttempt - User["Attempts"]
    print(f"Your password is not correct. You have this many {RemainingAttempts} attempts left.")
    return False

def HasAccess(InputName, Request):
  Role = Personal[InputName]["Role"]
  return Request in Permissions.get(Role, set())

def GetUpdates(Message):
  for InputName in NotifUpdates:
    NotifUpdates[InputName].append(Message)

def Access(InputName,  Request):
  if HasAccess(InputName, Request):
    print("Access granted.")

  else:
    print("Access denied.")
  