# Email Archive Search

A comprehensive email and PDF archive management solution designed to bridge the gap between stakeholder communications and enterprise database systems. This tool empowers data entry, management, and governance teams to efficiently organize and process email archives for seamless integration with ERP/CRM platforms.

## Overview

Email Archive Search streamlines the workflow of extracting, categorizing, and managing critical business documents from email communications. By automating the discovery and organization of emails and attachments, this utility significantly reduces manual data entry overhead while improving data accuracy and accessibility.

## Dependencies

### Python Packages (via pip)
- `extract_msg` - Email parsing and extraction
- `easyocr` - Optical character recognition for document processing
- `pdf2image` - PDF to image conversion
- `Pillow` - Image processing and manipulation

### Portable Libraries
- `poppler` - PDF rendering engine

## Features

### 1. Email Keyword Search
Perform comprehensive searches across multiple email components to quickly locate relevant communications:
- **Sender, recipient, and CC fields** - Identify correspondence by participant
- **Subject lines** - Filter by email topics
- **Message body** - Full-text search within email content
- **Attachments** - Scan attachment names and content

Search results are automatically collated into organized folders for easy access and review.

### 2. Email PDF Extractor
Efficiently extract PDF attachments from email archives with recursive directory scanning:
- Searches up to **three directory levels deep**
- Automatically identifies and extracts PDF files
- Essential for processing tax documents, invoices, and compliance materials
- Organizes extracted PDFs in a centralized location

### 3. PDF OCR and Categorization
Intelligent document processing powered by optical character recognition:
- **Automated document classification** - Distinguishes between W-9 forms and other PDF types
- **Smart file naming** - Renames W-9 forms using extracted business and DBA names
- **Batch processing** - Handles large volumes of documents efficiently
- **Data governance support** - Ensures proper document organization for compliance and auditing

## Use Cases

- **Tax document management** - Extract and organize W-9 forms from vendor communications
- **Vendor onboarding** - Streamline collection of business documentation
- **Compliance auditing** - Rapidly locate specific communications and attachments
- **Database synchronization** - Bridge email archives with structured ERP/CRM data
- **Document governance** - Maintain organized, searchable archives for regulatory requirements

## Getting Started

Make sure you have installed python (3.6 or newer) and click the Run.bat file (below)

```bat
@echo off
REM

REM Creates temp python script to check dependancies
set TEMP_PY=%TEMP%\check_deps_temp.py

echo import subprocess > "%TEMP_PY%"
echo import sys >> "%TEMP_PY%"
echo required = ["extract_msg","easyocr","pdf2image","Pillow"] >> "%TEMP_PY%"
echo for package in required: >> "%TEMP_PY%"
echo     try: >> "%TEMP_PY%"
echo         __import__(package) >> "%TEMP_PY%"
echo         print(f"{package} already installed.") >> "%TEMP_PY%"
echo     except ImportError: >> "%TEMP_PY%"
echo         print(f"{package} not found, installing...") >> "%TEMP_PY%"
echo         subprocess.check_call([sys.executable, "-m", "pip", "install", package]) >> "%TEMP_PY%"

REM run py script
python "%TEMP_PY%"

REM delete py script
del "%TEMP_PY%"

REM run main
python ./core/Windowbuilder.py

pause
```
