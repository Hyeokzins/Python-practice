class Note(object):
    def __init__(self,contents=None):
        self.contents=contents

    def write_contents(self,contents):
        self.contents=contents

    def remove_all(self):
        self.contents=""
    def __str__(self):
        return self.contents

class Notebook(object):
    def __init__(self,title,page_number,notes):
        self.title=title
        self.page_number=1
        self.notes={}

    def add_note(self,note,page=0):
        if self.page_number <300:
            if page == 0:    
                self.notes[self.page_number]=note
                self.page_number+=1
            else:
                self.notes={page:note}
                self.page_number+=1

        else:
            print("Notebook is full")

    def remove_note(self,page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("Page not found")
    
    def get_number_of_pages(self):
        return len(self.notes.keys())
    
g_sentences="abcd"
note_1=Note(g_sentences)

g_sentences="1234"
note_2=Note(g_sentences)

g_sentences="king"
note_3=Note(g_sentences)

g_sentences="mon"
note_4=Note(g_sentences)

test_notebook=Notebook('Test Notebook')

test_notebook.add_note(note_1)
test_notebook.add_note(note_2)
test_notebook.add_note(note_3)
test_notebook.add_note(note_4)

print(test_notebook.get_number_of_pages())






        