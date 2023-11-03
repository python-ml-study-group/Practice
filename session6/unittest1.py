import unittest
def get_separator():
    return " "

def get_Fullname(lastname, firstname): 
    # This function returns the full name of a person
    if firstname == "":
        return lastname
    elif lastname == "":
        return firstname
    else:
        return lastname + get_separator() + firstname

class TestFullname(unittest.TestCase):
    def test_simpleTest(self):
        fullname = get_Fullname("Tayaloor", "Roopesh")
        self.assertEqual(fullname, "Tayaloor Roopesh")
    def test_onlylastname(self):
        fullname = get_Fullname("Tayaloor", "")
        self.assertEqual(fullname, "Tayaloor")
    def test_onlyfirstname(self):
        fullname = get_Fullname("", "Roopesh")
        self.assertEqual(fullname, "Roopesh")
    @unittest.skip("Testing skip")
    def test_checkbothblank(self):
        fullname = get_Fullname("", "")
        self.assertEqual(fullname, "")

if __name__ == '__main__':
    unittest.main()
