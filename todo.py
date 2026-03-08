import json     # นำเข้า library json เพื่อใช้จัดการอ่านและเขียนไฟล์นามสกุล .json

file_name = "tasks.json"    # กำหนดชื่อไฟล์ที่จะใช้เก็บข้อมูลรายการงานต่างๆ

# load tasks from file (ฟังก์ชันสำหรับโหลดงานจากไฟล์)
def load_task():
    try:
        with open(file_name,"r") as file:       # พยายามเปิดไฟล์ tasks.json เพื่ออ่าน ("r")
            return json.load(file)              # แปลงข้อมูลจาก json เป็น list ของ python แล้วส่งค่ากลับ
    except:
        return[]                                # ถ้าหาไฟล์ไม่เจอ หรือไฟล์ว่างเปล่า ให้ส่งค่ากลับเป็น List ว่าง []
    
# save tasks to file (ฟังก์ชันสำหรับบันทึกงานลงไฟล์)
def save_tasks(tasks):
    with open(file_name, "w") as file:          # เปิดไฟล์เพื่อเขียนทับ ("w")
        json.dump(tasks, file)                  # แปลง List ใน Python กลับเป็นรูปแบบ JSON แล้วเซฟลงไฟล์
    
# add new task (ฟังก์ชันเพิ่มงานใหม่)
def add_task(tasks):
    task_name = input("Enter new task: ")       # รับชื่อเหตุการณ์จากผู้ใช้
    task = {
        "name" : task_name,                     # เก็บชื่อใน key ที่ชื่อว่า "name"
        "done" : False                          # กำหนดสถานะเริ่มต้นให้เป็น False (ยังไม่เสร็จ)
    }
    tasks.append(task)                          # นำ dict ของงานใหม่ไปต่อท้าย List 'tasks'
    save_tasks(tasks)                           # บันทึกลงไฟล์ทันที
    print("Task added")

# show all task (ฟังก์ชันแสดงงานทั้งหมด)
def show_all_tasks(tasks):
    if len(tasks) == 0:                         # ตรวจสอบว่ามีงานในลิสต์ไหม
        print("No tasks found")
        return
    
    for i, task in enumerate(tasks, start=1):   # วนลูปเพื่อดึงลำดับ (i) และข้อมูลงาน (task)
        status = "✓" if task["done"] else " "   # ถ้า "done" เป็น True ให้ใส่เครื่องหมายถูก
        print(f"{i}. {task['name']} [{status}]")

# complete task (ฟังก์ชันเปลี่ยนสถานะงานว่าเสร็จแล้ว)
def complete_task(tasks):
    show_all_tasks(tasks)                       # แสดงรายการให้ผู้ใช้ดูก่อนเลือก
    num = int(input("Emter task number: "))     # รับลำดับจากผู้ใช้ (เป็นตัวเลข)
    index = num - 1                             # แปลงเป็นเลข index ของ List (เริ่มที่ 0)
    tasks[index]["done"] = True                 # เปลี่ยนสถานะ "done" เป็น True
    save_tasks(tasks)                           # บันทึกการเปลี่ยนแปลง
    print("Tasks complete")

# delete task (ฟังก์ชันลบงาน)
def delete_task(tasks):
    show_all_tasks(tasks)
    num = int(input("Enter task number to delete: "))
    index = num - 1
    tasks.pop(index)                            # ลบข้อมูลออกจาก List ตามตำแหน่ง index
    save_tasks(tasks)
    print("Task delete")

# main program (ฟังก์ชันหลักที่เป็นจุดเริ่มต้นของโปรแกรม)
def main():
    tasks = load_task()                         # โหลดข้อมูลที่มีอยู่เดิมขึ้นมา

    while True:
        print("\nTo-Do list")
        print("1. Add task")
        print("2. Show all tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = int(input("Choose 1-5:"))

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            show_all_tasks(tasks)
        elif choice == 3:
            complete_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("INVALID")

# ตรวจสอบว่าไฟล์นี้ถูกรันโดยตรงหรือไม่ (ไม่ใช่การถูก import ไปที่อื่น)
if __name__ == "__main__":
    main()