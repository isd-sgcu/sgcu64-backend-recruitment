# โจทย์ข้อที่ 3: API

## วัตถุประสงค์

- วัดความรู้พื้นฐานในการออกแบบ API Endpoint
- วัดความรู้พื้นฐานในการเลือกใช้ HTTP Methods, Status Codes
- เพื่อประเมินความสามารถในการแก้ปัญหาของผู้สมัคร

## รายละเอียด

&emsp; บริษัท SGCU ใช้วิธีการเขียนข้อมูลของพนักงานไว้ในที่สมุดบันทึกมาโดยตลอด คุณและทีม Developer ของบริษัท SGCU ได้มองเห็นถึงปัญหาของวิธีการดังกล่าว จึงต้องการที่จะเปลี่ยนระบบจัดการข้อมูลพนักงานบริษัท ไปเป็นแบบ online เพื่อที่จะเปลี่ยนระบบนี้ให้ทันสมัยยิ่งขึ้น สามารถเก็บและแก้ไขข้อมูลได้ง่ายขึ้น คุณจึงยื่นเรื่องให้แก่ท่านประธาน

&emsp; จากการเสนอข้อมูลให้ประธานบริษัท เขาได้ถูกใจข้อเสนอดังกล่าวเป็นอย่างมาก จึงได้ร้องขอให้คุณและทีม Developer พัฒนาเว็บไซต์เว็บไซต์ดังกล่าวขึ้นเพื่อมาใช้งาน คุณซึ่งเป็นหนึ่งในทีมได้รับหน้าที่ในการ**วางแผนและออกแบบ** API เพื่อที่จะให้เว็บไซต์สามารถทำงานได้อย่างราบรื่น

1. Endpoint Path (เช่น /user ฯลฯ)
2. HTTP Method (เช่น GET POST PUT DELETE ฯลฯ)
3. Headers (ถ้ามีนอกเหนือจาก header ทั่วไป เช่น Authorization)
4. Request Body (ถ้ามี) อาจเป็นในรูปแบบ plain text หรือ JSON
5. Request Params (ถ้ามี)
6. Request Query (ถ้ามี)
7. Response Body (ถ้ามี) อาจเป็นในรูปแบบ plain text หรือ JSON
8. Response Status Codes เป็นต้น เช่น (200, 400, 401, 403, 404, 500)

## งานของคุณ

&emsp; ออกแบบ API Documentation ที่ใช้ในระบบนี้เพื่อให้สามารถทำตาม requirements ที่ระบุไว้ด้านล่างได้ โดยแต่ละ API Endpoint (URL) ขอให้อธิบายให้ละเอียดที่สุด เช่น

&emsp; **เป็นไปได้ที่ 1 endpoint จะมีได้หลาย response ขึ้นอยู่กับความเป็นไปได้ที่เกิดขึ้น ขอให้ระบุให้ครบถ้วนที่สุด ลองดูตัวอย่างด้านล่าง**

## ลักษณะการจัดเก็บข้อมูลพนักงาน

1. id: เลขประจำตัวพนักงาน (string)
2. password : รหัสผ่านซึ่งใช้ในการ login (string)
3. firstName: ชื่อจริงของพนักงาน (string)
4. lastName: นามสกุลของพนักกงาน (string)
5. salary: เงินเดือนของพนักงาน (number)
6. role: ตำแหน่งของพนักงาน (string) **(optional)**

## Features ที่ต้องมี

### Minimum Requirements

1. สามารถเพิ่มพนักงานใหม่เข้าไปในระบบได้ (Create)
2. สามารถดูข้อมูลของพนักงานทุกคนได้ (Read)
3. สามารถแก้ไขข้อมูลของพนักงานได้ เช่นชื่อ-สกุล ตำแหน่ง และเงินเดือนของพนักงานได้ (Update)
4. สามารถลบข้อมูลพนักงานในระบบได้ (Delete)
5. สามารถค้นหาพนักงานโดยใช้ ชื่อ นามสกุล หรือ ตำแหน่งได้

### Optional

1. สามารถเข้าสู่ระบบได้ (โดยใช้ เลขพนักงาน, รหัสผ่าน)
2. สามารถแบ่งแยก user ออกเป็น 2 role คือ Employee กับ HR ดังนี้

Employee

1. สามารถ login ด้วย username และ password ได้
2. สามารถแก้ไข password ของตนเองได้
3. สามารถดูข้อมูลของตนเองได้ (นั่นคือ API มีวิธีระบุตัวตนว่าใครเป็นคนยิง API)
4. **ไม่สามารถ** ทำสิ่งที่ระบุไว้ 5 ข้อด้านบนได้ (ให้เฉพาะ HR ใช้งานเท่านั้น)

HR

1. ทำสิ่งที่ employee ทำได้
2. **สามารถ** สิ่งที่ระบุไว้ 5 ข้อด้านบนได้ (ให้เฉพาะ HR ใช้งานเท่านั้น)

### Tips

1. โจทย์ข้อนี้ไม่ต้องการให้ทำ API นั้นขึ้นมาจริงๆ เพียงแต่ออกแบบ API Endpoints ขึ้นมาเท่านั้น (แต่หากต้องการเขียน code backend ขึ้นมาจริง ๆ ก็สามารถทำได้)
2. **การออกแบบ API Documentation ไม่มีถูกผิด** สามารถสร้าง API Documentation ขึ้นมาแบบไหนก็ได้ เช่น text file, PDF, Swagger และอื่นๆ ที่สามารถแสดงข้อมูลได้อย่างถูกต้องและครบถ้วน
3. **การตรวจจะพิจารณาจากความเหมาะสมในการเลือกใช้ชื่อ Path, HTTP Method, Status Codes รวมถึงอื่น ๆ ตาม Convention ทั่วไปด้วย** สามารถศึกษาเพิ่มเติมได้เองเลย
4. HTTP Methods สามารถศึกษาเพิ่มเติมได้ที่
   ([https://www.restapitutorial.com/lessons/httpmethods.html](https://www.restapitutorial.com/lessons/httpmethods.html))
5. Status Codes สามารถศึกษาเพิ่มเติมได้ที่
   ([https://developer.mozilla.org/en-US/docs/Web/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status))
   ไม่จำเป็นต้องใช้หรือทราบทั้งหมด ที่ใช้ประจำมีไม่กี่อัน เช่น 200, 201, 301, 400, 401, 403, 404, 500, 503
6. การทำ Authorization (login, user identification) สามารถเลือกใช้วิธีใดก็ได้ เช่น JWT (JSON Web Token), session, หรือแม้แต่ HTTP Basic Auth
7. สำหรับ Authorization Header สามารถศึกษาเพิ่มเติมได้ที่
   ([https://www.loginradius.com/blog/async/everything-you-want-to-know-about-authorization-headers/](https://www.loginradius.com/blog/async/everything-you-want-to-know-about-authorization-headers/))
8. **หากสงสัยโจทย์ในส่วนใด สามารถติดต่อสอบถามได้ที่ isd.sgcu64@gmail.com เสมอ**

<br/>

### ตัวอย่าง API Documentation

#### ทำแบบ Text

- Create task

  - Description: Creates a task with the given input. Returns the instance of the task stored in database. Task must have both name and deadline.
  - Path: /task
  - Method: POST
  - Headers: ไม่มีเพิ่มเติม
  - Request Body: JSON
    ```js
    {
      "name": "Buy chicken",
      "deadline": "21/07/2021"
    }
    ```
  - Request Params: ไม่มี
  - Request Query: ไม่มี
  - Responses
    - Successful task creation
      - Response Body: JSON
      ```json
      {
        "id": 1,
        "name": "Buy chicken",
        "deadline": "21/07/2021"
      }
      ```
      - Status Code: 200 OK
    - Incorrect request body
      - Response Body: JSON
      ```json
      {
        "message": "name or deadline does not exist."
      }
      ```
      - Status Code: 400 Bad Request

#### ทำแบบ Swagger (Spec ที่แสดงอาจไม่ตรงกับ UI ยกมาเพื่อให้เห็นภาพเฉย ๆ)
![image](https://user-images.githubusercontent.com/24814968/121923165-db069f00-cd64-11eb-9098-539c2e1734a9.png)  

OpenAPI Spec

![image](https://user-images.githubusercontent.com/24814968/121923206-e5289d80-cd64-11eb-950d-8391bcdc27e0.png)  

Swagger UI

# Applicant Section

ตั้งแต่ส่วนนี้ลงไป เป็นส่วนที่ผู้สมัครสามารถแก้ไขได้ตามอัธยาศัย ซึ่งอาจจะเป็นข้อสันนิษฐานหรือไอเดียเพิ่มเติมก็ได้
