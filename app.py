from notebook.view.ui_console import Console
from notebook.model.notebook import Notebook

if __name__ == "__main__":
    notebook = Notebook()
    console = Console(notebook)

    console.app_loop()
