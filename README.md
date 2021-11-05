# FeishuAutoTestDemo

This is a automation testing framework which use [Feishu](https://www.feishu.cn/) as an example.
Execute `runner.py` to run.

## Technology

### Web UI Test

- pytest + selenium + yaml + allure, Page Object Model
- Data-driven testing and Keyword-driven testing

### API Test
- pytest + requests + allure, Page Object Modeling Way
- Data-driven testing


## Directory

- **api_test**: API Test Code
    - *api*: Feishu API encapsulation code
    - *test_case*: Test case code

- **web_test**: Web Test Code 
    - *page*: Feishu web page object encapsulation code
    - *test_case*: Test case code
- **data**
    - *page_function*: Yaml files that store page object function details
    - *test_case_data*: Yaml files that store test case data
- **utils**: Utility classes