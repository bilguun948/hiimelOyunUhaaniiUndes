from collections import deque
from datetime import datetime
import time


# 1. Даалгаврын үндсэн класс
class Task:
    def __init__(self, task_id, description, priority=1):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.status = "Pending"
        self.created_at = datetime.now()
        self.error_message = None

    def get_id(self):
        return self.task_id

    def get_priority(self):
        return self.priority

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def __str__(self):
        return (
            f"ID: {self.task_id}, "
            f"Description: {self.description}, "
            f"Priority: {self.priority}, "
            f"Status: {self.status}"
        )


# 2. Өгөгдөл боловсруулах даалгавар
class DataProcessingTask(Task):
    def __init__(self, task_id, description, data_path, priority=1):
        super().__init__(task_id, description, priority)
        self.data_path = data_path

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"Data path: {self.data_path}"
        )


# 3. Загвар сургах даалгавар
class ModelTrainingTask(Task):
    def __init__(
        self, task_id, description, model_type,
        training_data_path, priority=1
    ):
        super().__init__(task_id, description, priority)
        self.model_type = model_type
        self.training_data_path = training_data_path

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"Model: {self.model_type}, "
            f"Training data: {self.training_data_path}"
        )


# 4. Загвар үнэлэх шинэ даалгавар
class ModelEvaluationTask(Task):
    def __init__(
        self, task_id, description, model_type,
        test_data_path, priority=1
    ):
        super().__init__(task_id, description, priority)
        self.model_type = model_type
        self.test_data_path = test_data_path

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"Model: {self.model_type}, "
            f"Test data: {self.test_data_path}"
        )


# 5. Дууссан даалгаврын түүх
class TaskHistory:
    def __init__(self):
        self.history = deque()

    def add_task(self, task):
        self.history.append(task)

    def undo_last(self):
        if not self.history:
            print("Түүхэнд буцаах даалгавар алга.")
            return None

        task = self.history.pop()
        print(f"Сүүлийн түүхийн бичлэг хасагдлаа: {task.task_id}")
        return task

    def show_history(self):
        print("\n--- Даалгаврын түүх ---")
        if not self.history:
            print("Түүх хоосон байна.")
        else:
            for task in self.history:
                print(task)


# 6. Даалгаврын дараалал удирдах класс
class TaskQueue:
    def __init__(self):
        self.queue = deque()
        self.history = TaskHistory()
        self.cancelled_tasks = {}

    def add_task(self, task):
        if task.status != "Pending":
            print("Алдаа: Зөвхөн хүлээгдэж буй даалгаврыг нэмнэ.")
            return

        self.queue.append(task)
        self.sort_queue()
        print(f"Даалгавар дараалалд нэмэгдлээ: {task.task_id}")

    # Өндөр priority утгатай даалгаврыг түрүүлж ажиллуулна.
    def sort_queue(self):
        self.queue = deque(
            sorted(
                self.queue,
                key=lambda task: task.priority,
                reverse=True
            )
        )

    # Даалгаврыг ID-аар цуцлах
    def cancel_task(self, task_id):
        # Эхлээд хүлээгдэж буй даалгавраас хайна.
        for task in list(self.queue):
            if task.task_id == task_id:
                self.queue.remove(task)
                task.set_status("Cancelled")
                self.cancelled_tasks[task_id] = task
                print(f"Даалгавар цуцлагдлаа: {task_id}")
                return True

        # Хэрэв өмнө нь цуцлагдсан бол дахин цуцлахгүй.
        if task_id in self.cancelled_tasks:
            print(f"{task_id} аль хэдийн цуцлагдсан байна.")
            return False

        print(
            f"{task_id} дараалалд байхгүй. "
            "Ажиллаж байгаа даалгаврыг энэ жишээ зогсоохгүй."
        )
        return False

    # Даалгаврын төрлөөс хамаарч өөр өөр боловсруулалт хийнэ.
    def _execute_task(self, task):
        print(f"\nДаалгавар эхэллээ: {task.task_id}")
        task.set_status("Running")

        try:
            if isinstance(task, DataProcessingTask):
                print(f"Өгөгдөл уншиж байна: {task.data_path}")
                time.sleep(0.5)
                print("Өгөгдлийг цэвэрлэж, боловсруулж байна...")
                time.sleep(0.5)

            elif isinstance(task, ModelTrainingTask):
                print(f"Загварын төрөл: {task.model_type}")
                print(f"Сургалтын өгөгдөл: {task.training_data_path}")
                time.sleep(0.5)
                print("Загварыг сургаж байна...")
                time.sleep(0.5)

            elif isinstance(task, ModelEvaluationTask):
                print(f"Үнэлэх загвар: {task.model_type}")
                print(f"Тестийн өгөгдөл: {task.test_data_path}")
                time.sleep(0.5)
                print("Загварын үзүүлэлтүүдийг тооцож байна...")
                time.sleep(0.5)
                print("Жишээ үнэлгээ: Accuracy = 0.92")

            else:
                print("Ерөнхий даалгавар боловсруулж байна...")
                time.sleep(0.5)

            task.set_status("Completed")
            print(f"Даалгавар амжилттай дууслаа: {task.task_id}")

        except Exception as error:
            task.set_status("Failed")
            task.error_message = (
                f"{type(error).__name__}: {error}"
            )
            print(f"Алдаа гарлаа: {task.error_message}")

        finally:
            self.history.add_task(task)

    # Дараалал дахь бүх даалгаврыг боловсруулах
    def process_tasks(self):
        if not self.queue:
            print("\nБоловсруулах даалгавар алга.")
            return

        while self.queue:
            task = self.queue.popleft()
            self._execute_task(task)

    def show_queue(self):
        print("\n--- Хүлээгдэж буй даалгаврууд ---")
        if not self.queue:
            print("Дараалал хоосон байна.")
        else:
            for task in self.queue:
                print(task)


# 7. Програмыг турших
if __name__ == "__main__":
    task_queue = TaskQueue()

    # Өөр өөр төрлийн даалгавар үүсгэнэ.
    task1 = DataProcessingTask(
        1, "Өгөгдөл цэвэрлэх", "data.csv", priority=2
    )

    task2 = ModelTrainingTask(
        2, "Загвар сургах", "RandomForest",
        "train.csv", priority=5
    )

    task3 = ModelEvaluationTask(
        3, "Загвар үнэлэх", "RandomForest",
        "test.csv", priority=4
    )

    task4 = DataProcessingTask(
        4, "Өгөгдөл хувиргах", "data2.csv", priority=1
    )

    # Даалгавруудыг дараалалд нэмнэ.
    task_queue.add_task(task1)
    task_queue.add_task(task2)
    task_queue.add_task(task3)
    task_queue.add_task(task4)

    # Давуу эрхээр эрэмбэлэгдсэн дарааллыг харуулна.
    task_queue.show_queue()

    # Хүлээгдэж буй даалгаврыг цуцлах.
    task_queue.cancel_task(4)

    # Даалгавруудыг боловсруулна.
    task_queue.process_tasks()

    # Гүйцэтгэлийн түүхийг харуулна.
    task_queue.history.show_history()