"""🔴 Challenge 3A: Multi-File App — ✅ SOLUTION"""
from agent import run_agent

if __name__ == "__main__":
    task = """Build contact book in 'contacts/':

models.py: Contact(name,phone,email), __str__, to_dict(), from_dict() classmethod
storage.py: CONTACTS_FILE, load/save/add/delete(case-insensitive)/search(partial match)
test_contacts.py: unittest, setUp/tearDown isolation, 8+ tests, roundtrip/CRUD/search

After creating: run tests, then demo add 2 contacts, list, search, delete, list again."""
    run_agent(task)
