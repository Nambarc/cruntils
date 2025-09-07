
# Core Python.

# 3rd party.
import os
import requests

class Artifactory:
    def __init__(self, username: str = "", password: str = ""):
        self.username = username
        self.password = password
    def upload_file(self, path: str, url: str):
        """Upload a file to Artifactory.

        path: The path to the file to upload.

        url: The URL at which to place the file.
        """

        # Check if the file exists.
        if not(os.path.isfile(path)):
            print(f"File '{path}' does not exist!")
            return

        # Could check if file already exists.
        # Have an arg to override if file already exists.
        # Does Artifactory support version tracking?
        #   If so, check version before and after if overriding?

        # Read data and upload file.
        # TODO: How to upload very large files...?
        with open(path, "rb") as file:
            data = file.read()
            response = requests.put(
                url,
                data,
                verify=False,
                auth=(self.username, self.password)
            )
            print(response.status_code)
            print(response.text)