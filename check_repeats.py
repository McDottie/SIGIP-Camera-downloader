import filecmp
import os
import cv2
import pytesseract


def dateExtraction(path):
    # Open the video file using cv2
    video = cv2.VideoCapture(path)
    # Set up tesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    # Set up the font for text extraction
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Set the top-right corner coordinates of the region where text should be extracted

    # Loop through each frame of the video
    while video.isOpened():
        # Extract the frame
        success, frame = video.read()
        width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
        heigth = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
        x1 = int(width/2)
        y1 = 0
        x2 = int(width)
        y2 = int(heigth/10)
        
        if not success:
            break

        # Crop the frame to the desired region
        cropped_frame = frame[y1:y2, x1:x2]

        # Convert the frame to grayscale
        gray = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2GRAY)

        # Run tesseract on the frame to extract the text
        text = pytesseract.image_to_string(gray)

        # Return the extracted text
        text = text.replace('\n', '')
        text = text.replace('\r', '')
        
        return text

    # Release the video file
    video.release()

class FileComparer:

  def search_files(extension, root_dir):
    """Searches the file tree for the two files with the specified names and extension"""
    file_bin_cnt = 0
    for root, dirs, files in os.walk(root_dir):
      for file in files:
        if file.endswith(extension):
            if file_bin_cnt == 0:
                file1_path = os.path.join(root, file)
            else:
                file2_path = os.path.join(root, file)

    return file1_path, file2_path

  def compare_files(file1_path, file2_path):
    """Compares the size and contents of the two files"""
    # Check if both files were found
    if file1_path is None or file2_path is None:
      return False

    # Check if the files are the same size
    file1_size = os.stat(file1_path).st_size
    file2_size = os.stat(file2_path).st_size
    if file1_size != file2_size:
      return False

    # Open the files and read their contents
    return filecmp.cmp(file1_path, file2_path, shallow=False)


folder1 = None
folder2 = None
file1 = None
file2 = None

for root, dirs, files in os.walk('.'):
    if (len(files) == 0 or 'info.json' in files) and len(dirs) > 1 and root.count('\\') > 1 and folder1 is None and folder2 is None:
        folder1 = root + '\\' + dirs[-1]
        folder2 = root + '\\' + dirs[-2]

    elif len(files) > 0 and folder1 is not None and folder2 is not None:
        if folder1 == root:
            file1 = folder1 + '\\' + files[0]
        if folder2 == root:
            file2 = folder2 + '\\' + files[0]

        if file1 is not None and file2 is not None:
            if filecmp.cmp(file1, file2, shallow=False):
                spliStr = folder1.split('\\')
                print("At road {0}, camera {1} did not update on last download. Folder -> {2} | LastUpdate {3}".format(spliStr[1], spliStr[2], folder1, dateExtraction(file1)))
                # print("Na estrada {0} a camera {1} nao faz update desde {2}".format(spliStr[1], spliStr[2], dateExtraction(file1)))
            folder1 = None
            folder2 = None
            file1 = None
            file2 = None
