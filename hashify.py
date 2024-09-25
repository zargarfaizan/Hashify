import hashlib  # For hashing functions
import os  # For file handling

def hash_string(input_string, algorithm='sha256'):
    """Hash a given string with the specified algorithm."""
    hash_func = getattr(hashlib, algorithm)()  # Get the hash function
    hash_func.update(input_string.encode('utf-8'))  # Update with the string
    return hash_func.hexdigest()  # Return the hash

def hash_file(file_path, algorithm='sha256'):
    """Hash a file using the specified algorithm."""
    hash_func = getattr(hashlib, algorithm)()  # Get the hash function
    with open(file_path, "rb") as f:  # Open file in binary mode
        for byte_block in iter(lambda: f.read(4096), b""):  # Read in chunks
            hash_func.update(byte_block)  # Update with the chunk
    return hash_func.hexdigest()  # Return the hash

def main():
    """Main function for user interaction."""
    print("Welcome to Hashify!")  # Greeting
    choice = input("Hash a file or a string? (file/string): ").strip().lower()

    if choice == 'file':
        file_path = input("Enter the file path: ").strip()  # Get file path
        if os.path.isfile(file_path):  # Check if file exists
            algorithm = input("Hashing algorithm (sha256/md5/sha1): ").strip().lower()  # Get algorithm
            hash_value = hash_file(file_path, algorithm)  # Generate file hash
            print(f"{algorithm.upper()} hash: {hash_value}")  # Output hash
        else:
            print("File does not exist.")  # Error if file not found

    elif choice == 'string':
        input_string = input("Enter the string to hash: ").strip()  # Get string
        algorithm = input("Hashing algorithm (sha256/md5/sha1): ").strip().lower()  # Get algorithm
        hash_value = hash_string(input_string, algorithm)  # Generate string hash
        print(f"{algorithm.upper()} hash: {hash_value}")  # Output hash

    else:
        print("Invalid choice! Select 'file' or 'string'.")  # Error for invalid input

if __name__ == "__main__":
    main()  # Execute main function
