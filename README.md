1 จงสร้าง model ของ ML ด้วยวิธี Decision Tree เพื่อทำนายประเภทดอก IRIS แล้วบันทึกเป็นไฟล์เก็บไว้
2 จงสร้างระบบให้บริการผ่าน Web App หรือ Web Service ด้วย Python Flask เพื่อทำนายประเภทดอก IRIS ด้วยการ Load model จากข้อ 1 และจาก Feature ทั้ง 4 ค่าที่ต้องการทำนาย โดย
      2.1 ถ้าเป็น Web App
                     ให้ทำหน้า Web ที่มีช่องให้กรอก

Feature    4 ค่า ประกอบด้วย Sepal length, Sepal width, Petal length และ Petal width  และสร้างปุ่มกด "ทำนาย" เพื่อทำนายว่าเป็นดอก IRIS ประเภทไหนจาก Feature ทั้ง 4 ที่ให้ใส่ค่า
      2.2 ถ้าเป็น Web Service
                     ให้ใช้ Postman ส่งไฟล์ Json ที่มีพารามิเตอร์ ตามนี้
                                 {"Sepal length": aaaaa, "Sepal width": bbbbb, "Petal length": ccccc, "Petal width": ddddd} ส่งให้ Web server ทำการประมวลผล เมื่อประมวลผลเสร็จให้ ส่งคืนค่ากลับมาในรูปของ Json ดังนี้
                                  {"Iris type": "XXXXX"}

3 ให้ส่งผ่าน Github โดยส่งเป็นลิ้ง http ของ Github (ตั้งค่าเป็น public)


V.2
จาก Assignment ที่แล้ว "Web or Web Service for IRIS ML using FLASK" ให้นักศึกษาต่อยอด โดยนำค่าที่ส่งให้และคืนค่าจาก ML เก็บลงฐานข้อมูล (อย่างง่าย โดยเขียนลงอย่างน้อย 1 Table) และโดยให้เพิ่ม ลิ้ง /All_result เพื่อดึงตารางด้งกล่าวมาดู ค่าที่ส่งให้ Classify และ ผลลัพธ์ที่ได้ โดยถ้าเป็น Web App ให้อยู่ในรูปตาราง แต่ถ้าเป็น Web Service ให้คืนค่ากลับมาเป็น JSON

In postgreSQL use command below:
CREATE TABLE iris_data (
    id SERIAL PRIMARY KEY,
    sepal_length FLOAT NOT NULL,
    sepal_width FLOAT NOT NULL,
    petal_length FLOAT NOT NULL,
    petal_width FLOAT NOT NULL,
    species VARCHAR(50) NOT NULL
);

