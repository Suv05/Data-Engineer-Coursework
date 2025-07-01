# HDFS Command Cheat Sheet

This README provides a comprehensive guide to essential HDFS (Hadoop Distributed File System) commands. It covers navigation, file operations, directory management, storage information, advanced operations, common data engineering scenarios, best practices, and troubleshooting tips.
---

## 1. Basic HDFS Command Structure

There are two equivalent ways to interact with HDFS:

* `hadoop fs [commands]`
* `hdfs dfs [commands]`

Both commands achieve the same results. Choose whichever you find more comfortable.

---

## 2. Navigation and File Listing

### Basic Listing Commands

* **List files in your HDFS home directory:**
    ```bash
    hadoop fs -ls
    ```
    *Explanation:* Lists the contents of the current user's home directory in HDFS.

* **List files in a specific HDFS directory:**
    ```bash
    hadoop fs -ls /user/username
    ```
    *Explanation:* Lists the contents of the specified HDFS directory. Replace `/user/username` with the actual path.

* **List files recursively:**
    ```bash
    hadoop fs -ls -R /user/username
    ```
    *Explanation:* Lists the contents of the specified directory and all its subdirectories recursively.

* **List files with human-readable sizes:**
    ```bash
    hadoop fs -ls -h /user/username
    ```
    *Explanation:* Lists files with their sizes displayed in human-readable format (e.g., KB, MB, GB).

* **Sort by timestamp (newest first):**
    ```bash
    hadoop fs -ls -t /user/username
    ```
    *Explanation:* Lists files sorted by their modification timestamp, with the newest files appearing first.

* **Sort by size:**
    ```bash
    hadoop fs -ls -S -h /data_warehouse
    ```
    *Explanation:* Lists files sorted by their size, with the largest files appearing first. The `-h` flag makes sizes human-readable.

> **Pro Tip:** The `-h` flag makes file sizes human-readable (KB, MB, GB) instead of bytes.

---

## 3. Directory Management

* **Create a directory:**
    ```bash
    hadoop fs -mkdir /user/username/new_dir
    ```
    *Explanation:* Creates a new directory in the specified HDFS path.

* **Create nested directories:**
    ```bash
    hadoop fs -mkdir -p /user/username/dir1/dir2/dir3
    ```
    *Explanation:* Creates a directory and any necessary parent directories that do not already exist.

* **Remove an empty directory:**
    ```bash
    hadoop fs -rmdir /user/username/empty_dir
    ```
    *Explanation:* Removes an empty directory from HDFS. Will fail if the directory contains files.

* **Remove a directory and its contents:**
    ```bash
    hadoop fs -rm -R /user/username/dir_with_contents
    ```
    *Explanation:* Recursively removes a directory and all its contents (files and subdirectories). Use with caution.

---

## 4. File Operations

### Copying Files Between Local and HDFS

#### From Local to HDFS:

* **Using `put`:**
    ```bash
    hadoop fs -put localfile.txt /user/username/
    ```
    *Explanation:* Copies a file from the local filesystem to the specified HDFS directory.

* **Using `copyFromLocal`:**
    ```bash
    hadoop fs -copyFromLocal bigdata.csv /user/username/data/
    ```
    *Explanation:* Similar to `put`, copies a file from the local filesystem to HDFS.

* **`put` with overwrite if the file exists:**
    ```bash
    hadoop fs -put -f localfile.txt /user/username/
    ```
    *Explanation:* Copies a file from local to HDFS. If a file with the same name already exists in the destination, it will be overwritten.

#### From HDFS to Local:

* **Using `get`:**
    ```bash
    hadoop fs -get /user/username/hdfs_file.txt local_directory/
    ```
    *Explanation:* Copies a file from HDFS to the specified local directory.

* **Using `copyToLocal`:**
    ```bash
    hadoop fs -copyToLocal /user/username/hdfs_file.txt .
    ```
    *Explanation:* Similar to `get`, copies a file from HDFS to the local filesystem. The `.` indicates the current local directory.

### Operations Within HDFS

* **Copy files within HDFS:**
    ```bash
    hadoop fs -cp /source/path/file.txt /destination/path/
    ```
    *Explanation:* Copies a file from one location in HDFS to another.

* **Move files within HDFS:**
    ```bash
    hadoop fs -mv /source/path/file.txt /destination/path/
    ```
    *Explanation:* Moves (renames) a file from one location in HDFS to another.

* **Remove a file:**
    ```bash
    hadoop fs -rm /user/username/unwanted_file.txt
    ```
    *Explanation:* Deletes a specific file from HDFS.

* **Remove a directory and its contents:**
    ```bash
    hadoop fs -rm -R /user/username/unwanted_directory
    ```
    *Explanation:* Recursively deletes a directory and all its contents in HDFS. (Same as directory management, but listed here for file operations context).

---

## 5. File Content Operations

### Viewing File Contents

* **View the entire file:**
    ```bash
    hadoop fs -cat /user/username/file.txt
    ```
    *Explanation:* Displays the entire content of a file to the console.

* **View the first few lines:**
    ```bash
    hadoop fs -head /user/username/file.txt
    ```
    *Explanation:* Displays the first 1KB of a file's content.

* **View the last few lines:**
    ```bash
    hadoop fs -tail /user/username/file.txt
    ```
    *Explanation:* Displays the last 1KB of a file's content.

* **Merge small files:**
    ```bash
    hadoop fs -getmerge /user/username/small_files/* merged_file.txt
    ```
    *Explanation:* Takes all files in the specified HDFS directory, concatenates them, and writes the output to a single local file.

---

## 6. Storage and System Information

### Storage Usage

* **Check disk usage:**
    ```bash
    hadoop fs -df -h
    ```
    *Explanation:* Displays the free and used space on the HDFS filesystem, similar to the `df` command on Linux. The `-h` flag makes sizes human-readable.

* **Get directory space usage:**
    ```bash
    hadoop fs -du -h /user/username
    ```
    *Explanation:* Displays the aggregate length of files in a directory or the length of a single file in HFS. The `-h` flag makes sizes human-readable.

* **Get a summary of directory usage:**
    ```bash
    hadoop fs -du -s -h /user/username/*
    ```
    *Explanation:* Provides a summary of disk usage for each specified path, rather than listing individual files.

### File System Check

* **Check file status and block locations:**
    ```bash
    hdfs fsck /user/username/important_file.txt -files -blocks -locations
    ```
    *Explanation:* Runs a filesystem check on the specified file or directory, reporting on its health, file status, block locations, and more.

* **Get a filesystem health report:**
    ```bash
    hdfs dfsadmin -report
    ```
    *Explanation:* Provides a detailed report on the HDFS cluster's health, including DataNode status, capacity, and usage.

---

## 7. Advanced Operations

### Permission Management

* **Change file permissions:**
    ```bash
    hadoop fs -chmod 644 /user/username/file.txt
    ```
    *Explanation:* Changes the permissions of a file or directory in HDFS using octal notation (e.g., 644 grants read/write to owner, read to group and others).

* **Change file ownership:**
    ```bash
    hadoop fs -chown username:group /user/username/file.txt
    ```
    *Explanation:* Changes the owner and/or group of a file or directory in HDFS.

* **Change group ownership:**
    ```bash
    hadoop fs -chgrp newgroup /user/username/file.txt
    ```
    *Explanation:* Changes only the group ownership of a file or directory in HDFS.

### File Checksums and Verification

* **Get file checksum:**
    ```bash
    hadoop fs -checksum /user/username/file.txt
    ```
    *Explanation:* Returns the checksum of a file in HDFS, which can be used to verify data integrity.

* **Test file existence:**
    ```bash
    hadoop fs -test -e /user/username/file.txt
    ```
    *Explanation:* Checks if a file or directory exists in HDFS. Returns 0 if it exists, 1 otherwise. Can be used in scripts.

---

## 8. Common Data Engineering Scenarios

### Data Pipeline Operations

* **Check if a directory is empty:**
    ```bash
    hadoop fs -ls /user/username/input_dir | wc -l
    ```
    *Explanation:* Lists the contents of a directory and pipes the output to `wc -l` to count the lines. If the count is 0 (or 1 if only the directory itself is listed), it's empty.

* **Move processed files to an archive:**
    ```bash
    hadoop fs -mv /user/username/processed/* /user/username/archive/
    ```
    *Explanation:* Moves all files from the `processed` directory to an `archive` directory in HDFS.

* **Clean up temporary files:**
    ```bash
    hadoop fs -rm -skipTrash /user/username/temp/*
    ```
    *Explanation:* Removes all files within the `temp` directory. The `-skipTrash` flag permanently deletes files without moving them to the HDFS trash, useful for large deletions.

### Data Validation

* **Count the number of lines in a file:**
    ```bash
    hadoop fs -cat /user/username/data.txt | wc -l
    ```
    *Explanation:* Displays the file content and pipes it to `wc -l` to count the number of lines, useful for quick data validation.

* **Quick data sampling:**
    ```bash
    hadoop fs -head /user/username/large_file.csv
    ```
    *Explanation:* Quickly views the beginning of a large file to inspect its format and content without downloading the entire file.

---

## 9. Best Practices

* **Always Use Absolute Paths:**
    ```bash
    hadoop fs -ls /user/username/data  # Better than relative paths
    ```
    *Explanation:* Using absolute paths ensures that your commands are unambiguous and run correctly regardless of your current working directory in HDFS.

* **Check Commands Before Execution:**
    ```bash
    # Use count before remove
    hadoop fs -count /user/username/to_delete
    hadoop fs -rm -R /user/username/to_delete
    ```
    *Explanation:* Before performing destructive operations like `rm -R`, it's good practice to verify the contents and count of files in the target directory using commands like `ls` or `count`.

* **Use Appropriate Flags:**
    ```bash
    # Human readable sizes
    hadoop fs -du -h /user/username

    # Skip trash for large deletions
    hadoop fs -rm -skipTrash /user/username/large_files
    ```
    *Explanation:* Utilizing flags like `-h` for human-readable output or `-skipTrash` for large deletions can improve usability and efficiency.

---

## 10. Troubleshooting Tips

### Permission Issues

* **Check file permissions:**
    ```bash
    hadoop fs -ls -d /user/username/file.txt
    ```
    *Explanation:* Use `-ls -d` to list the permissions of the directory or file itself, rather than its contents.

* **Fix permissions:**
    ```bash
    hadoop fs -chmod 644 /user/username/file.txt
    ```
    *Explanation:* If you encounter permission denied errors, you might need to adjust the file or directory permissions using `chmod`.

### Space Issues

* **Check HDFS space:**
    ```bash
    hadoop fs -df -h
    ```
    *Explanation:* Regularly check the overall HDFS disk usage to ensure there's enough space for new data.

* **Find large files:**
    ```bash
    hadoop fs -ls -S -h /user/username
    ```
    *Explanation:* If HDFS space is low, use this command to identify large files or directories that might be candidates for deletion or archiving.
