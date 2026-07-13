def log_event(message, *args, **kwargs):
    print(f"Event: {message}")

    if args:
        print(f"Details: {args}")
    
    if kwargs:
        print(f"Metadata: {kwargs}")

# * unpacks any extra positional arguments into a tuple
#   useful when you don't know how many items a user will pass
# ** unpacks named arguments into a dictionary
#   perfect for optional configuration settings
log_event("User Login", "admin", "dashboard", timestamp="10:00 AM", status="Success")
