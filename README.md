# ASU Course Registration Automation [Developed in 2023]

## My Personal Experience
I arrived in the US in August 2023 for the Fall semester. Back in India during the Summer of 2023, I had registered for my core CS courses without much of a strategic plan. After arriving and observing the learning strategies used by my peers, I realized I should focus on my specific areas of interest. Since I was passionate about security, I planned to take the **Engineering Blockchain Applications** course in the Spring 2024 semester.

There was only one section available with 150 seats, and it was in extremely high demand. On the day of registration, I woke up before 6:00 AM and pressed the register button at exactly 6:00 AM sharp. Despite my timing, the initial loading symbol ended with a notification that I didn't get the course.

I later learned about the "add/drop" period, where seats occasionally open up before the semester starts. I tried manually checking the website for availability, but no seats ever seemed to stay open. This gave me the idea to build a system to track the course 24/7. I wrote a script that monitored the course status; whenever a seat opened, it would notify me immediately so I could register via my laptop or mobile phone.

I tracked three courses in my cart, with Blockchain as my priority. The automation ran for five days. I actually missed the window twice because seats were being filled within 10 seconds of being dropped—it felt like I was competing against machines. Finally, on the sixth day, I caught an opening and successfully registered. I ultimately finished the course with an **A+** and truly enjoyed the material.

## The Challenge
The course was in such high demand that seats would vanish within seconds of a student dropping them (250-300 students competing for a single seat after the course registration day completed). Initially, it felt impossible to compete manually.

## Conclusion
This was the first project that introduced automation into my Software Engineering career. Since then, I have moved on to developing much more complex automated systems.

## Technical Stack
* **Language:** Python
* **Browser:** Chrome Webdriver (Chrome Browser)
* **Automation Engine:** Selenium WebDriver
* **Notification System to Mobile:** Gmail Server (smtp.gmail.com)

---

**Note for Students:** Analyze the logic of this script and adapt the selectors to the current ASU website structure to secure your high-priority courses.

