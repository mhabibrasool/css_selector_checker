#!/usr/bin/env python3

"""
    Python CSS locator program.
    Powered by: playwright
    @uthor: Administrator
"""

# ====== import libs ======
import logging as log # Make it easy
import asyncio
import json
from playwright.async_api import async_playwright , Page


# ====== Setup logging ======
log.basicConfig(
    level=log.INFO,
    format="[%(asctime)s] %(levelname)s : %(message)s",
    handlers = [
        log.FileHandler('scraper.log'),
        log.StreamHandler(),
        ],
    )


async def check_selector(page, selectors):
    for selector in selectors:
        elements = await page.locator(selector).all()    # Check for selectors across entire markup code
        count = len(elements)

        if count > 0:
            log.info(f"Selector found: {selector}- {count} elements")
        elif count == 0:
            log.warning(f"Selector exist but found {selector} elements")

        else:
            log.warning(f"Selector not found: {selector}")



async def main():
    log.info('Program working....')
    base_url = input("Welcome to CSS selector checking. Please enter the url you wish to search selectors: ")

    selectors_input = input("Enter the selector you wish to find ( if more than one selector, separate it by comma) : ")

    selectors = [s.strip() for s in selectors_input.split(",")]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        log.info(f"Visiting page {base_url}")
        try:
            await page.goto(base_url, timeout=20000)
            await check_selector(page, selectors)
        except Exception as e:
            log.critical(f"Program facing dificulties {e} exiting....")

    await browser.close()


# Run it
if __name__ == "__main__":
    asyncio.run(main())
