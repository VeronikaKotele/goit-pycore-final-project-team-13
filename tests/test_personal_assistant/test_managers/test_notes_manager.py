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
        note = self.manager.find("Test Title")
        self.assertEqual(note.content, "Test note content")
        self.assertIn("Test Title: Test note content", self.manager.get_all_notes())

    def test_find_note_existing(self):
        self.manager.add_note("Find Title", "Find me")
        note = self.manager.find("Find Title")
        self.assertEqual(note.content, "Find me")

    def test_find_note_nonexistent(self):
        note = self.manager.find("Nonexistent Title")
        self.assertIsNone(note)

    def test_delete_note_existing(self):
        self.manager.add_note("Delete Title", "Delete me")
        self.manager.delete("Delete Title")
        note = self.manager.find("Delete Title")
        self.assertIsNone(note)
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
        self.assertEqual(updated_content.content, "New content")

    def test_update_note_nonexistent_raises(self):
        with self.assertRaises(KeyError):
            self.manager.update("Nonexistent Title", "Content")

    def test_add_note_duplicate_title_raises(self):
        self.manager.add_note("Duplicate Title", "First content")
        with self.assertRaises(ValueError):
            self.manager.add_note("Duplicate Title", "Second content")

    def test_add_tag_existing_note(self):
        self.manager.add_note("Tag Title", "Tag content")
        self.manager.add_tag("Tag Title", "urgent")
        note = self.manager.find("Tag Title")
        self.assertIn("urgent", note.tags)

    def test_add_tag_nonexistent_note_raises(self):
        with self.assertRaises(KeyError):
            self.manager.add_tag("Nonexistent Title", "tag")

    def test_search_by_tag_existing(self):
        self.manager.add_note("Note 1", "Content 1")
        self.manager.add_tag("Note 1", "work")
        self.manager.add_note("Note 2", "Content 2")
        self.manager.add_tag("Note 2", "personal")
        self.manager.add_note("Note 3", "Content 3")
        self.manager.add_tag("Note 3", "work")

        work_notes = self.manager.search_by_tag("work")
        self.assertEqual(len(work_notes), 2)
        titles = [note.title for note in work_notes]
        self.assertIn("Note 1", titles)
        self.assertIn("Note 3", titles)

    def test_search_by_tag_nonexistent(self):
        self.manager.add_note("Note 1", "Content 1")
        self.manager.add_tag("Note 1", "work")

        personal_notes = self.manager.search_by_tag("personal")
        self.assertEqual(len(personal_notes), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)