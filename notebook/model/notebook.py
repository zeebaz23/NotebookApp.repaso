from datetime import datetime
from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    code: int
    title: str
    text: str
    importance: str
    creation_date: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def _str_(self) -> str:
        return f"Code: {self.code}\nCreation date: {self.creation_date}\n{self.title}: {self.text}"

class Notebook:
    def _init_(self):
        self.notes: Dict[int, Note] = {}

    def add_note(self, title: str, text: str, importance: str) -> int:
        code = len(self.notes) + 1
        self.notes[code] = Note(code, title, text, importance)
        return code

    def important_notes(self) -> List[Note]:
        return [note for note in self.notes.values() if note.importance in [Note.HIGH, Note.MEDIUM]]

    def tags_note_count(self) -> Dict[str, int]:
        tag_count = {}
        for note in self.notes.values():
            for tag in note.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1
        return tag_count

