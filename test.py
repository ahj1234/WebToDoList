import os
import unittest

from Classes.TO_DO_List import Task, To_Do
import main as app_module

os.system("cls")

class TestTask(unittest.TestCase):

    def test_attributes(self):
        t = Task("9-10", "Math", "Homework", taskID=0)
        self.assertEqual(t.Subject, "Math")
        self.assertEqual(t.Time_Range, "9-10")
        self.assertEqual(t.taskID, 0)

    def test_show(self):
        t = Task("9-10", "Math", "Homework")
        self.assertEqual(t.show(), ("9-10", "Math", "Homework"))


class TestToDo(unittest.TestCase):

    def setUp(self):
        self.todo = To_Do()

    def test_empty(self):
        self.assertEqual(self.todo.show(), {})

    def test_add(self):
        self.todo.add_new_task("9-10", "Math", "Homework")
        self.assertEqual(len(self.todo.show()), 1)

    def test_remove(self):
        self.todo.add_new_task("9-10", "Math", "Homework")
        id = list(self.todo.show().keys())[0]
        self.todo.rem(id)
        self.assertEqual(len(self.todo.show()), 0)



class TestRoutes(unittest.TestCase):

    def setUp(self):
        app_module.app.config["TESTING"] = True
        self.client = app_module.app.test_client()
        app_module.Current_List.cart.clear()

    def test_login_page(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_login_correct(self):
        res = self.client.post("/", data={"user": "test", "passw": "1234"})
        self.assertEqual(res.status_code, 302)

    def test_login_wrong(self):
        res = self.client.post("/", data={"user": "test", "passw": "wrong"})
        self.assertIn(b"alert", res.data)

    def test_dashboard(self):
        res = self.client.get("/Dashboard")
        self.assertEqual(res.status_code, 200)

    def test_add_task(self):
        self.client.post("/Dashboard", data={"subject": "Physics", "TimeRange": "10-11", "description": "Newton"})
        res = self.client.get("/Dashboard")
        self.assertIn(b"Physics", res.data)

    def test_delete_task(self):
        self.client.post("/Dashboard", data={"subject": "Physics", "TimeRange": "10-11", "description": "Newton"})
        id = list(app_module.Current_List.cart.keys())[0]
        self.client.post(f"/delete/{id}")
        res = self.client.get("/Dashboard")
        self.assertNotIn(b"Physics", res.data)


if __name__ == "__main__":
    unittest.main(verbosity=2)