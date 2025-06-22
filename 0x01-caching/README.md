# 0x01. Caching

This project is part of the ALX Backend curriculum and focuses on implementing and comparing core caching strategies in Python. It is designed to help you understand how different cache replacement policies affect system performance and resource management.

## Project Overview
This project explores caching strategies and their implementation in backend systems. You will design and implement various cache replacement policies to optimize data retrieval and resource usage.

## Learning Objectives
- Understand the role of caching in backend architectures.
- Implement multiple cache replacement algorithms (FIFO, LIFO, LRU, MRU, LFU).
- Design extensible cache classes.
- Evaluate trade-offs between different caching strategies.

## Requirements
- Python 3.x
- No external dependencies required (standard library only)

## Project Structure
- `base_caching.py` – Abstract base class for all cache implementations.
- `0-basic_cache.py` – Basic cache with no eviction policy.
- `1-fifo_cache.py` – First-In First-Out cache.
- `2-lifo_cache.py` – Last-In First-Out cache.
- `3-lru_cache.py` – Least Recently Used cache.
- `4-mru_cache.py` – Most Recently Used cache.
- `100-lfu_cache.py` – Least Frequently Used cache.
- `*-main.py` – Test scripts for each cache class.
- `README.md` – Project documentation.

## Cache Policies Implemented
- **Basic Cache**: No eviction, stores up to a fixed limit.
- **FIFO (First-In First-Out)**: Removes the oldest item when the cache is full.
- **LIFO (Last-In First-Out)**: Removes the most recently added item when the cache is full.
- **LRU (Least Recently Used)**: Removes the least recently accessed item.
- **MRU (Most Recently Used)**: Removes the most recently accessed item.
- **LFU (Least Frequently Used)**: Removes the item used least often.

## Usage
1. Run any of the main test scripts to see cache behavior:
   ```zsh
   python 1-main.py
   ```
2. Review the output to understand how each cache policy manages data.
