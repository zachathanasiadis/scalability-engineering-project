from passlib.hash import argon2
import hashlib
import time
from db.shared_cache import shared_cache


def md5_task(parameters):
    """Task handler for calculating MD5 hash

    Args:
        parameters (dict): Task parameters containing 'string' to hash

    Returns:
        dict: Result containing the MD5 hash and execution time
    """
    start_time = time.time()

    # Get the string to hash
    string = parameters.get('string', '') if parameters else ''

    # Calculate MD5 hash
    md5 = hashlib.md5()
    md5.update(string.encode())
    hashed_string = md5.hexdigest()

    end_time = time.time()

    result = {
        'original_string': string,
        'md5_hash': hashed_string,
        'execution_time_seconds': end_time - start_time
    }

    # Store result in cache for future requests
    cache_key = f"md5:{string}"
    shared_cache.set(cache_key, result, ttl=3600)  # Cache for 1 hour

    return result


def sha256_task(parameters):
    """Task handler for calculating SHA256 hash

    Args:
        parameters (dict): Task parameters containing 'string' to hash

    Returns:
        dict: Result containing the SHA256 hash and execution time
    """
    start_time = time.time()

    # Get the string to hash
    string = parameters.get('string', '') if parameters else ''

    # Calculate SHA256 hash
    sha256 = hashlib.sha256()
    sha256.update(string.encode())
    hashed_string = sha256.hexdigest()

    end_time = time.time()

    result = {
        'original_string': string,
        'sha256_hash': hashed_string,
        'execution_time_seconds': end_time - start_time
    }
    # Store result in cache for future requests
    cache_key = f"sha256:{string}"
    shared_cache.set(cache_key, result, ttl=3600)  # Cache for 1 hour

    return result


def argon2_task(parameters):
    start_time = time.time()

    # Get the string to hash
    string = parameters.get('string', '') if parameters else ''

    # Calculate Argon 2 hash
    hashed_string = argon2.using(
        time_cost=6,     # Higher = slower
        memory_cost=65536,  # In KB (64 MB)
        parallelism=2
    ).hash(string)

    end_time = time.time()

    return {
        'original_string': string,
        'argon2_hash': hashed_string,
        'execution_time_seconds': end_time - start_time
    }
