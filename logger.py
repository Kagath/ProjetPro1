import os
import datetime

def log(log_type, message, log_file):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} [{log_type}] {message}\n"

    with open(log_file, "a") as f:
        f.write(log_message)

def log_info(message, log_file="logs/info.log"):
    log("INFO", message, log_file)

def log_error(message, log_file="logs/error.log"):
    log("ERROR", message, log_file)

def save_result(result, result_file="results/results.txt"):
    with open(result_file, "a") as f:
        f.write(result)
        f.write("\n")
