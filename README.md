# 🎭 Playwright Test Automation Framework

![Playwright Tests](https://github.com/liliyadev/playwright-test-automation-framework/actions/workflows/python-tests.yml/badge.svg)

A modern UI automation framework built with **Playwright**, **Python**, and **Pytest** for testing the SauceDemo e-commerce demo application.

---

## 🚀 What This Project Demonstrates

- Playwright browser automation
- Page Object Model design
- Pytest test structure
- End-to-end checkout testing
- HTML reporting
- GitHub Actions CI/CD
- Comparison with Selenium framework design

---

## 🧪 Test Scenarios

| Area | Test Coverage |
|---|---|
| Login | Valid and invalid login |
| Inventory | Add and remove product |
| Cart | Verify product is added |
| Checkout | Complete end-to-end purchase |

---

## 🏗 Framework Structure

```text
playwright-test-automation-framework/
├── config/
│   └── settings.py
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── overview_page.py
│   └── complete_page.py
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── reports/
├── screenshots/
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## ▶️ Run Tests

```bash
pip install -r requirements.txt
playwright install
pytest
```

---

## 📊 HTML Report

After execution, the report is generated here:

```text
reports/report.html
```

---

## 🔍 Why Playwright?

Compared with Selenium, Playwright provides:

- Built-in auto-waiting
- Cleaner locator syntax
- Faster setup
- Reliable browser context handling
- Easier end-to-end workflow automation

---

## 📚 Related Project

I also built the same framework using Selenium:

[selenium-test-automation-framework](https://github.com/liliyadev/test-automation-portfolio)

---

## 👩‍💻 Author

**Liliya Vildanova**  
Junior Test Automation Engineer  
GitHub: [liliyadev](https://github.com/liliyadev)