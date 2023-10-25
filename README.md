# Scripting

Follow the instructions on [Python's official website](https://www.python.org/) to install Python. Then, using your terminal, run the following commands:

1. Create a virtual environment:
   ```shell
   python3 -m venv venv
    ```
2. Activate virtualenv 
    ```shell 
   source venv/bin/activate
   ```
3. Install all requirements
   ```shell 
   pip install -r requirements.txt
   ```
4. Run the program
   ```shell 
   python exercise.py
   ```
The program will generate the `sales_report_output.csv` file with budget values converted to the local currency.

Note:

Please be aware that the API used in this program may not support all currencies. As a result, the program may generate empty values for those currencies that are not supported. You can refer to the list of supported currencies at Supported Currencies for further information.

# PySpark
