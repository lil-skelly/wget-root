def handle_prompt_validation(prompts: dict[str, any], default_values: list, validation_funcs: list[callable]) -> dict[str, any]:
    results = {}
    for prompt, default, validation_func in zip(prompts, default_values, validation_funcs):
        while True:
            value = input(prompts[prompt]).strip()
            value = value if value else default
            if validation_func(value):
                results[prompt] = value
                break
            # else:
            #     logger.error(f"{RED}Invalid input. Please provide valid data.")
    return results


prompts = [
    f"{BOLD}Network interface or IP address to host the HTTP server {CYAN}{BOLD}(default: eth0):{RESET} ",
    f"{BOLD}Specify alternate port {CYAN}{BOLD}(default: 8000):{RESET} ",
    f"{BOLD}File to config {CYAN}{BOLD}(Must be a valid file!):{RESET} ",
    f"{BOLD}Payload to execute (Options: {CYAN}{BOLD}forceroot, dnspoof):{RESET} ",
    ]
defaults = ["eth0", 8000, None]
validation_funcs = [
    lambda x: True,
    lambda x: x.isdigit(),
    lambda x: os.path.isfile(x),
    lambda x: x in ["forceroot", "dnspoof"]
]
results = handle_prompt_validation(prompts, defaults, validation_funcs)
