import logging
from datetime import datetime
import os

# Базова директорія — там, де лежить сам скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Повний шлях до вхідного файлу
LOG_INPUT = os.path.join(
    BASE_DIR,
    "heartbeat",
    "hblog.txt"
)

# Повний шлях до вихідного файлу
LOG_OUTPUT = os.path.join(
    BASE_DIR,
    "hb_test.log"
)

# Лог створюється завжди у тій самій папці, що й скрипт
logging.basicConfig(
    filename=LOG_OUTPUT,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract_timestamp(line: str):
    parts = line.split()
    for i, p in enumerate(parts):
        if p == "Timestamp":
            return datetime.strptime(parts[i + 1], "%H:%M:%S")
    return None

def process_log(path: str):
    with open(path, "r") as f:
        lines = f.readlines()

    prev_ts = None
    last_ts = None
    delays_found = False

    for line in lines:
        ts = extract_timestamp(line)
        if ts is None:
            continue

        # Новий блок Timestamp
        if last_ts is None:
            last_ts = ts
            continue

        if ts != last_ts:
            # Аналізуємо різницю між блоками
            if prev_ts:
                diff = abs((ts - prev_ts).total_seconds())

                if diff > 31 and diff <= 33:
                    logging.warning(f"Heartbeat WARNING: delay {diff} sec")
                    delays_found = True
                elif diff > 33:
                    logging.error(f"Heartbeat ERROR: delay {diff} sec")
                    delays_found = True

            prev_ts = ts
            last_ts = ts

    # Якщо не знайдено жодної затримки — все одно пишемо у файл
    if not delays_found:
        logging.info("No heartbeat delays detected")

if __name__ == "__main__":
    process_log(LOG_INPUT)