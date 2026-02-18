const { Builder, Browser, By, Key, until } = require('selenium-webdriver')

;(async function example() {
  let driver = await new Builder().forBrowser(Browser.FIREFOX).build()
  try {
    await driver.get('https://www.youtube.com/')
    await driver.wait(until.elementLocated(By.xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")), 10000)
    const loginbutton = await driver.findElement(By.xpath, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
    loginbutton.click()
    await new Promise((resolve)=>setTimeout(resolve, 100000))
    // await driver.wait(until.elementIsDisabled(revealed),10000)
    // await driver.findElement(By.name('q')).sendKeys('webdriver', Key.RETURN)
    // await driver.wait(until.titleIs('webdriver - Google Search'), 100000)
  } finally {
    await driver.quit()
  }
})()