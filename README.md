# לוגיקה עסקית - תשובות 

שאלה 5:

נוכל לבדוק את כל הפונקציות של השירות באמצעות unit tests.

בכל פונקציה נבדוק את הפלט שלה עם פלט ידני שנבדוק בעצמנו.

מקרי הקצה שיכולים להיות הם - מסת מטען שלילית ושווה אפס.

מסה שווה אפס היא מקרה קצה שבו השירות אמור לעבוד כמו שצריך וזהו מקרה שהמערכת צריכה לחשב בו את הפלט כרגיל לפי אותן נוסחאות.

חשוב לבדוק שהמערכת עובדת גם כשמסת המטען שווה אפס קילוגרם.

במקרה שהקלט למסת המטען שלילי או לא מספר, נבקש מהמשתמש להזין מסה חיובית ולא נקבל פלט עד שהוא יכניס מסה חיובית או אפס.

במקרה בו אחת הפונקציות מקבלת קלט שלילי או שאינו מספר, נזרוק חריגה.

שאלה 6:

על מנת לשפר את המודל הפיזיקלי של במערכת, נוכל להתחשב במסה של המטוס שמשתנה בעקבות צריכת דלק, בחיכוך (עם האוויר ועם המשטח) ונוכל להשתמש במשוואות של תנועה שאיננה שוות תאוצה.

# תשובות - חיבור ל API חיצוני 

לדעתי, כדאי להציג ללקוחות גם את הרוח (מהירות וכיוון) כמו את הטמפטרטורה בגובה בו המטוס טס, וכן את נתוני מזג האוויר ביעד הטיסה.


# שרידות המערכת 

המערכת שבניתי תלויה בחיבור אינטרנט ולא תעבוד כאשר הלקוח לא מחובר לאינטרנט.
המערכת לא תשרוד גם במקרה שתקרה תקלה במחשבים של השרת.
האפליקציה גם תלויה ב API החיצוני, ולכן לא תשרוד במקה של תקלה בשרת של ה API החיצוני.
