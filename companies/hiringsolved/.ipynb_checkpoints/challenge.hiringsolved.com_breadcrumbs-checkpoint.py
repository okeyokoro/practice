import requests

message = "the next breadcrumb..."
base_url = "https://challenge.hiringsolved.com/breadcrumbs/"
breadcrumb = "50137"
breadcrumbs = []
messages = []

while "breadcrumb" in message or "keep going" in message:
    
    r = requests.get(base_url+breadcrumb)
    message = r.text
    print(message)

    if "Subtract " in message:
        print("subracting...")
        breadcrumb = str(int(breadcrumbs[-1]) - int(message.split("Subtract ")[1].split(" ")[0]))
        print(f"the next breadcrumb is {breadcrumb}")
    elif "Add " in message:
        print("adding...")
        breadcrumb = str(int(breadcrumbs[-1]) + int(message.split("Add ")[1].split(" ")[0]))
        print(f"the next breadcrumb is {breadcrumb}")
    else:
        breadcrumb = message.split(" ")[-1]

    breadcrumbs.append(breadcrumb)
    messages.append(message)

