import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QProgressBar

class TextEditorApp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the UI layout
        layout = QtWidgets.QVBoxLayout()

        # Add a label and file selector for input file
        self.inputFileLabel = QtWidgets.QLabel('Select a .txt file:')
        layout.addWidget(self.inputFileLabel)
        self.inputFileButton = QtWidgets.QPushButton('Browse')
        self.inputFileButton.clicked.connect(self.select_input_file)
        layout.addWidget(self.inputFileButton)

        # Add a label and folder selector for output directory
        self.outputFolderLabel = QtWidgets.QLabel('Select an output folder: [default is /Results]')
        layout.addWidget(self.outputFolderLabel)
        self.outputFolderButton = QtWidgets.QPushButton('Browse')
        self.outputFolderButton.clicked.connect(self.select_output_folder)
        layout.addWidget(self.outputFolderButton)

        # Add a process button
        self.processButton = QtWidgets.QPushButton('Process')
        self.processButton.clicked.connect(self.process_files)
        layout.addWidget(self.processButton)

        # Add a progress bar
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setMaximum(100)
        layout.addWidget(self.progressBar)

        # Set the layout and window properties
        self.setLayout(layout)
        self.setWindowTitle('Simple Text Editor')
        self.setGeometry(100, 100, 400, 220)

    def select_input_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select a .txt file", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file:
            self.inputFileLabel.setText(f'Selected input file: {file}')
            self.input_file_path = file

    def select_output_folder(self):
        options = QFileDialog.Options()
        folder = QFileDialog.getExistingDirectory(self, "Select an output folder", "", options=options)
        if folder:
            self.outputFolderLabel.setText(f'Selected output folder: {folder}')
            self.output_folder_path = folder

    def process_files(self):
        try:
            # Default output folder to "results" directory in the root directory
            default_output_folder = os.path.join(os.getcwd(), "results")
            os.makedirs(default_output_folder, exist_ok=True)

            # Perform the processing
            input_file = getattr(self, 'input_file_path', None)
            output_folder = getattr(self, 'output_folder_path', default_output_folder)

            if not input_file:
                QMessageBox.warning(self, "Error", "Please select an input file.")
                return

            # Mock processing with progress update
            self.progressBar.setValue(0)
            QtWidgets.QApplication.processEvents()

            # Example of processing by reading lines
            with open(input_file, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()

            total_lines = len(lines)
            output_file = f"{output_folder}/processed_output.txt"

            with open(output_file, 'w', encoding='utf-8') as outfile:
                for i, line in enumerate(lines):
                    # Replace the following line with your actual processing logic
                    processed_line = line.strip()  # Example processing
                    outfile.write(processed_line + '\n')

                    # Update progress
                    progress = int((i + 1) / total_lines * 100)
                    self.progressBar.setValue(progress)
                    QtWidgets.QApplication.processEvents()

            QMessageBox.information(self, "Success", "Processing complete!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            self.progressBar.setValue(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TextEditorApp()
    window.show()
    sys.exit(app.exec_())
