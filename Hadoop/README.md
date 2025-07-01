# HDFS Command Cheat Sheet

This README provides a comprehensive guide to essential HDFS (Hadoop Distributed File System) commands. It covers navigation, file operations, directory management, storage information, advanced operations, common data engineering scenarios, best practices, and troubleshooting tips.

## Table of Contents

1.  [Basic HDFS Command Structure](#basic-hdfs-command-structure)
2.  [Navigation and File Listing](#navigation-and-file-listing)
    * [Basic Listing Commands](#basic-listing-commands)
3.  [Directory Management](#directory-management)
4.  [File Operations](#file-operations)
    * [Copying Files Between Local and HDFS](#copying-files-between-local-and-hdfs)
        * [From Local to HDFS](#from-local-to-hdfs)
        * [From HDFS to Local](#from-hdfs-to-local)
    * [Operations Within HDFS](#operations-within-hdfs)
5.  [File Content Operations](#file-content-operations)
    * [Viewing File Contents](#viewing-file-contents)
6.  [Storage and System Information](#storage-and-system-information)
    * [Storage Usage](#storage-usage)
    * [File System Check](#file-system-check)
7.  [Advanced Operations](#advanced-operations)
    * [Permission Management](#permission-management)
    * [File Checksums and Verification](#file-checksums-and-verification)
8.  [Common Data Engineering Scenarios](#common-data-engineering-scenarios)
    * [Data Pipeline Operations](#data-pipeline-operations)
    * [Data Validation](#data-validation)
9.  [Best Practices](#best-practices)
10. [Troubleshooting Tips](#troubleshooting-tips)
    * [Permission Issues](#permission-issues)
    * [Space Issues](#space-issues)

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

* **List files in a specific HDFS directory:**
    ```bash
    hadoop fs -ls /user/username
    ```

* **List files recursively:**
    ```bash
    hadoop fs -ls -R /user/username
    ```

* **List files with human-readable sizes:**
    ```bash
    hadoop fs -ls -h /user/username
    ```

* **Sort by timestamp (newest first):**
    ```bash
    hadoop fs -ls -t /user/username
    ```

* **Sort by size:**
    ```bash
    hadoop fs -ls -S -h /data_warehouse
    ```

> **Pro Tip:** The `-h` flag makes file sizes human-readable (KB, MB, GB) instead of bytes.

---

## 3. Directory Management

* **Create a directory:**
    ```bash
    hadoop fs -mkdir /user/username/new_dir
    ```

* **Create nested directories:**
    ```bash
    hadoop fs -mkdir -p /user/username/dir1/dir2/dir3
    ```

* **Remove an empty directory:**
    ```bash
    hadoop fs -rmdir /user/username/empty_dir
    ```

* **Remove a directory and its contents:**
    ```bash
    hadoop fs -rm -R /user/username/dir_with_contents
    ```

---

## 4. File Operations

### Copying Files Between Local and HDFS

#### From Local to HDFS:

* **Using `put`:**
    ```bash
    hadoop fs -put localfile.txt /user/username/
    ```

* **Using `copyFromLocal`:**
    ```bash
    hadoop fs -copyFromLocal bigdata.csv /user/username/data/
    ```

* **`put` with overwrite if the file exists:**
    ```bash
    hadoop fs -put -f localfile.txt /user/username/
    ```

#### From HDFS to Local:

* **Using `get`:**
    ```bash
    hadoop fs -get /user/username/hdfs_file.txt local_directory/
    ```

* **Using `copyToLocal`:**
    ```bash
    hadoop fs -copyToLocal /user/username/hdfs_file.txt .
    ```

### Operations Within HDFS

* **Copy files within HDFS:**
    ```bash
    hadoop fs -cp /source/path/file.txt /destination/path/
    ```

* **Move files within HDFS:**
    ```bash
    hadoop fs -mv /source/path/file.txt /destination/path/
    ```

* **Remove a file:**
    ```bash
    hadoop fs -rm /user/username/unwanted_file.txt
    ```

* **Remove a directory and its contents:**
    ```bash
    hadoop fs -rm -R /user/username/unwanted_directory
    ```

---

## 5. File Content Operations

### Viewing File Contents

* **View the entire file:**
    ```bash
    hadoop fs -cat /user/username/file.txt
    ```

* **View the first few lines:**
    ```bash
    hadoop fs -head /user/username/file.txt
    ```

* **View the last few lines:**
    ```bash
    hadoop fs -tail /user/username/file.txt
    ```

* **Merge small files:**
    ```bash
    hadoop fs -getmerge /user/username/small_files/* merged_file.txt
    ```

---

## 6. Storage and System Information

### Storage Usage

* **Check disk usage:**
    ```bash
    hadoop fs -df -h
    ```

* **Get directory space usage:**
    ```bash
    hadoop fs -du -h /user/username
    ```

* **Get a summary of directory usage:**
    ```bash
    hadoop fs -du -s -h /user/username/*
    ```

### File System Check

* **Check file status and block locations:**
    ```bash
    hdfs fsck /user/username/important_file.txt -files -blocks -locations
    ```

* **Get a filesystem health report:**
    ```bash
    hdfs dfsadmin -report
    ```

---

## 7. Advanced Operations

### Permission Management

* **Change file permissions:**
    ```bash
    hadoop fs -chmod 644 /user/username/file.txt
    ```

* **Change file ownership:**
    ```bash
    hadoop fs -chown username:group /user/username/file.txt
    ```

* **Change group ownership:**
    ```bash
    hadoop fs -chgrp newgroup /user/username/file.txt
    ```

### File Checksums and Verification

* **Get file checksum:**
    ```bash
    hadoop fs -checksum /user/username/file.txt
    ```

* **Test file existence:**
    ```bash
    hadoop fs -test -e /user/username/file.txt
    ```

---

## 8. Common Data Engineering Scenarios

### Data Pipeline Operations

* **Check if a directory is empty:**
    ```bash
    hadoop fs -ls /user/username/input_dir | wc -l
    ```

* **Move processed files to an archive:**
    ```bash
    hadoop fs -mv /user/username/processed/* /user/username/archive/
    ```

* **Clean up temporary files:**
    ```bash
    hadoop fs -rm -skipTrash /user/username/temp/*
    ```

### Data Validation

* **Count the number of lines in a file:**
    ```bash
    hadoop fs -cat /user/username/data.txt | wc -l
    ```

* **Quick data sampling:**
    ```bash
    hadoop fs -head /user/username/large_file.csv
    ```

---

## 9. Best Practices

* **Always Use Absolute Paths:**
    ```bash
    hadoop fs -ls /user/username/data  # Better than relative paths
    ```

* **Check Commands Before Execution:**
    ```bash
    # Use count before remove
    hadoop fs -count /user/username/to_delete
    hadoop fs -rm -R /user/username/to_delete
    ```

* **Use Appropriate Flags:**
    ```bash
    # Human readable sizes
    hadoop fs -du -h /user/username

    # Skip trash for large deletions
    hadoop fs -rm -skipTrash /user/username/large_files
    ```

---

## 10. Troubleshooting Tips

### Permission Issues

* **Check file permissions:**
    ```bash
    hadoop fs -ls -d /user/username/file.txt
    ```

* **Fix permissions:**
    ```bash
    hadoop fs -chmod 644 /user/username/file.txt
    ```

### Space Issues

* **Check HDFS space:**
    ```bash
    hadoop fs -df -h
    ```

* **Find large files:**
    ```bash
    hadoop fs -ls -S -h /user/username
    ```