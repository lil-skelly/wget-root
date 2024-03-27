from wget_exploit import check_interface, logger, RED, GREEN, CYAN, BOLD, RESET
import os

def handle_prompt_validation(prompts: list[dict]) -> list:
    results = []
    for prompt in prompts:
        while True:
            value = input(prompt["text"]).strip()
            value = value if value else prompt["default"]
            if prompt["check"](value):
                results.append(value)
                break
            logger.error(f"{RED}Invalid input. Please provide valid data.{RESET}")
    return results

prompts = [
    {
        "text": f"{BOLD}Network interface or IP address to host the HTTP server {CYAN}{BOLD}(default: eth0):{RESET} ",
        "default": "eth0",
        "check": lambda x: check_interface(x)
    },
    {
        "text": f"{BOLD}Specify alternate port {CYAN}{BOLD}(default: 8000):{RESET} ",
        "default": 8000,
        "check": lambda x: str(x).isdigit()
    },
    {
        "text": f"{BOLD}File to config {CYAN}{BOLD}(Must be a valid file!):{RESET} ",
        "default": "",
        "check": lambda x: x != "" and os.path.isfile(x)
    },
    {
        "text": f"{BOLD}Payload to execute (Options: {CYAN}{BOLD}forceroot, dnspoof):{RESET} ",
        "default": "",
        "check": lambda x: x in ["forceroot", "dnspoof"]
    }
]

results = handle_prompt_validation(prompts)
serve_host, port, file, payload = results

print(results)