## 定时任务框架
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from docx import Document
import time


def timer(n):
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(n)


def read_docx():
    doc = Document(r"E:\test\test.docx")
    tables = doc.tables
    for i in range(len(tables)):
        tb = tables[i]
        tb_rows = tb.rows
        for i in range(len(tb_rows)):
            row_data = []
            row_cells = tb_rows[i].cells
            for cell in row_cells:
                row_data.append(cell.text)

            print(row_data)


def timeprint():
    print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
    print(datetime.now())


def job():
    # read_docx()
    timeprint()


# ASP定时任务框架
if __name__ == '__main__':
    # 定义BlockingScheduler
    sched = BlockingScheduler()
    sched.add_job(job, 'interval', seconds=1)
    sched.start()
