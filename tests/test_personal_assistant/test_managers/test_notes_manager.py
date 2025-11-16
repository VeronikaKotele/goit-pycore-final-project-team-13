import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src'))

from personal_assistant.managers import NotesManager

class TestNotesManager(unittest.TestCase):
    def setUp(self):
        self.manager = NotesManager()
        # Clear any existing notes from cache to ensure clean test state
        self.manager._NotesManager__notebook.clear()

    def tearDown(self):
        if os.path.exists("notes_state.pkl"):
            os.remove("notes_state.pkl")

    def test_add_note(self):
        self.manager.add_note("Test Title", "Test note content")
        note_content = self.manager.find("Test Title")
        self.assertEqual(note_content, "Test note content")
        self.assertIn("Test Title: Test note content", self.manager.get_all_notes())

    def test_find_note_existing(self):
        self.manager.add_note("Find Title", "Find me")
        found_note = self.manager.find("Find Title")
        self.assertEqual(found_note, "Find me")

    def test_find_note_nonexistent(self):
        found_note = self.manager.find("Nonexistent Title")
        self.assertIsNone(found_note)

    def test_delete_note_existing(self):
        self.manager.add_note("Delete Title", "Delete me")
        self.manager.delete("Delete Title")
        found_note = self.manager.find("Delete Title")
        self.assertIsNone(found_note)
        self.assertNotIn("Delete Title: Delete me", self.manager.get_all_notes())

    def test_delete_note_nonexistent_raises(self):
        with self.assertRaises(KeyError):
            self.manager.delete("Nonexistent Title")

    def test_get_all_notes(self):
        self.manager.add_note("Title 1", "Note 1")
        self.manager.add_note("Title 2", "Note 2")
        all_notes = self.manager.get_all_notes()
        self.assertIn("Title 1: Note 1", all_notes)
        self.assertIn("Title 2: Note 2", all_notes)
        self.assertEqual(len(all_notes), 2)

    def test_update_note_existing(self):
        self.manager.add_note("Update Title", "Old content")
        self.manager.update("Update Title", "New content")
        updated_content = self.manager.find("Update Title")
        self.assertEqual(updated_content, "New content")

    def test_update_note_nonexistent_raises(self):
        with self.assertRaises(KeyError):
            self.manager.update("Nonexistent Title", "Content")

    def test_add_note_duplicate_title_raises(self):
        self.manager.add_note("Duplicate Title", "First content")
        with self.assertRaises(ValueError):
            self.manager.add_note("Duplicate Title", "Second content")

if __name__ == '__main__':
    unittest.main(verbosity=2)