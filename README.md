## API tests for Stellar Burgers

Url: https://stellarburgers.nomoreparties.site/

**Creating a user - test_create_user:**
- a unique user;
- a user who is already registered;
- a user without one of the required fields.

**User login - test_login:**
- login under an existing user,
- login with incorrect login and password.

**Changing user data - test_update_data:**
- with authorization,
- without authorization.

**Creating an order - test_create_order:**
- with authorization,
- without authorization,
- with ingredients,
- no ingredients,
- with an incorrect ingredient hash.

**Receiving orders from a specific user - test_get_order:**
- authorized user,
- unauthorized user.

Running tests: python -m pytest tests\
Reading run results: allure serve allure_results
